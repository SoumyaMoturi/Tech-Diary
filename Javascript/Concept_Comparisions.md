

## Table of Contents

| Section          | Description                                        |
|------------------|----------------------------------------------------|
|1.| [Differences Between Object and Map in JavaScript](#differences-between-object-and-map-in-javascript)|
|2.|[Differences Between indexOf and findIndex in JavaScript](#differences-between-indexof-and-findindex-in-javaScript)|
|3.|[React.memo vs useMemo](#reactmemo-vs-usememo)|


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
