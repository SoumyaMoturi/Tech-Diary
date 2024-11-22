

## Table of Contents

| Section          | Description                                        |
|------------------|----------------------------------------------------|
|1.| [Differences Between Object and Map in JavaScript](#differences-between-object-and-map-in-javascript)|
|2.|[Differences Between indexOf and findIndex in JavaScript](#differences-between-indexof-and-findindex-in-javaScript)|


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

