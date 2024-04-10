---
title: React Best Practises
authors:
  - Rhodri Hewitson, Damjan Banjac
---

## Introduction

React is a popular open-source JavaScript library used for building user interfaces. It was created by Facebook and has gained a lot of popularity among developers for its declarative and efficient approach to building web applications. TypeScript is a superset of JavaScript that adds optional static typing and other features to the language. By using TypeScript with React, developers can write more reliable, maintainable, and scalable code with fewer errors. In this context, it's important to follow best practices and guidelines to ensure that your code is of the highest quality. In this post, we've provided some guidelines and best practices for writing React code in TypeScript that can help you write better code and improve the overall quality of your application.

## Guidelines for Writing React Code in TypeScript

### Writing in React

1. **Read and understand the official React documentation:** The React documentation at <https://react.dev/> is a valuable resource for learning about React and its ecosystem. Take the time to read and understand the documentation, and follow the best practices and recommendations provided by the React team. This will help you write better code and avoid common pitfalls in your React applications.

1. **Use semantic HTML:** React will still output HTML, CSS, and JavaScript; with that in mind, it's important we use semantic HTML tags that describe the content of the page rather than just the appearance. This will help with accessibility and search engine optimization, and make your code easier to read and maintain. For further reading, MDN has a good article on [semantic HTML](https://developer.mozilla.org/en-US../../Glossary/Semantics).

1. **Follow useState best practices:** Removing redundant and duplicate data from the state helps ensure that all its pieces stay in sync, similar to how a database engineer normalizes the database structure to minimize bugs. See [choosing the state structure](https://react.dev/learn/choosing-the-state-structure) for more information.

1. **Follow useEffect best practices**

   - **Don't use unnecessary useEffect:** Removing unnecessary Effects will make your code easier to follow, faster to run, and less error-prone. See [you may not always need an effect](https://react.dev/learn/you-might-not-need-an-effect#) for more information.

   - **Don't use objects in your useEffect:** Don't include objects in the dependency array, which can lead to unintended consequences. This is because objects are compared by reference, not by value. If the object reference changes, even if the object properties are the same, the effect will be triggered again. See [some reactive value change unintentionally](https://react.dev/learn/removing-effect-dependencies#does-some-reactive-value-change-unintentionally) for more information.

1. **Keep your components small and focused:** Break your UI into smaller, reusable components that are focused on a single responsibility. This will make your code easier to test, maintain, and understand. As a rule of thumb, aim to keep each component under 100 lines of code.

1. **Add global files:** Enhance the structure by introducing additional folders such as "constants" for storing application-wide constants, "colors" for maintaining a color palette, and "styles" for global CSS styling.

1. **Be careful of excessive prop drilling:** Avoid excessive prop drilling by using React Query or React Context. These provide a centralized store for managing the state of your application and can help you avoid passing props down through multiple levels of components. Alternatively lifting the state up can help reduce prop drilling see Kent C Dodds article on [application state management with react](https://kentcdodds.com/blog/application-state-management-with-react). React.dev also has a great tutorial on [managing state](https://react.dev/learn/managing-state). _Note we haven't yet needed a global state but lightweight libraries like [zustand](https://github.com/pmndrs/zustand) or [jotai](https://github.com/pmndrs/jotai) could fit that need depending on the use case._

1. **Reuse logic with custom hooks:** Extract reusable logic into custom hooks to avoid code duplication and improve the reusability of your components. Custom hooks can be used to encapsulate logic related to data fetching, state management, and other common patterns. By using custom hooks, you can make your code more modular and easier to test and maintain. See [reusing logic with custom-hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) for more details.

1. **Use strict mode:** Use the React strict mode to enable additional checks and warnings for potential problems in your code. This can help you catch potential issues early and improve the overall quality of your code.

### Structuring your code

1. **Use the Atomic Design Methodology:** The Atomic Design Methodology is a system for designing and building UI components in a structured and scalable way. By breaking down your UI into smaller, reusable components, you can create a more flexible and maintainable codebase. See Brad Frost article on [Atomic Design](https://atomicdesign.bradfrost.com/table-of-contents/) for more information.

1. **Use CSS modules or styled-components:** Use CSS modules or styled-components to manage the styling of your components. These tools provide a way to write scoped styles that are only applied to specific components and can help you avoid naming collisions and other styling issues.

1. **Use ESLint and Prettier:** Use [ESLint](https://eslint.org/) and [Prettier](https://prettier.io/) to enforce coding standards and formatting rules in your codebase. These tools can help you maintain consistency and improve the readability of your code.

### Fetching your data

1. **Use React Query:** React Query is a library for managing data fetching and caching in React applications. It provides a simple and intuitive API for fetching data from APIs, and supports caching, pagination, and other advanced features. See [ReactQuery](https://tanstack.com/query/v3../../react/overview) for more infomation.

   > _**Note:** the `onSuccess()`/`onError()`/`onSettled()` callback methods in `useQuery()` will be deprecated in [React Query v5](https://twitter.com/TkDodo/status/1647341498227097600)._

1. **Use async/await for data fetching:** Use async/await syntax to fetch data asynchronously from APIs or other sources. This can help you avoid callback hell and make your code easier to read and maintain.

### Testing your code

1. **Use React Testing Library:** Use React Testing Library to write unit and integration tests for your components. This library provides a simple and intuitive API for testing React components and encourages developers to write tests that reflect the way users interact with the application. See [React Testing Library](https://testing-library.com../../react-testing-library/intro/) for more information.

### Other things to be aware of

1. **Use TypeScript generics:** Use TypeScript generics to create reusable components and functions that work with a variety of data types. Generics provide a way to write type-safe code that can be used in a flexible and scalable way.

1. **Use type inference:** Let TypeScript infer types whenever possible, rather than specifying types explicitly. This will make your code more concise and easier to read. For example, you can use the const keyword to infer the type of a variable, and the as const assertion to infer the type of an object literal.

1. **Use the latest version of React and TypeScript:** Always use the latest version of React and TypeScript to take advantage of the latest features and bug fixes.

### When reviewing React code in pull requests (PRs), here are some important rules and considerations to keep in mind:

1. **Follow the style guide:** Ensure that the code follows the established coding conventions and style guide of the project. Consistent code style improves readability and maintainability.

1. **Code quality and readability:** Evaluate the code for clarity, readability, and maintainability. Look for concise and descriptive variable and function names, proper indentation, and comments where necessary.

1. **Modular and reusable components:** Encourage the use of modular components that have a single responsibility and can be easily reused throughout the application. Avoid large, monolithic components that are difficult to understand and maintain.

1. **Handling state and props:** Check if the state and props are used appropriately. Avoid unnecessary state management and prefer lifting the state up when needed. Ensure that props are properly validated using PropTypes or TypeScript interfaces.

1. **Conditional rendering:** Review the usage of conditional rendering. Make sure it is clear, concise, and avoids unnecessary complexity. Consider alternatives like using the logical AND operator (&&) instead of ternary operators for conditional rendering when applicable.

1. **Avoiding Unnecessary Closing Tags:** Make sure that closing tags are used only when necessary. In React, self-closing tags are preferred for elements that don't have any children. For example, instead of '<div></div>', you can use '<div />' to indicate a self-closing tag.

1. **Eliminate empty tags:** Check for instances where tags are rendered without any content or purpose. If a tag doesn't contain any meaningful content or attributes, it may be unnecessary and can be safely removed. Empty tags can clutter the code and make it harder to understand.

1. **Effective use of hooks:** Verify that React hooks like useState, useEffect, and useContext are used correctly. Ensure that hooks are placed in the correct order and follow the rules of hooks (e.g., not using hooks inside loops or conditionals).

1. **Performance considerations:** Assess the code for any potential performance bottlenecks. Look for inefficient rendering, excessive re-renders, or unnecessary computations. Suggest optimizations if applicable, such as memoization or using useMemo and useCallback hooks.

1. **Error handling:** Check if error handling is implemented appropriately. Look for proper error boundaries, handling of asynchronous errors, and displaying helpful error messages to users.

1. **Test coverage:** Evaluate if the code changes are adequately covered by unit tests or integration tests. Encourage adding or updating tests to maintain good test coverage.

1. **Consistency with existing codebase:** Ensure that the code aligns with the existing architecture, patterns, and practices followed in the project. Maintain consistency to avoid introducing unnecessary deviations.
