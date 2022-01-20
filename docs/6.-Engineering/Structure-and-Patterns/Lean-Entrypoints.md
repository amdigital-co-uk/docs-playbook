[[_TOC_]]

## Code Structure

All the C# code we write for microservices runs in one of the following contexts, referred to here as different types of "entry point". They are all different ways of "getting stuff done" within the platform.

* HTTP Endpoint (or Microservice endpoint, or Microservice request)
* [Background Task](#background-tasks)
* [Message Queue handler](#message-queue-handlers)
* [Regular Task](#regular-tasks)

Each type of entry point serves a slightly different use-case, and should follow the appropriate conventions and patterns, which are described below. Ideally, all entry points should be very lean, and should call off to an `ISomethingService` (also called an IOC Service, after the Inversion of Control Pattern) to perform the bulk of the work. The advantage of this approach is that Unit Tests can focus on testing the IOC service, whilst the entry points stay very "dumb".

## HTTP Endpoints

HTTP endpoints (aka. microservice endpoints) are the main way of starting an action in the platform, and most developers will be very familiar working with them. They are the only type of entry point that block untill they are finished, and the only type that provide a response. So if you need to retrieve a piece of information, an HTTP endpoint is the only option.

Virtually all endpoints in Quartex are implemented as actions within MVC Controllers.

### Endpoint Best Practices

* Follow the [endpoint naming](/Platform-Development-Playbook/Engineering/Quality-Standards/Endpoint-Naming-Conventions) best practices
* Controllers should be very lean:
    * Collect the input from the request
    * Perform basic validation (e.g. are all required parameters correct? More complex validation e.g. does an asset exist for a given ID should belong in the controller)
    * Call an IOC Service to perform the meat of the request
    * Minimal code to return the result from the IOC Service
* Use `new ServiceResult()` to wrap up the C# result object into an HTTP response

The ideal endpoint code would look like this. In practice, it may be necessary to process some of the parameters somewhat before passing them to the IOC service.

```cs
[HttpGet("endpoint")]
public Task<IActionResult> Endpoint(SomeRequest request)
{
    var response = await _service.DoSomething(request);

    return new ServiceResult(response);
}
```

The service method should do all the error trapping and ensure the returned response object sets the `Status` property appropriately based on success or failure more. The advantage of ths approach is that the error trapping can be effectively Unit Tested.

## Background Tasks

Background tasks in Quartex use the HangFire library. Background tasks will be kicked off by making a microservice request to the microservice that runs the task. The endpoint will then add the background task to the queue via Hangfire. Background Tasks are well suited to use-cases where there is either one single large job that needs to be done, or there are lots of items but they need to be done in a specific order, or can influence each other.

### Background Task Best Practices

Background tasks have specific concerns around silent failures, retries and updating the user on the process of the task. 

* Create an entry on the processes page to keep the user updated
    * Avoid creating duplicate jobs
    * Ensure the job is "finished" whether in success or failure
* Ensure that failures are detected
* Cater for long running tasks

Following the pattern below should ensure all the concerns are dealt with:

```cs
public async Task Run(TaskParameters parameters, IJobCancellationToken cancellationToken)
{
    var context = parameters.GetContext();

    try
    {
        await service.DoTheWork(parameters, context);
    }
    catch (Exception e)
    {
        if (!context.LastAttempt)
        {
            // If there are more attempts to come, log the error and re-throw the exception to trigger the next retry
            _logger.LogError(e, "Error DOING SOMETHING for {ClientKey}: {Retries} retries", parameters.ClientKey, context.Retry);
            throw;
        }
        else
        {
            // Otherwise ensure the UI is updated
            await _serviceClient.Request<UpdateJobRequest, UpdateJobResponse>(new UpdateJobRequest
            {
                ClientKey = parameters.ClientKey,
                JobId = parameters.JobId,
                Status = BatchJobStatus.CompleteWithErrors
            });
        }
    }

}
```

Firstly, ensure that the endpoint that queues the task up via hangfire is what creates the Job on the processes page, and the JobId passed in via the job's parameters. This ensures that only one job is created. If the Job is created within the background task itself, there is the risk that should the task fail on the first attempt, subsequent attempts will create duplicate jobs.

Next, the `BackgroundTaskContext` object (which can be retrieved from the task parameters) provides information about how many attempts have been made at the job so far. The pattern demonstrated above with the try/catch and a check against the `LastAttempt` property should ensure:

* The task is re-attempted where possible
* The Job on the processes page is updated should all attempts fail

### Long running background tasks: the re-entrant pattern

Another specific concern with Background Tasks that take a long time is the possibility of the microservice restarting (or being scaled down) whilst the task is still running.

A Background Task should process a single batch of input, meaning it will only run for a limited amount of time and has a good chance of processing the batch it is responsible for before potentially getting restarted. As such, the `TaskParameters` object will need a parameter such as `BatchNumber` or `Skip` for example, so it knows what work to do.

When the background task finishes, it would then kick off the next iteration of itself (with an updated `BatchNumber` or `Skip` parameter as appropriate), which will process the next batch of items, and so on and so forth until the last item is processed. Each task would be responsible for updating the status/percentage of the job on the processes page, and the *last* job would be the one to set the status to Complete or Failed.

This is an example of the `ISomethingService` method which does the real work of the background task:

```cs
public async Task DoTheWork(TaskParameters parameters, BackgroundTaskContext context)
{
    if (parameters.Skip == 0)
    {
        // this will only run on the first iteration
    }

    // 
    var allItems = _otherService.GetAllItems();
    var batch = allItems.Skip(parameters.Skip).Take(_batchSize);

    // Process items in the batch
    foreach (var item in batch)
    {
        await ProcessItem(item);
    }

    if (parameters.Skip + _batchSize >= allItems.Count())
    {
        // finished case
        _serviceClient.Request<UpdateJobRequest, UpdateJobResponse>(new UpdateJobRequest
        {
            ClientKey = parameters.ClientKey,
            JobId = parameters.JobId,
            Status = BatchJobStatus.Complete
        });
    }
    else
    {
        // kick off next batch
        parameters.Skip += _batchSize;

        _backgroundTasks.Start<ITask, ITaskParameters>(parameters);
    }
}
```

One thing to be careful of in this pattern is how we retrieve the items to be worked on. It may be a good idea to retrieve the list of items and store them in the cache for faster retrieval.

Likewise, if the act of processing items would change the results of the query we make to retrieve the list of items in the first place, that can be problematic. Imagine a method called `GetAllIncompleteAssets()` in a task that needs to mark those assets as `Complete`. The very act of marking some of them complete will mean that future calls to `GetAllIncompleteAssets()` will return fewer items... this would be another good instance to store the list of items in the cache for all future iterations of the background task to process.

## Message Queue Handlers

Message Queue handlers wait for messages to arrive on the queue and process each item independently. The MQ is well suited to use-cases where there are lots of very small items to be processed (like "OCR this single image") and when each item can be processed in any order without impacting any others, or for small discrete jobs that won't take very long.

If an MQ handler might feasibly take more than a minute, it is probably better suited to being refactored as a Background Task.

### MQ Handler Best Practices

MQ handlers should live in a controller class, and can be considered quite similar to HTTP endpoints, with the exception that they don't return a response as such.

* MQ Handlers should be very lean
    * Collect the input from the message
    * Call an IOC Service to perform the real work
    * Minimal code to return success or failure
* Ensure that errors are caught and the appropriate status is returned

MQ handlers, like background tasks work in the background (with less visibility to an end user), so as a result it is important that they are retried in the event of a failure or exception. It is however possible to return `HandleMessageStatus.FailNoRetry` to skip retries in the event that the piece of work being requested is invalid (e.g. validation error, missing parameters etc).

The below is an example of how to implement an MQ handler that follows the above principles:

```cs
public async Task<HandleMessageStatus> UpdateSingleItem(UpdateItemMessage message, MessageContext context)
{
    try
    {
        await _updateSingleItem(message.ClientKey, message.ItemId);
    }
    catch (InvalidOperationException ioe)
    {
        _logger.LogError(ioe, "Invalid message on the Queue for item with Id {ItemId} for {ClientKey}: {Error}", message.ItemId, message.ClientKey, ioe.Message);
        return HandleMessageStatus.FailNoRetry;
    }
    catch (Exception e)
    {
        _logger.LogError(e, "Could not update single item with Id {ItemId} for {ClientKey}", message.ItemId, message.ClientKey);
        return HandleMessageStatus.Failed;
    }

    return HandleMessageStatus.Success;
}

```

## Regular Tasks

Background tasks in Quartex use the `IHostedService` [feature of dotnet core](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-2.2). As with all other types of Entry Point, Regular Tasks should be very skinny and most of the work should be done in an `ISomethingService`.