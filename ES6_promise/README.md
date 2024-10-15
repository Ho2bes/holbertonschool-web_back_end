# ES6 Promises Project

This repository contains the solutions for the **ES6_promise** project at Holberton School. The project focuses on understanding and using Promises in JavaScript, a key feature introduced in ES6 to handle asynchronous operations.

## 📝 Project Overview

**Promises** provide a more elegant way to manage asynchronous operations in JavaScript, replacing the callback-based approach. Promises allow handling asynchronous code with `.then()` and `.catch()` blocks, making code easier to read and maintain. This project explores the fundamentals of Promises and how to use them effectively in modern JavaScript.

### Key Concepts:
- **Promises**: Representing the eventual completion (or failure) of an asynchronous operation.
- **then()**: Handling the result of a successful Promise.
- **catch()**: Handling errors or rejected Promises.
- **async/await**: A syntactic sugar built on Promises for writing asynchronous code in a more synchronous manner.
- **Chaining**: Handling multiple asynchronous operations in sequence.

### Skills Gained:
- Creating and using Promises to manage asynchronous tasks.
- Using `.then()` and `.catch()` to handle successful and failed operations.
- Writing cleaner asynchronous code using `async` and `await`.
- Understanding how to chain Promises for sequential asynchronous tasks.

## 📂 Project Structure

- **0-promise.js**: A function that returns a Promise, which resolves or rejects based on input conditions.
- **1-get_full_promise.js**: A function that simulates an API call and resolves a Promise after a timeout.
- **2-handle_rejection.js**: A function that demonstrates how to catch and handle Promise rejections.
- **3-chaining.js**: A function that chains multiple Promises together to simulate sequential asynchronous operations.
- **4-wait.js**: A function that returns a Promise that resolves after a specified delay.
- **5-promisify.js**: A function that converts a callback-based function into a Promise-based function using `promisify`.
