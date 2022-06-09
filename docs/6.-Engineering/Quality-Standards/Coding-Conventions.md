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

# TypeScript and JavaScript Coding Conventions

There are a few handbooks out there that help with coding style for typescript. 

Google and AirBnb have alot of backers with regards to their styles. When using eslint in a project, we can install specific packages that will help set the rules. i.e. [Eslint Airbnb Config](https://www.npmjs.com/package/eslint-config-airbnb-typescript)

The AirBnb Guideline is located here https://github.com/airbnb/javascript although this is saying Javascript, alot of this can be applied to the typescript styling. 

Examples of code styling are below 

Consistent use of Qutoes, although single and double quotes are interchangable for strings in typescript/javascript, guides suggest use of one version.
```typescript

const myString = 'Hello world'; //Use single quotes
const myOtherString = "Hello world"; //Dont use double quotes

```
Single quotes is most commonly used


Using `const` over `var` and `let` unless the value is going to change, use `let`
```typescript

const someValue = 1; //Value will not change

let someOtherValue = 1; //Value most likely to change
someOtherValue = 2;

```
Try to avoid the use of `var` as this is globally scoped, where as `const` and `let` are scoped locally. 

Not exceeding max line length 
```typescript
//Long line (using react for illastration purposes)
const TextField:FC<TextFieldProps> = (props) => <MuiTextField disabled={props.disabled} required={props.required} type={props.type} variant={props.variant} label={props.label} />;

//Broken down
const TextField:FC<TextFieldProps> = (props) => (
    <MuiTextField disabled={props.disabled}
                  required={props.required}
                  type={props.type}
                  variant={props.variant}
                  label={props.label} />
);
```