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

As a department we have agreed to use the AirBnb as our baseline for code styling. We use ESLint to ensure coding styles are followed. 

We install the required packages in a typescript project. 

* `@typescript-eslint/eslint-plugin`
* `@typescript-eslint/parser`
* `eslint`
* `eslint-config-airbnb-base`
* `eslint-config-airbnb-typescript` [Link](https://www.npmjs.com/package/eslint-config-airbnb-typescript)

For React Project we additionally add the following packages.

* `eslint-plugin-react`

We create an eslint config file with in the project. (.eslintrc.js)

```Javascript
module.exports = { 
  env: { 
    es2021: true, 
    node: true, 
  }, 
  extends: [ 
    'airbnb-base', 
  ], 
  parser: '@typescript-eslint/parser', 
  parserOptions: { 
    ecmaVersion: 'latest', 
    sourceType: 'module', 
  }, 
  plugins: [ 
    '@typescript-eslint', 
  ], 
  ignorePatterns: ['node_modules/'], 
  rules: { 
  }, 
  settings: { 
    'import/resolver': { 
      node: { 
        extensions: ['.js', '.jsx', '.ts', '.tsx'], 
      }, 
    }, 
  }, 
}; 
```

There is an option to override rules in the `rules` section in the eslintrc file.

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