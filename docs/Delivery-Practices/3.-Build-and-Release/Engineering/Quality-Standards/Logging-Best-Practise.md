## Dotnet Best Practise

Engineers **should** use Log message template when generating log messages [(See Here)](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-5.0#log-message-template-1)

## TypeScript Best Practice

Engineers **should not** use `console.log` directly, as this can be visible by end users. 
_Alternatively we should be using the `Tracer` objects from the `Eden.Scripts` library. [(See Monitoring Tips)](/Platform-Development-Playbook/Monitoring-Tips)_


## General Best Practice
Engineers **should** provided enough information engineers understand what was happening when reading the log 
e.g. Log the client key responsible for the call ```_logger.LogInformation("Create Controlled Vocabulary '{VocabName}' for client {clientKey}", request.ControlledVocabulary.Name, clientKey);```

Engineers **should** use the correct log level when generating logs [(see here)](https://docs.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.loglevel?view=dotnet-plat-ext-5.0)


