# Python Async Comprehension Project

This repository contains an implementation of **asynchronous comprehensions** in Python. The project demonstrates how to use Python's `async` and `await` syntax in combination with comprehensions to handle asynchronous tasks efficiently.

## 📝 Project Overview

**Asynchronous comprehensions** in Python allow you to work with asynchronous iterators and generators while using list, set, and dictionary comprehensions. This project focuses on understanding the power of asynchronous operations, particularly how to collect data from asynchronous sources in a concise and readable way.

### Key Concepts:
- **async/await**: Python keywords used to define and handle asynchronous functions and operations.
- **Async comprehensions**: Using list, set, or dictionary comprehensions to collect data from asynchronous iterators or generators.
- **Event Loop**: Understanding how the Python event loop works to handle asynchronous tasks concurrently.
- **Asynchronous Generators**: Functions that yield values asynchronously, allowing you to iterate over them using `async for`.

### Skills Gained:
- Writing asynchronous functions and understanding the async/await pattern in Python.
- Using asynchronous comprehensions to collect data from asynchronous sources.
- Managing asynchronous generators and iterators in Python.
- Understanding how asynchronous code runs in the context of the Python event loop.

## 📂 Project Structure

- **0-async_generator.py**: Defines an asynchronous generator that yields random numbers after a delay.
- **1-async_comprehension.py**: Uses an asynchronous comprehension to collect values from the `async_generator`.
- **2-measure_runtime.py**: Measures the runtime of running an asynchronous comprehension multiple times concurrently.
