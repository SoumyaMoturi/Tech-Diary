

## Table of Contents

| Section          | Description                                        |
|------------------|----------------------------------------------------|
|[Javascript](#javascript)||
|1.|[ES5 Vs ES6](#es5-vs-es6)|
|2.| [Differences Between Object and Map in JavaScript](#differences-between-object-and-map-in-javascript)|
|3.|[Differences Between indexOf and findIndex in JavaScript](#differences-between-indexof-and-findindex-in-javaScript)|
|4.|[fetch vs axios](#fetch-vs-axios)|
|5.|[bind, call Vs apply](#bind-call-vs-apply)|
|6.|[defer, async, and normal <script> tags](#defer-async-and-normal-script-tags)|
|7.|[View State Vs Session State](#view-state-vs-session-state)|
|8.|[Throttling Vs Debouncing](#throttling-vs-debouncing)|
|[React](#react)||
|1.|[Props Vs State](#props-vs-state)|
|2.|[React.memo vs UseMemo](#reactmemo-vs-usememo)|
|3.|[UseCallback vs UseMemo](#usecallback-vs-usememo)|
|4.|[useState Vs useRef](#usestate-vs-useref)|
|[TypeScript](#typescript)||
|1.|[Unknown Vs Any Vs Void](#unknown-vs-any-vs-void)|
|[Node Js](#node-js)||
|1.|[ES Modules Vs CommonJS](#es-modules-vs-commonjs)|

# Javascript

# ES5 Vs ES6


| **Feature**            | **ES5**                      | **ES6**                                |
|-------------------------|------------------------------|----------------------------------------|
| **Variable Declarations** | `var`                    | `let`, `const`                        |
| **Functions**           | Regular functions           | Arrow functions                       |
| **Classes**             | Prototype-based inheritance | `class` syntax                        |
| **Strings**             | Concatenation               | Template literals                     |
| **Modules**             | `require`                  | `import`/`export`                     |
| **Promises**            | Callbacks                  | Promises                              |
| **Syntax Enhancements** | None                       | Destructuring, Spread, Rest, etc.     |


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
| **File uploads**           | Requires manual handling.                   | Easier to handle with `FormData` support.    |

# `bind`, `call` Vs `apply`

| Feature                | **`bind()`**                                                | **`call()`**                                                  | **`apply()`**                                                 |
|------------------------|-------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| **Purpose**             | Returns a new function with a specific `this` value and arguments. | Invokes the function immediately with a specified `this` value and arguments. | Invokes the function immediately with a specified `this` value and arguments (as an array). |
| **Return Value**        | A new function.                                            | The result of the function invocation.                       | The result of the function invocation.                       |
| **Invocation**          | Does not invoke the function immediately. It returns a new function. | Invokes the function immediately.                            | Invokes the function immediately.                            |
| **Arguments Handling**  | You can specify a fixed `this` value and optional arguments which are prepended to those passed during the invocation. | Pass arguments directly after the `this` value.              | Pass arguments as an array (or array-like object).           |
| **Use Case**             | Useful when you want to pass a function around with a specific `this` value, especially in event handlers and callbacks. | Useful for invoking a function with a specific `this` context and immediate execution. | Similar to `call()`, but arguments are passed as an array or array-like object. |
| **Example**             | `const greet = person.greet.bind(person, "Hello"); greet();` | `person.greet.call(person, "Hello");`                        | `person.greet.apply(person, ["Hello"]);`                     |
| **Modification of `this`** | `this` is permanently bound to the given value.             | `this` is set dynamically at the time of the function invocation. | `this` is set dynamically at the time of the function invocation. |

---

## **Key Differences:**

1. **`bind()`**:
   - Does not invoke the function immediately.
   - Returns a new function with the specified `this` value and optional arguments.
   - Can be useful when you want to preserve `this` for later use (e.g., in event handlers).

2. **`call()`**:
   - Invokes the function immediately.
   - Arguments are passed individually (not as an array).
   - Used when you want to invoke a function with a specific `this` context immediately.

3. **`apply()`**:
   - Invokes the function immediately.
   - Arguments are passed as an array (or array-like object).
   - Useful when you have arguments stored in an array or array-like object and want to invoke the function with those arguments.
   
### Explanation of Differences:

`bind()`
bind creates a new function, which can be called later. It is useful when you need to "bind" a function to a specific this context and optionally pass initial arguments to it.
Example:

```javascript
const person = {
  name: "Alice",
  greet: function(greeting) {
    console.log(greeting + " " + this.name);
  }
};
const greetPerson = person.greet.bind(person, "Hello");
greetPerson();  // Output: "Hello Alice"
```

`call()`:

call immediately invokes the function with a specified this context and individual arguments.
Example:

```javascript
const person = {
  name: "Alice",
  greet: function(greeting) {
    console.log(greeting + " " + this.name);
  }
};
person.greet.call(person, "Hello");  // Output: "Hello Alice"
```


`apply()`:

Similar to call(), but the arguments are passed as an array (or array-like object).
Example:
```javascript
Copy code
const person = {
  name: "Alice",
  greet: function(greeting, punctuation) {
    console.log(greeting + " " + this.name + punctuation);
  }
};
person.greet.apply(person, ["Hello", "!"]);  // Output: "Hello Alice!"
```

**When to Use Each:**
- bind(): When you need to pass a function around but with a fixed this context. Commonly used with event handlers or callbacks.
- call(): When you want to invoke a function immediately with a specific this context and arguments passed individually.
- apply(): When you want to invoke a function immediately with a specific this context and arguments passed as an array.

# `defer`, `async`, and normal `<script>` tags

| Feature                   | **Normal `<script>`**                                          | **`defer`**                                                    | **`async`**                                                   |
|---------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| **Execution Timing**       | Executes immediately as the script is encountered in the HTML. | Executes after the HTML document is fully parsed.             | Executes as soon as the script is downloaded, potentially before the HTML is fully parsed. |
| **Blocking Behavior**      | Blocks parsing of the HTML document until the script is executed. | Does not block HTML parsing; script execution is deferred until parsing completes. | Does not block HTML parsing, but can execute out of order with respect to other scripts. |
| **Script Execution Order** | Executes in the order it appears in the HTML document.        | Executes in the order it appears in the HTML document after parsing. | Executes as soon as the script is downloaded, potentially out of order with other scripts. |
| **Use Case**               | Suitable for inline scripts or scripts that need to be executed immediately. | Suitable for scripts that don't depend on DOM content or other scripts. | Suitable for scripts that don't depend on other scripts or the DOM (e.g., analytics scripts). |
| **Attributes**             | No special attributes (e.g., `<script src="file.js"></script>`). | `<script src="file.js" defer></script>`                       | `<script src="file.js" async></script>`                       |
| **HTML Parsing**           | HTML parsing is blocked until the script has executed.        | HTML parsing continues while the script is being downloaded, but execution is deferred. | HTML parsing continues while the script is being downloaded and executed as soon as it's ready. |
| **Dependence on Other Scripts** | Can cause issues if the script depends on others being executed before it. | Can rely on other deferred scripts since execution order is maintained. | Cannot depend on other scripts or execution order because it executes as soon as it’s ready. |
| **Example**                | `<script src="example.js"></script>`                          | `<script src="example.js" defer></script>`                    | `<script src="example.js" async></script>`                    |

![`defer`, `async`, and normal `<script>`](images/asyncVsDefer.png)


# View State Vs Session State

| Feature                       | **View State**                                              | **Session State**                                            |
|-------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Storage Location**           | Stored in the client-side browser (as hidden input or in memory). | Stored on the server-side (session store, cookies, or memory). |
| **Lifetime**                   | Data is preserved for the duration of a page load or postback. | Data persists for the duration of a user's session (usually until the session expires or the user logs out). |
| **Scope**                       | Page-specific. The data is tied to a single page and not shared across pages. | User-specific. The data is shared across multiple pages within the same user session. |
| **Data Security**              | Less secure because it is stored on the client-side and can be tampered with. | More secure since data is stored on the server-side, inaccessible to the client. |
| **Data Size Limit**            | Typically small, limited by hidden input field size (4 KB or less). | Can store larger amounts of data, depending on server memory or database storage. |
| **Performance**                | Affects page load time, as it has to be transmitted with every postback. | Performance is typically better, as data is stored on the server and not sent with every request. |
| **Persistence**                | Data is not persistent across different pages unless passed explicitly (e.g., via form submission). | Data persists across multiple page requests within the user session. |
| **Use Case**                   | Used for maintaining data that is specific to a single page (like user input or form state). | Used for data that needs to persist across different pages (like authentication status or shopping cart contents). |
| **Example**                    | Storing form data in a hidden input for postback.           | Storing user authentication status across multiple pages. |
| **Example in Code**            | `<input type="hidden" id="viewState" value="SomeStateData"/>` | `sessionStorage.setItem('username', 'JohnDoe');` in JavaScript. |




# Throttling Vs Debouncing

Throttling and debouncing are techniques used to limit how frequently a function is called during events like scrolling, resizing, or typing. While both concepts are used to optimize performance, they serve different purposes.

## Key Differences Between Throttling and Debouncing

| **Aspect**               | **Throttle**                                             | **Debounce**                                               |
|--------------------------|---------------------------------------------------------|-----------------------------------------------------------|
| **Definition**            | Throttling ensures a function is executed at most once in a specified time interval. | Debouncing ensures a function is executed only once after a specified delay, typically after the last event in a series. |
| **When the function is called** | The function is called at regular intervals, at most once every specified time period (e.g., 200ms). | The function is called after a certain period of inactivity, after the last event. |
| **Use Case**              | Used for continuous events like scrolling, resizing, or mouse movements, where you want to limit how often a function runs. | Used for events that are fired multiple times in a short period, like typing in an input field or button clicks, where you want to wait until the user stops. |
| **How it behaves**        | The function is called at a consistent rate, irrespective of how many times the event is triggered during the interval. | The function is delayed until the event stops being triggered for a specified time. |
| **Example Use Cases**     | - Handling `scroll` events<br>- Throttling `resize` events<br>- API polling at intervals | - User input for search bar<br>- Window resizing that only triggers the final size change<br>- Button click events (e.g., submit form) |
| **Function Calls**        | The function will be invoked repeatedly, but only once in the defined interval, no matter how many times the event occurs during that interval. | The function will only be called once, and only after a specified delay after the last event occurs. |
| **Rate of Execution**     | Controlled rate: function is invoked at most once in a fixed time period. | Delay based: function is invoked once after a pause in the event sequence. |
| **Example**               | Scrolling: Log scroll position once every 200ms, even if scrolling occurs more frequently. | Typing in an input: Trigger search after 300ms of inactivity (user stops typing). |
| **Behavior for Frequent Events** | Executes at consistent intervals during frequent events. | Waits for the event to stop and only executes once. |


## Example 

**Debounce** 

```javascript
function debounce(func, delay) {
  let timeout;
  
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
}

// Usage: Input field debouncing
document.getElementById('input').addEventListener('input', debounce(function(event) {
  console.log('User stopped typing: ', event.target.value);
}, 500));  // Calls the function only after 500ms of no typing


```

**Throttle**

```javascript
function throttle(func, delay) {
  let lastCall = 0;
  
  return function(...args) {
    const now = new Date().getTime();
    
    if (now - lastCall >= delay) {
      func(...args);
      lastCall = now;
    }
  };
}

// Usage: Scroll event throttling
window.addEventListener('scroll', throttle(function() {
  console.log('Scrolled!');
}, 1000));  // Only calls the function once every 1 second

```
**Key Points** : 

- **Throttling**: Executes the function at regular intervals (e.g., once every 1000ms), regardless of how often the event is triggered.
- **Debouncing**: Executes the function only after the event has stopped being triggered for a specified time (e.g., 500ms after the last keystroke).

# React

# `Props` Vs `State` 

| Feature               | **Props**                                                  | **State**                                                 |
|-----------------------|------------------------------------------------------------|-----------------------------------------------------------|
| **Purpose**            | Used to pass data from a parent component to a child.      | Used to store data that changes over time within a component. |
| **Mutability**         | Immutable (cannot be changed by the child component).      | Mutable (can be changed within the component).            |
| **Ownership**          | Owned by the parent component.                            | Owned by the component itself.                           |
| **Usage**              | Passed down to child components, typically set once.       | Managed within the component, can be updated with `setState`. |
| **Change Trigger**     | Cannot be changed by the receiving component.              | Can be changed by the component using `setState`.          |
| **Default Value**      | Passed from parent; must be set by the parent.             | Set within the component using `useState` or `this.setState`. |
| **Type of Data**       | Can be any type of data (objects, arrays, functions, etc.). | Usually primitive types or objects/arrays.                |
| **Re-rendering**       | Triggers re-rendering of the child component when changed. | Triggers re-rendering of the component when changed.      |
| **Example Usage**      | `<ChildComponent name="John" age={30} />`                 | `const [count, setCount] = useState(0);`                  |

---

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
## Example 

```jsx
import React, { useState, useMemo, useCallback } from 'react';

function FilteredList({ filter }: { filter: string }) {
  const list = ["apple", "banana", "cherry", "date", "elderberry"];

  const filteredList = useMemo(() => {
    console.log("Filtering list...");
    return list.filter((item) => item.includes(filter));
  }, [filter]);

  return (
    <ul>
      {filteredList.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}

function App() {
  const [filter, setFilter] = useState("");
  const [count, setCount] = useState(0);

  const handleFilterChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setFilter(e.target.value);
    },
    []
  );

  return (
    <div>
      <input
        type="text"
        placeholder="Filter"
        value={filter}
        onChange={handleFilterChange}
      />
      <FilteredList filter={filter} />
      <button onClick={() => setCount(count + 1)}>Increment Count: {count}</button>
    </div>
  );
}

export default App;

```
**key points :**
- useMemo optimizes the filtering operation.
- useCallback ensures the handleFilterChange function does not get recreated unnecessarily.


# `useState` Vs `useRef`

| Feature               | **`useState`**                                         | **`useRef`**                                               |
|-----------------------|--------------------------------------------------------|---------------------------------------|
| **Purpose**            | Used to hold and update state in a component.          | Used to persist values across renders without causing a re-render. |
| **Re-renders**         | Triggers a re-render when the state changes.           | Does **not** trigger a re-render when the value changes.   |
| **Mutability**         | The state is mutable and updated with `setState` (or the setter function from `useState`). | The ref object is mutable and can be changed directly.     |
| **Value Persistence**  | The value is lost when the component re-renders.       | The value persists across re-renders without loss.         |
| **Usage**              | Typically used for data that affects the UI and needs to trigger re-renders. | Typically used for DOM references, storing mutable data that doesn’t need to trigger re-renders. |
| **Data Type**          | Stores primitive values, arrays, or objects that need re-rendering. | Stores any type of mutable object or DOM element reference. |
| **Common Use Cases**   | Managing form inputs, counters, toggles, etc.           | Storing a reference to a DOM element or a persistent value across renders (e.g., for timeouts, interval IDs). |
| **Example Usage**      | `const [count, setCount] = useState(0);`               | `const inputRef = useRef(null);`                            |

---

## Example 

```tsx
import React, { useState, useEffect, useRef } from 'react';

function CountTracker() {
  // State to hold the current count value
  const [count, setCount] = useState(0);

  // Ref to store the previous count value (without causing re-render)
  const prevCountRef = useRef<number>(0);

  // Update the previous count when count changes
  useEffect(() => {
    prevCountRef.current = count;
  }, [count]);  // This effect runs every time `count` changes

  return (
    <div>
      <h2>Current Count: {count}</h2>
      <h3>Previous Count: {prevCountRef.current}</h3>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
    </div>
  );
}

export default CountTracker;
```

- useState causes the component to re-render when its value changes. It is used for data that impacts the rendering of the component.
- useRef does not cause re-renders when its value is changed. It’s used to store mutable values that don't need to trigger a re-render, like the previous count value or DOM references.

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


```tsx
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


# NodeJs

# ES Modules Vs CommonJS

| Feature                         | ES Modules (ESM)                     | CommonJS (CJS)                      |
|---------------------------------|--------------------------------------|-------------------------------------|
| **Syntax**                      | `import` and `export`                | `require` and `module.exports`     |
| **File Extension**              | `.mjs` (default) or `.js` with `"type": "module"` in `package.json` | `.js` (default)                     |
| **Imports**                     | Static (at the top of the file)      | Dynamic (can be conditional)        |
| **Exports**                     | Named and default exports            | Only `module.exports` or `exports` |
| **Top-level `this`**            | `undefined`                          | `exports` object                    |
| **Execution Timing**            | Executes in strict mode by default   | Executes in sloppy mode unless strict mode is explicitly enabled |
| **File Resolution**             | Follows URL resolution logic         | Follows `require` resolution logic |
| **Asynchronous Loading**        | Supports `import()` for dynamic imports | Fully synchronous                  |
| **Interoperability**            | Use `createRequire` to load CJS in ESM | Use `require` to load ESM (experimental) |
| **Caching**                     | Separate cache for ESM and CJS       | Shares a single cache for CJS       |
| **Tooling Support**             | Requires compatibility for older tools | Widely supported across tools      |


how **import statements in ES Modules (ESM)** are **installed (resolved)** and **executed** in Node.js.

## ESM Module Behavior

| **Aspect**            | **Behavior**                                                                                                                                                 |
|-----------------------|----------------------------------------------------|
| **Installation**       | - **Static Analysis**: ESM's `import` statements are resolved at compile-time before execution begins.                                                       |
|                       | - The module loader locates the dependencies using their exact file paths or the resolution algorithm for extensions (`.js`, `.mjs`, etc.).                   |
|                       | - Modules are fetched and cached for subsequent reuse.                                                                                                     |
| **Execution**          | - ESM imports are **asynchronous** and executed in the following order:                                                                                     |
|                       |   1. **Dependency Tree Evaluation**: All dependencies (imported modules) are recursively evaluated first.                                                    |
|                       |   2. **Top-Down Execution**: The module's own code runs after all its dependencies are resolved.                                                           |
|                       | - Execution follows **strict mode** by default.                                                                                                             |
| **Caching**            | - Modules are cached after the first import. Any subsequent import reuses the already loaded module without re-execution.                                    |
| **Dynamic Import**     | - Supports asynchronous `import()` to dynamically load modules at runtime. This returns a `Promise` and executes after all static imports are resolved.      |

## Key Points

- **Static Resolution**: Dependencies are resolved before execution, allowing for better optimization and performance.
- **Asynchronous Import**: Import statements are asynchronous, and modules are executed after their dependencies are resolved.
- **Strict Mode**: ESM modules always run in strict mode, enforcing stricter syntax and runtime checks.
- **Caching**: Once imported, modules are cached and reused in future imports.
- **Dynamic Import**: The `import()` syntax allows dynamic, on-demand loading of modules during runtime.

## CJS Module Behavior

| **Aspect**            | **Behavior**                                                                                                                                                 |
|-----------------------|--------------------------------------------|
| **Installation**       | - The `require` statement resolves the module path at runtime using Node.js's resolution algorithm.                                                          |
|                       | - Dependencies are located synchronously. Node.js checks extensions (`.js`, `.json`, `.node`) and resolves paths recursively.                               |
| **Execution**          | - Modules are loaded and executed synchronously in the order of their `require` calls.                                                                       |
|                       | - After resolving dependencies, the module's code runs immediately.                                                                                         |
|                       | - CJS modules do not run in strict mode by default.                                                                                                         |
| **Caching**            | - Modules are cached after the first `require`. Any subsequent `require` uses the cached module.                                                            |
|                       | - Circular dependencies are partially resolved by providing an incomplete module during execution.                                                          |
| **Dynamic Loading**    | - CJS does not support dynamic imports like `import()`. However, you can conditionally call `require` to load modules at runtime.                           |

## Key Points

- **Synchronous Execution**: Modules are executed synchronously when `require` is called, and dependencies are resolved at runtime.
- **Caching**: Modules are cached after being required once to improve performance.
- **No Dynamic Imports**: CommonJS does not support dynamic imports like `import()`, but you can conditionally use `require` to load modules dynamically.

