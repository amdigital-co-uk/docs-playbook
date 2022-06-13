
The following guidelines are adapted from the [REST API Tutorial](https://restfulapi.net/resource-naming/).

## Endpoint path conventions

All our microservice endpoints should start with a **version** (e.g. `v1`,  `v2` etc.), which will have different uses depending on the context. Most microservice endpoints will also relate directly either to a specific **Client** or specific **Website**; although some microservices don't require this (e.g. the File Validation service):

* `/{version}/{ClientKey}/rest/of/url` - Version and ClientKey
* `/{version}/{WebsiteKey}/rest/of/url` - Version and WebsiteKey
* `/{version}/rest/of/url` - Version only

Requests paths should use plural nouns, and indicate the hierarchy of the objects that they represent as much as possible. It can be helpful to think of every endpoint path as representing a specific object (or a specific set of objects).

* `/{version}/{client}/jobs` - Get all Jobs
* `/{version}/{client}/jobs/{JobId}` - Get details for a single Job
* `/{version}/{client}/jobs/{JobId}/items` - Get all the Items for a single Job
* `/{version}/{client}/jobs/{JobId}/items/{ItemId}` - Get details for a single Item within a given Job

> **NOTE**: _avoid_ using verbs in endpoint paths wherever possible. E.g. don't use `getasset/{assetId}` because the **get** is already in the HTTP verb. This leads nicely onto the following section...

## Use the relevant HTTP Verb for each action.

* Use `GET` requests for reading data
* `POST` requests should be creating new items or uploading files
* `PUT` requests should be used for updating existing items
* `DELETE` requests should be used for deleting data

If we consider each endpoint's path to be a specific object, then it makes sense that each HTTP verb is performing the relevant action on that object. E.g. a `GET` request will retrieve the object, a `PUT` request will modify the same object, and a `DELETE` request would delete that same object.

For `GET` requests, only identifiers (e.g. numerical IDs or Paths) should go in to the URL; filters, sorting or pagination (i.e. `skip` and `take`) parameters should be included as Query String values (implement the `IQueryStringRequest` interface). In extreme cases it might be necessary to use a `POST` request to include all the required parameters but avoid doing this if at all possible as it strictly speaking the wrong verb. Some examples below:

* `/{version}/{client}/assets/{skip}/{take}` - instead use `/{version}/{client}/assets?skip={skip}&take={take}`

In principle, there could be several identical looking URLs - but using different HTTP Verbs would perform different actions. E.g.

* `GET /{version}/{client}/jobs` - Get all jobs. This may include pagination or filtering as query string 
* `GET /{version}/{client}/jobs/{JobId}` - Get details for a specific job
* `PUT /{version}/{client}/jobs/{JobId}` - Update a job (e.g. set its status to Complete - the exact properties to be updated would live in the request body)
* `DELETE /{version}/{client}/jobs/{JobId}` - Delete the job

Wherever possible **avoid putting an action into the URL** if it can be indicated by the HTTP Verb. The only exception to this is where there are multiple similar actions that would otherwise need identical URLs. For example:

* `POST /{version}/{client}/assets/deleteasset/{id}` - this is very bad practice, instead use the below
* `DELETE /{version}/{client}/assets/{id}` - this performs a soft delete on the asset with the specified id
* `DELETE /{version}/{client}/assets/{id}/_force` - this performs a hard delete on the same asset

The last case is effectively a variation on the previous action, so adding an extra path component for differentiation is acceptable. Use the convention of adding an underscore to signal this variation.

## Filtering and pagination

Wherever possible, a `GET` request should always be used for _reading_ data. If an endpoint represents a collection of objects, (e.g. `/{version}/{client}/assets` might represent all Assets for a client), then use query string parameters to allow the caller to retrieve the objects they need.

* Use `?skip` and `?take` parameters to allow the caller to perform pagination
* Use `?sortBy` and `?sortDir` parameters to allow the caller to specify sort ordering
* Provide whatever parameters make sense in the context of the use-case to allow filtering. E.g. you might provide
    * `?collections=A,B` to filter by collection A or collection B
    * `?status=InComplete,ForReview` to filter by assets where the status is Incomplete for For Review

A `POST` request should only ever be used in the case where the maximum length of a query string is insufficient to supply the complexity of the parameters. A caveat for the previous rule is using `POST` while sending sensitive data, as POST data doesn't get cached or stored. When using `GET` request with query parameters these could potentially be cached or saved in a log, so using a `POST` has better security implications.

## Make API Endpoints as generic as possible

Try to avoid having multiple endpoints that do similar things. E.g. instead of having multiple endpoints to get a different set of assets for different purposes, instead extend the existing endpoint to provide more flexibility. E.g. assume we have the following existing endpoint that is already used for Manage Assets:

* `GET /{version}/{client}/assets` - Assumes filtering and pagination are provided by Query String parameters

Imagine then that someone needed to get a list of assets for promotion to a website; the example above might not quite meet their needs as it includes metadata-only records for example, so they decide to create a new endpoint specific to their use-case.

* `GET /{version}/{client}/assets/for-promotion/{WebsiteKey}`

However this isn't ideal, as it creates more code that needs to be maintained and tested. Instead they could simply extend the existing endpoint to add a `?includeMetadataOnly=false` query string value to make sure the existing endpoint works for them too.