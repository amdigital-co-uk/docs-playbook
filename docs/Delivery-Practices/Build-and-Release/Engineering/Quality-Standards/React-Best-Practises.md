---
title: React Best Practises 
authors: 
- Rhodri Hewitson
---

## Introduction

React is a popular open-source JavaScript library used for building user interfaces. It was created by Facebook and has gained a lot of popularity among developers for its declarative and efficient approach to building web applications. TypeScript is a superset of JavaScript that adds optional static typing and other features to the language. By using TypeScript with React, developers can write more reliable, maintainable, and scalable code with fewer errors. In this context, it's important to follow best practices and guidelines to ensure that your code is of the highest quality. In this post, we've provided some guidelines and best practices for writing React code in TypeScript that can help you write better code and improve the overall quality of your application.

## 

## Guidelines for Writing React Code in TypeScript

1. Use semantic HTML: Use semantic HTML tags that describe the content of the page rather than just the appearance. This will help with accessibility and search engine optimization, and make your code easier to read and maintain. For further reading, MDN has a good article on [semantic HTML]( https://developer.mozilla.org/en-US/docs/Glossary/Semantics).

1. Use React Testing Library: Use React Testing Library to write unit and integration tests for your components. This library provides a simple and intuitive API for testing React components and encourages developers to write tests that reflect the way users interact with the application. See [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) for more information.

1. Use the Atomic Design Methodology: The Atomic Design Methodology is a system for designing and building UI components in a structured and scalable way. By breaking down your UI into smaller, reusable components, you can create a more flexible and maintainable codebase. See Brad Frost article on [Atomic Design](https://atomicdesign.bradfrost.com/table-of-contents/) for more information.

1. Use React Query: React Query is a library for managing data fetching and caching in React applications. It provides a simple and intuitive API for fetching data from APIs, and supports caching, pagination, and other advanced features. See [ReactQuery](https://tanstack.com/query/v3/docs/react/overview) for more infomation.
_Note `onSuccess()/onError()/onSettled()` will be deprecated see [React Query v5](https://twitter.com/TkDodo/status/1647341498227097600)._

1. Read and understand the official React documentation: The React documentation at <https://react.dev/> is a valuable resource for learning about React and its ecosystem. Take the time to read and understand the documentation, and follow the best practices and recommendations provided by the React team. This will help you write better code and avoid common pitfalls in your React applications.

1. Use strict mode: Use the React strict mode to enable additional checks and warnings for potential problems in your code. This can help you catch potential issues early and improve the overall quality of your code.

1. Use ESLint and Prettier: Use ESLint and Prettier to enforce coding standards and formatting rules in your codebase. These tools can help you maintain consistency and improve the readability of your code.

1. Use CSS modules or styled-components: Use CSS modules or styled-components to manage the styling of your components. These tools provide a way to write scoped styles that are only applied to specific components and can help you avoid naming collisions and other styling issues.

1. Be careful of excessive prop drilling: Avoid excessive prop drilling by using React Query or React Context. These provide a centralized store for managing the state of your application and can help you avoid passing props down through multiple levels of components. Alternatively lifting the state up can help reduce prop drilling see Kent C Dodds article on [application state management with react](https://kentcdodds.com/blog/application-state-management-with-react). React.dev also has a great tutorial on [managing state](https://react.dev/learn/managing-state). _Note we haven't yet needed a global state but lightweight libraries like [zustand](https://github.com/pmndrs/zustand) or [jotai](https://github.com/pmndrs/jotai) could fit that need depending on the use case._

1. Use async/await for data fetching: Use async/await syntax to fetch data asynchronously from APIs or other sources. This can help you avoid callback hell and make your code easier to read and maintain.

1. Follow useState best practices: Removing redundant and duplicate data from the state helps ensure that all its pieces stay in sync, similar to how a database engineer normalizes the database structure to minimize bugs. See [choosing the state structure](https://react.dev/learn/choosing-the-state-structure) for more information.

1. Don't use unnecessary useEffect:  Removing unnecessary Effects will make your code easier to follow, faster to run, and less error-prone. See [you may not always need an effect](https://react.dev/learn/you-might-not-need-an-effect#) for more information. 

1. Don't use objects in your useEffect: Don't include objects in the dependency array, which can lead to unintended consequences. This is because objects are compared by reference, not by value. If the object reference changes, even if the object properties are the same, the effect will be triggered again. See [some reactive value change unintentionally](https://react.dev/learn/removing-effect-dependencies#does-some-reactive-value-change-unintentionally) for more information.

1. Reuse logic with custom hooks: Extract reusable logic into custom hooks to avoid code duplication and improve the reusability of your components. Custom hooks can be used to encapsulate logic related to data fetching, state management, and other common patterns. By using custom hooks, you can make your code more modular and easier to test and maintain. See [reusing logic with custom-hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) for more details.

1. Use TypeScript generics: Use TypeScript generics to create reusable components and functions that work with a variety of data types. Generics provide a way to write type-safe code that can be used in a flexible and scalable way.

1. Keep your components small and focused: Break your UI into smaller, reusable components that are focused on a single responsibility. This will make your code easier to test, maintain, and understand. As a rule of thumb, aim to keep each component under 100 lines of code.

1. Use type inference: Let TypeScript infer types whenever possible, rather than specifying types explicitly. This will make your code more concise and easier to read. For example, you can use the const keyword to infer the type of a variable, and the as const assertion to infer the type of an object literal.

1. Use the latest version of React and TypeScript: Always use the latest version of React and TypeScript to take advantage of the latest features and bug fixes.