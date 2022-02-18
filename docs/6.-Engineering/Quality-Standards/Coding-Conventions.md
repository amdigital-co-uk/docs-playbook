[[_TOC_]]

# C# Coding Conventions

Our coding standards use the Microsoft [C# conventions](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions). All engineers must use and be familiar with them.

## Additional in-house conventions

Controllers (and other [code entry points](/Platform-Development-Playbook/Software-Engineering-Practices/Architecture-&-Infrastructure/Structure-and-Patterns/Lean-Entrypoints) like Background Tasks and Message Queue Message Handlers which are similar to controllers) should be kept as lean as possible. Each controller should dependency inject a Service that is responsible for business logic.
- The controller should do some basic input validation (returning an appropriate error code if validation fails) and then call the service to perform the bulk of the work.
- The main service can then inject as many other classes as it needs to perform its function.

Smaller repeated snippets of code should be refactored out and made re-usable, using one of the following approaches:
- Simpler pieces of code can be grouped into static methods within a `SomethingHelper` class
- Extension methods should generally be grouped together based on the class they extend, and be called `MyClassExtensions`
- Consider whether any refactored code could be useful moved into a shared package for re-use in other repositories

For constructing a small string, use String Interpolation (i.e. `string formatted = $"My variable is {variable}"`) rather than `string.Format()`. However if you need to log the value of a string, remember to use Serilog logging properties.

For constructing a larger string e.g. within a loop, use `StringBuilder` instead of concatenating many strings together.

Unit and Integration tests should make use [Shouldly](https://github.com/shouldly/shouldly#readme) instead of `Assert.That` to make assertions more readable.


# Conventions for package inclusion
When including packages/dependencies (internal or external) allways use a set package version, do not specify app version with wildcards or a minimum version of an package.

# TypeScript and JavaScript Coding Conventions

> _TODO: document this section and link to an industry-standard style guide_
