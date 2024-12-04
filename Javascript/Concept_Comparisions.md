

## Table of Contents

| Section          | Description                                        |
|------------------|----------------------------------------------------|
|[Javascript](#javascript)||
|1.| [Differences Between Object and Map in JavaScript](#differences-between-object-and-map-in-javascript)|
|2.|[Differences Between indexOf and findIndex in JavaScript](#differences-between-indexof-and-findindex-in-javaScript)|
|3.|[fetch vs axios](#fetch-vs-axios)|
|[React](#react)||
|1.|[React.memo vs UseMemo](#reactmemo-vs-usememo)|
|2.|[UseCallback vs UseMemo](#usecallback-vs-usememo)|
|[TypeScript](#typescript)||
|1.|[Unknown Vs Any Vs Void](#unknown-vs-any-vs-void)|

# Javascript

# Differences Between Object and Map in JavaScript

| Feature                    | Object                             | Map                                |
|----------------------------|------------------------------------|------------------------------------|
| **Type**                    | Part of JavaScript's core language | An instance of the `Map` class     |
| **Key Types**               | Keys must be strings or symbols    | Keys can be of any data type       |
| **Order of Keys**           | No guaranteed order for iteration  | Keys are iterated in insertion order |
| **Size**                    | No direct method for size          | `map.size` returns the number of key-value pairs |
| **Performance**             | Fast for small collections         | Optimized for larger collections and frequent additions/removals |
| **Prototypes**              | Inherits from `Object.prototype`, may cause key collisions | No prototype, so no risk of collisions with default properties |
| **Iteration**               | Manual (`for...in`, `Object.keys()`) | Easy (`map.forEach()`, `for...of`) |
| **Methods for Management**  | No built-in methods for key-value management | Methods like `set()`, `get()`, `has()`, and `delete()` |

### Use Cases

- **Object**: Best for storing simple key-value pairs where keys are known in advance (e.g., configuration objects).
- **Map**: Ideal for dynamic data collections where key types vary, and order matters.
  

# Differences Between indexOf and findIndex in JavaScript


| Feature             | `indexOf`                                    | `findIndex`                                |
|---------------------|-----------------------------------------------------|--------------------------------------------------|
| **Input**           | A value (e.g., number, string)                      | A callback function (condition)                  |
| **Comparison**      | Strict equality (`===`)                             | Custom logic using a callback                    |
| **Return Value**    | Index of the value or `-1`                          | Index of the first match or `-1`                 |
| **Use Case**        | Simple value search                                 | Conditional or complex searches                  |
| **Supports Objects**| No                                                  | Yes                                              |
| **Example**         | `const arr = [10, 20, 30];`                         | `const arr = [10, 20, 30];`                      |
|                     | `arr.indexOf(20); // Output: 1`                     | `arr.findIndex(num => num > 25); // Output: 2`   |
|                     | `arr.indexOf(40); // Output: -1`                    | `arr.findIndex(num => num > 40); // Output: -1`  |

### Use Cases : 
- Use **indexOf** when searching for a specific value in an array.
- Use **findIndex** when searching based on a condition or when working with objects or complex criteria.


# fetch vs axios

| **Feature**               | **fetch**                                   | **axios**                                       |
|---------------------------|---------------------------------------------|------------------------------------------------|
| **Built-in**               | Yes (native JavaScript)                     | No (requires installation)                     |
| **Promise-based**          | Yes                                         | Yes                                            |
| **Error handling**         | Doesn't reject on HTTP error status codes. You need to check `response.ok` or `response.status`. | Rejects on HTTP error statuses (e.g., 404, 500). |
| **Automatic JSON Parsing** | No, you need to manually call `.json()`     | Yes, `response.data` contains parsed JSON data. |
| **Request cancellation**   | No, you need to use `AbortController`       | Yes, using `axios.CancelToken`.                 |
| **Timeout support**        | No, manual handling required.               | Yes, built-in support via `timeout` config.     |
| **Browser compatibility**  | Supported by most modern browsers.          | Works in most browsers, including IE, with polyfills. |
| **Response transformation**| No, manual handling needed.                 | Yes, supports transforming requests and responses. |
| **File uploads**           | Requires manual handling.                   | Easier to handle with `FormData` support.      |

# React


# React.memo vs useMemo

| **Feature**    | **React.memo**                          | **useMemo**                                     |
|-----------------|-----------------------------------------|------------------------------------------------|
| **Type**        | Higher-order component (HOC)           | React hook                                     |
| **Purpose**     | Optimizes components by skipping re-renders. | Optimizes values by memoizing the result of a computation. |
| **Scope**       | Works at the component level.          | Works at the value or computation level.       |
| **Usage**       | Wraps functional components to memoize their output. | Used inside functional components for memoizing calculations or values. |
| **Comparison**  | Compares props (shallow comparison by default). | Tracks dependencies to decide if the computation should re-run. |

## Explanation

**React.memo**
- A higher-order component (HOC) that wraps functional components.
- Avoids unnecessary re-renders by performing a shallow comparison of the component's props.
- Useful for optimizing performance in components that re-render frequently without changes to props.

**useMemo**
- A React hook designed to memoize the result of a computation.
- Prevents expensive calculations from re-running on every render by tracking dependency changes.
- Often used within components to optimize performance by caching computed values.

## Example Usage

**React.memo**
```jsx
const MyComponent = React.memo(({ name }) => {
    console.log('Rendered!');
    return <div>Hello, {name}!</div>;
});
```
**UseMemo**

```jsx
const MyComponent = ({ num }) => {
    const squared = useMemo(() => num * num, [num]);
    return <div>Squared Value: {squared}</div>;
};
```

# UseCallback Vs UseMemo

| Feature             | `useMemo`                                                                 | `useCallback`                                                            |
|---------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Purpose**          | Caches the result of a computation to avoid unnecessary recalculations.  | Caches a function reference to avoid unnecessary re-creations.           |
| **Return Value**     | Returns a **memoized value**.                                             | Returns a **memoized callback function**.                                |
| **When to Use**      | When you have an expensive computation and want to avoid re-computing it on every render. | When you pass a callback as a prop to child components or need stable references for dependencies. |
| **Dependency Array** | Triggers recomputation of the value when dependencies change.            | Triggers re-creation of the function when dependencies change.           |
| **Use Case Example** | Optimizing derived data, calculations, or component rendering.           | Preventing child component re-renders or maintaining event handler references. |
| **Syntax**           | `const memoizedValue = useMemo(() => compute(), [dependencies]);`        | `const memoizedCallback = useCallback(() => { callback }, [dependencies]);` |

---

# Typescript


# Unknown Vs Any Vs Void

## **Comparison Table**

| Feature           | `unknown`                          | `void`                           | `any`                            |
|--------------------|-------------------------------------|-----------------------------------|---------------------------|
| **Purpose**        | Type-safe placeholder for unknown types. | Represents no value (e.g., for functions with no return). | Dynamic type that disables type safety. |
| **Type Checking**  | Required before usage.             | Not applicable (used for no value). | No type-checking enforced.        |
| **Flexibility**    | Limited without type-checking.     | Not flexible (strict purpose).   | Highly flexible but unsafe.       |
| **Common Use Cases** | APIs returning unknown values.    | Functions with no return values. | Prototyping or gradual migration to TypeScript. |
| **Example Usage**  | `let x: unknown;`                  | `function x(): void {}`          | `let x: any;`                     |

---


```typescript
let vAny: any = "Hello, world!";
let vUnknown: unknown = "Hello, TypeScript!";

// Any can be assigned directly to any other type
let str1: string = vAny; // This works fine
console.log(str1); // Output: Hello, world!

// Unknown requires a type assertion before assignment
// let str2: string = vUnknown; // Error: Type 'unknown' is not assignable to type 'string'
let str2: string = vUnknown as string; // Correct: Using type assertion
console.log(str2); // Output: Hello, TypeScript!

// Any allows any property or method, even if it doesn't exist
vAny.nonExistentMethod(); // No error, but this will fail at runtime if the method doesn't exist

// Unknown doesn't allow any method or property access without a type check
// vUnknown.nonExistentMethod(); // Error: Object is of type 'unknown'
if (typeof vUnknown === "string") {
    console.log(vUnknown.toUpperCase()); // This is safe after a type check
}

```

