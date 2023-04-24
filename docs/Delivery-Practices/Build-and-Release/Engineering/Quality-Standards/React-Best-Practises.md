---
title: React Best Practises 
authors: 
- Rhodri Hewitson
---

## Introduction

React is a popular open-source JavaScript library used for building user interfaces. It was created by Facebook and has gained a lot of popularity among developers for its declarative and efficient approach to building web applications. TypeScript is a superset of JavaScript that adds optional static typing and other features to the language. By using TypeScript with React, developers can write more reliable, maintainable, and scalable code with fewer errors. In this context, it's important to follow best practices and guidelines to ensure that your code is of the highest quality. In this post, we've provided some guidelines and best practices for writing React code in TypeScript that can help you write better code and improve the overall quality of your application.

## Guidelines for Writing React Code in TypeScript

1. Use semantic HTML: Use semantic HTML tags that describe the content of the page rather than just the appearance. This will help with accessibility and search engine optimization, and make your code easier to read and maintain.

1. Use React Testing Library: Use React Testing Library to write unit and integration tests for your components. This library provides a simple and intuitive API for testing React components and encourages developers to write tests that reflect the way users interact with the application.

1. Use the Atomic Design Methodology: The Atomic Design Methodology is a system for designing and building UI components in a structured and scalable way. By breaking down your UI into smaller, reusable components, you can create a more flexible and maintainable codebase.

1. Use React Query: React Query is a library for managing data fetching and caching in React applications. It provides a simple and intuitive API for fetching data from APIs, and supports caching, pagination, and other advanced features.

1. Use strict mode: Use the React strict mode to enable additional checks and warnings for potential problems in your code. This can help you catch potential issues early and improve the overall quality of your code.

1. Use ESLint and Prettier: Use ESLint and Prettier to enforce coding standards and formatting rules in your codebase. These tools can help you maintain consistency and improve the readability of your code.

1. Use CSS modules or styled-components: Use CSS modules or styled-components to manage the styling of your components. These tools provide a way to write scoped styles that are only applied to specific components and can help you avoid naming collisions and other styling issues.

1. Use prop drilling sparingly: Avoid excessive prop drilling by using React Query or React Context. These provide a centralized store for managing the state of your application and can help you avoid passing props down through multiple levels of components.

1. Use async/await for data fetching: Use async/await syntax to fetch data asynchronously from APIs or other sources. This can help you avoid callback hell and make your code easier to read and maintain.

1. Use hooks effectively: Use React hooks like useState and useEffect to manage state and side effects in your components. Hooks provide a simple and intuitive API for managing state and can help you avoid class components and the complexities that come with them.

1. Use TypeScript generics: Use TypeScript generics to create reusable components and functions that work with a variety of data types. Generics provide a way to write type-safe code that can be used in a flexible and scalable way.

1. Keep your components small and focused: Break your UI into smaller, reusable components that are focused on a single responsibility. This will make your code easier to test, maintain, and understand. As a rule of thumb, aim to keep each component under 100 lines of code.

1. Use type inference: Let TypeScript infer types whenever possible, rather than specifying types explicitly. This will make your code more concise and easier to read. For example, you can use the const keyword to infer the type of a variable, and the as const assertion to infer the type of an object literal.

1. Use the latest version of React and TypeScript: Always use the latest version of React and TypeScript to take advantage of the latest features and bug fixes.