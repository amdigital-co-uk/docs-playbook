## C# Coding Conventions

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

## TypeScript and JavaScript Coding Conventions

AM follows a code style for TypeScript and JavaScript that is based on [Airbnb's JavaScript Style Guide](https://airbnb.io/javascript/) and [React/JSX Style Guide](https://airbnb.io/javascript/react/).

This is enforced in codebases through the use of a .prettierrc file and a .eslintrc.json files, the contents of which are detailed below. These files should be added to the root folder of projects where TypeScript and/or JavaScript is written.

**.prettierrc**

```json
{
  "arrowParens": "avoid",
  "bracketSpacing": true,
  "htmlWhitespaceSensitivity": "css",
  "insertPragma": false,
  "bracketSameLine": false,
  "jsxSingleQuote": false,
  "printWidth": 80,
  "proseWrap": "always",
  "quoteProps": "as-needed",
  "requirePragma": false,
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "useTabs": false,
  "endOfLine": "lf"
}

```

**.eslintrc.json**

```json
{
  "root": true,
  "ignorePatterns": [
    "**/*"
  ],
  "parser": "@typescript-eslint/parser",
  "extends": [
    "airbnb/base",
    "plugin:prettier/recommended",
    "plugin:unicorn/recommended",
    "plugin:compat/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:security/recommended",
    "plugin:jsx-a11y/recommended",
    "plugin:jest/recommended",
    "plugin:jest-dom/recommended",
    "plugin:mdx/recommended",
    "plugin:no-unsanitized/DOM"
  ],
  "env": {
    "browser": true
  },
  "plugins": [
    "@typescript-eslint",
    "@nx",
    "import",
    "security",
    "jsx-a11y",
    "jest",
    "@emotion"
  ],
  "settings": {
    "import/resolver": {
      "typescript": {
        "project": "tsconfig.base.json"
      }
    }
  },
  "overrides": [
    {
      "files": [
        "*.ts",
        "*.tsx",
        "*.js",
        "*.jsx"
      ],
      "rules": {
        "@nx/enforce-module-boundaries": [
          "error",
          {
            "enforceBuildableLibDependency": true,
            "allowCircularSelfDependency": true,
            "allow": [],
            "depConstraints": [
              {
                "sourceTag": "*",
                "onlyDependOnLibsWithTags": [
                  "*"
                ]
              }
            ]
          }
        ],
        "import/order": [
          "error",
          {
            "groups": [
              [
                "builtin",
                "external"
              ],
              [
                "parent",
                "internal",
                "sibling",
                "index"
              ]
            ],
            "pathGroups": [
              {
                "pattern": "@am-ui-applications/**",
                "group": "internal"
              }
            ],
            "alphabetize": {
              "order": "asc"
            },
            "newlines-between": "always"
          }
        ],
        "import/no-extraneous-dependencies": "off",
        "import/prefer-default-export": "off",
        "import/extensions": [
          "error",
          "always",
          {
            "ts": "never",
            "tsx": "never",
            "js": "never",
            "jsx": "never"
          }
        ],
        "no-console": "off",
        "no-duplicate-imports": "error",
        "no-irregular-whitespace": "error",
        "no-shadow": "off",
        "no-use-before-define": "off",
        "no-restricted-exports": "off",
        "security/detect-object-injection": "off",
        "unicorn/no-array-reduce": "off",
        "unicorn/no-null": "off",
        "unicorn/prefer-module": "off",
        "unicorn/filename-case": "off",
        "unicorn/no-array-for-each": "off",
        "unicorn/no-for-loop": "off",
        "unicorn/prevent-abbreviations": [
          "error",
          {
            "allowList": {
              "getServerSideProps": true,
              "getStaticProps": true
            },
            "replacements": {
              "env": {
                "environment": false
              },
              "props": {
                "properties": false
              },
              "lib": {
                "library": false
              }
            }
          }
        ],
        "jest/expect-expect": [
          "error",
          {
            "assertFunctionNames": [
              "expect",
              "cy.**.should",
              "**.contains"
            ]
          }
        ],
        "@emotion/syntax-preference": [
          2,
          "object"
        ],
        "@emotion/jsx-import": "error",
        "@emotion/no-vanilla": "error",
        "@emotion/import-from-emotion": "error",
        "@emotion/styled-import": "error"
      }
    },
    {
      "files": [
        "*.ts",
        "*.tsx"
      ],
      "extends": [
        "plugin:@nx/typescript"
      ],
      "rules": {
        "@typescript-eslint/no-empty-function": "off",
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/ban-ts-comment": "off",
        "@typescript-eslint/no-unsafe-call": "off",
        "@typescript-eslint/no-unsafe-assignment": "off",
        "@typescript-eslint/no-unsafe-member-access": "off",
        "@typescript-eslint/explicit-function-return-type": "off",
        "@typescript-eslint/interface-name-prefix": "off",
        "@typescript-eslint/no-use-before-define": [
          "error"
        ],
        "@typescript-eslint/no-unused-vars": "off",
        "@typescript-eslint/no-shadow": "error",
        "unicorn/prefer-node-protocol": "off"
      }
    },
    {
      "files": "*.json",
      "parser": "jsonc-eslint-parser",
      "rules": {}
    },
    {
      "files": "jest.config.ts",
      "rules": {
        "unicorn/no-abusive-eslint-disable": "off"
      }
    }
  ]
}
```

## Terraform Standards

### General Style Guide

Terraform files should obey the syntax rules for the [HashiCorp Configuration Language (HCL)](https://www.terraform.io/language/syntax/configuration) and [the general formatting guidelines](https://www.terraform.io/cli/commands/fmt) provided by the Terraform Project through the `fmt` command.

In addition, Adam Matthew Digital follows the following standards when writing Terraform:

- Use [Snake Case](https://en.wikipedia.org/wiki/Snake_case) for all resource names
- Use descriptive and non environment specific names to identify resources
- Declare all variables in `variables.tf`, including a description and type
- Specify sensible defaults in `variables.tf` where appropriate, rather than forcing every variable to be explicitly defined in `.tfvars` files
- Prefer using variables with defaults over hard-coding values in resources
- Declare all outputs in `outputs.tf`, including a description
- Pin all modules and providers to a specific version or tag
- Always use relative paths and [the file() helper](https://www.terraform.io/language/functions/file) when needing to work with external files
- Prefer seperate resources over inline blocks (e.g. `aws_security_group_rule` over `aws_security_group`)
- Always define the AWS region as a variable when building modules
- Always use workspace variables in an `envs` folder, `{component}/envs/{workspace}.tfvars`
- Always use `maps` over `sets` or `lists` when the variable is used for iterations such as `for_each` loops 
    - Managing resources via indexes has horrible ramifications when the data structure is changed and can cause resources to be re-created/deleted unnecessarily as Terraform can quite easily loose track of what index is mapped to what resource

### Running terraform

- All changes should be made through CI/CD tooling, and Terraform should not be run locally - especially `terraform apply`
- Terraform versions and provider versions should be pinned, as [it's not possible to safely downgrade a state file](https://github.com/hashicorp/terraform/issues/16879) once it has been used with a newer version of Terraform
- Use [S3 (standard region) with DynamoDB locking](https://www.terraform.io/language/settings/backends/s3), with versioning and server-side encryption in S3
    - Standard bucket name: `amdigital-co-uk-infrastructure-state`
    - State key: `{component}.tfstate`
    - KMS Key Id: `alias/terraform_bucket_key`
    - DynamoDB Table: `terraform-state`
- Always use the `workspace_key_prefix` set to `env`
- Always format the terraform files before requesting a PR (`terraform fmt -recursive`)

### Using Shared Resources

In Terraform there are two ways to use shared resources: [Data Sources](https://www.terraform.io/language/data-sources), and [Importing](https://www.terraform.io/cli/import).

Ideally we would never really use **Importing** as a method of re-using existing architecture, but it becomes necessary when the resource we wish to use is not managed by any Terraform State. Even then more times than not there is likely a **Data Source** from the infrastructure provider (`AWS`, `Azure` etc), that enables the ability to lookup the resource and access its information.

Importing should only be used when we need to _modify_ and now track an existing resource, that is not already being managed by Terraform in some capacity.

With Data Sources we have the data source resource blocks provided by the providers, as well as the ability to load in output variables from other remote states using the [terraform_remote_state](https://www.terraform.io/language/state/remote-state-data) data source block.

In the scenario that there is a resource (such as a `vpc`) that needs re-using across multiple terraform projects, the shared resource should be created and managed seperately in its own project/component, and then the other projects/components should either use the `terraform_remote_state` to access the information (such as `id`, or `subnets` etc.) where needed or use a data source from the provider to lookup the resource (if possible) and gain access to its information that way.

### Writing and organizing Terraform with modules

A common recommendation in the Terraform community is to think of modules as functions that take an input and provide an output. Modules can be used to create lightweight abstractions, so that you can describe the infrastructure in terms of its architecture, rather than directly in terms of physical objects. 

Modules can be built in shareable repositories, or locally within a component repository. If you find yourself writing the same set of resources or functionality over and over again, consider building a module instead.

When to consider writing a module:

- When multiple resources should always be used together (e.g. a CloudWatch Alarm and EC2 instance)
- When module re-use is shallow (preferably don't nest modules)
   - Over using modules can make the Terraform configuration harder to understand and maintain so it is recommended to use modules in moderation
- When you cannot find a module on the [Terraform Registry](https://registry.terraform.io/) for the functionality you need

It is _not_ recommended by Hashicorp to write modules that are just thin wrappers around single other resource types. If you have trouble finding a name for your module that isn't the same as the main resource type inside it, that may be a sign that your module is not creating any new abstraction and so the module is a adding unnecessary complexity. Just use the resource type directly in the calling module instead.

For more information around modules and how to structure them take a look at the [Official Hashicorp documentation](https://www.terraform.io/language/modules/develop/structure).

### Module Standards

When creating a module, any contributions should follow these guidelines.

- Use semantic versioning for shared code and modules
- Always point to Github releases (over a binary or master) when referencing external modules
- Always extend, don't re-create resources manually
- Modules should be built using the standard files: `main.tf`, `variables.tf`, `output.tf`, `versions.tf`
- Readme files should contain a description of the module as well as documentation of variables. 
- Use [terraform-docs](https://terraform-docs.io/) for auto-generation of markdown for:
    - The requirements of the module
    - What providers are used
    - Any modules that are used within the module itself
    - The resources that are generated by the module
    - Inputs for the module (including description and default values)
    - Any outputs produced and exported by the module
- Use [Github's .gitignore contents for Terraform](https://github.com/github/gitignore/blob/master/Terraform.gitignore)
- Take a map of common tags as an input which should be applied to **_all_** resource blocks that support `tags`