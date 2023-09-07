## Fundamentals
Read and be familiar with the following:

* [Exception Fundamentals](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/) 
* [Using Exceptions Fundamentals](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/using-exceptions)
* [Exception Handling Fundamentals](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/exception-handling)
* [Creating and Throwing Exceptions Fundamentals](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/creating-and-throwing-exceptions)
* [Compiler-generated Exceptions Fundamentals](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/compiler-generated-exceptions)
* [Best Practices for Exceptions](https://docs.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions)
* [Using Standard Exception Types](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/using-standard-exception-types)


## Best Practices

Engineers **should** follow Microsoft Exception Best Practises.

Engineers **should not** throw `System.Exception, System.SystemException, System.NullReferenceException, or System.IndexOutOfRangeException` in their own code.

Engineers **should** throw predefined Exceptions when it is suitable to do so e.g. `ArgumentNullException`

Engineers **should** only create Exceptions when predefined ones do not exist, **but** should priorities specificity over a less detailed generic predefined exception. 
e.g. Create custom `OutOfMoneyException` instead of `InvalidOperationException("OutOfMoney")`

Engineers **should** only catch specific types of exceptions not a general Exception catch.

Engineers **should** use finally blocks to clean up resources even if no exceptions have been caught. 