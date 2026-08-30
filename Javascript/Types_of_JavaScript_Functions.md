
# Table of Contents
---
||**Topic**|
|:--|:--|
||[Function Declarations](#function-declarations)|
||[Function Expressions](#function-expressions)|
||[Arrow Functions](#arrow-functions)|
||[Anonymous Functions](#anonymous-functions)|
||[Named Functions](#named-functions)|
||[Immediately Invoked Function Expressions (IIFE)](#immediately-invoked-function-expressions-iife)|
||[Generator Functions](#generator-functions)|
||[Async Functions](#async-functions)|
||[Pure Functions](#pure-functions)|
||[First-Class Functions](#first-class-functions)|
||[Callback Functions](#callback-functions)|
---


# JavaScript Functions

JavaScript functions are essential for structuring code and can be defined in various ways. 
Below is an overview of different types of functions in JavaScript:

## Function Declarations

Function declarations are hoisted, which means you can call them before their definition in the code.

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```

## Function Expressions
Function expressions are not hoisted. The function is available only after the assignment.

```javascript
const greet = function(name) {
  return `Hello, ${name}!`;
};

```
## Arrow Functions
Arrow functions provide a shorter syntax and do not have their own this context, which is useful for short, single-expression functions.

```javascript
const greet = (name) => `Hello, ${name}!`;
```

## Anonymous Functions

Anonymous functions are functions without names and are often used as arguments to other functions.

```javascript

setTimeout(function() {
  console.log('Executed after 1 second');
}, 1000);

```

## Named functions

Named function expressions have a name, which can be helpful for debugging.

```javascript

const greet = function greet(name) {
  return `Hello, ${name}!`;
};

```


**Named functions** in JavaScript are functions that have a specific name given at the time of their definition. This name can be used to call the function or to refer to the function within its own scope, which is useful for recursion and debugging.

### Example of a Named Function  

Here’s a simple example of a named function:

```javascript
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // Output: 5

```

### Named Function Expressions 

In addition to standard named functions, you can also create named function expressions. This means that even though the function is assigned to a variable, it retains its own name for internal use.

``` javascript
const factorial = function fact(n) {
  if (n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
};

console.log(factorial(5)); // Output: 120
```

In this example:  
fact is the name of the function, which is useful for recursive calls within the function.  
factorial is the variable to which the function is assigned. You can call the function using the variable name.  

### Benefits of Named Functions

**Debugging**: Named functions provide more descriptive stack traces in debugging tools, making it easier to identify where an error occurred.  
**Recursion**: Named function expressions allow the function to call itself, which is essential for recursive operations.  
**Readability**: Named functions improve code readability by clearly indicating the purpose of the function.  

### Comparison with Anonymous Functions
Unlike anonymous functions, named functions have a specific name that can be used to refer to them within their own scope or for better error handling.  

**Anonymous Function:**

```javascript
const greet = function(name) {
  return `Hello, ${name}!`;
};
```

**Named Function:**

```javascript
const greet = function greetUser(name) {
  return `Hello, ${name}!`;
};
```

In this comparison:
The anonymous function doesn’t have a name, which can make debugging more difficult.  
The named function (greetUser) can be used to identify the function in error messages and stack traces.    

### Summary
Named functions are an essential tool in JavaScript that offer benefits in terms of readability, debugging, and recursion. Use named functions to create clear and maintainable code, especially in situations where the function’s behavior is complex or prone to errors.  





## Immediately Invoked Function Expressions (IIFE)

IIFEs are functions that are executed immediately after their definition. They are often used to create a new scope.

```javascript

(function() {
  console.log('I am an IIFE');
})();

```

## Generator functions

Generator functions use the function* syntax and can yield multiple values over time using the yield keyword.

```javascript

function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

```

## Async functions

Async functions simplify working with promises and use await to pause execution until a promise resolves.

```javascript
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}
```

## Pure Functions 


A **pure function** is a function that, given the same input, will always return the same output and has **no side effects**. This means:
1. **Deterministic**: The function returns the same result every time it is called with the same arguments.
2. **No Side Effects**: The function does not alter any external state or rely on external state that may change.

### Characteristics of Pure Functions

- **Consistency**: A pure function will always yield the same output for identical inputs.
- **No External Dependency**: It does not rely on or modify any external state or variables.
- **Predictable and Testable**: Because they’re consistent, pure functions are easy to test and reason about.

### Example of a Pure Function

Below is an example of a pure function in JavaScript:

```javascript
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // Output: 5
console.log(add(2, 3)); // Output: 5, always returns the same result with same inputs
```

###  Example of Impure Function 

```javascript
let count = 0;

function increment() {
  count += 1;
  return count;
}

console.log(increment()); // Output: 1
console.log(increment()); // Output: 2, different result each time


```

## First-Class Functions

### Overview

In JavaScript, functions are considered **first-class citizens**. This means functions in JavaScript can be treated as objects and can be passed around and manipulated just like any other value (e.g., numbers, strings).

### Key Characteristics

1. **Assignment**: Functions can be assigned to variables.
2. **Passing as Arguments**: Functions can be passed as arguments to other functions.
3. **Returning from Functions**: Functions can be returned from other functions.
4. **Storing in Data Structures**: Functions can be stored in data structures such as arrays or objects.

### Examples

**1. Assignment**

```javascript
// Function assigned to a variable
const greet = function(name) {
    return `Hello, ${name}!`;
};

console.log(greet('Alice')); // Output: Hello, Alice!
```

**2.Passing as Arguments**

```javascript
function callFunction(fn, value) {
    return fn(value);
}

const square = x => x * x;

console.log(callFunction(square, 5)); // Output: 25

```
**3.Returning from Functions**

```javascript
function makeMultiplier(factor) {
    return function(x) {
        return x * factor;
    };
}

const double = makeMultiplier(2);

console.log(double(4)); // Output: 8
```

**4. Storing in Data Structures**

```javascript
const operations = {
    add: (x, y) => x + y,
    subtract: (x, y) => x - y
};

console.log(operations.add(5, 3)); // Output: 8
console.log(operations.subtract(5, 3)); // Output: 2

```


### Conclusion

In JavaScript, the concept of first-class functions allows for greater flexibility and abstraction in your code. Functions can be treated just like any other value, enabling powerful programming techniques such as higher-order functions, functional composition, and dynamic behavior. Understanding and utilizing first-class functions can help you write cleaner, more modular, and maintainable code, making your JavaScript applications more robust and adaptable.


## Callback Functions

A **callback function** is a function that is passed as an argument to another function and is executed after some operation has been completed. Callbacks are commonly used for asynchronous operations such as API requests, reading files, or handling events.

### Example of a Simple Callback

Here’s a basic example where a callback function is used:

```javascript
function greet(name, callback) {
  console.log(`Hello, ${name}!`);
  callback();
}

function sayGoodbye() {
  console.log('Goodbye!');
}

greet('Alice', sayGoodbye);

```

In this example:
greet is a function that accepts a name and a callback function as arguments.  
After greeting the user, it calls the sayGoodbye function passed as a callback.  

### Asynchronous Callbacks 
Callbacks are particularly useful in asynchronous code. For example, when working with timeouts or API requests:

```javascript
function fetchData(callback) {
  setTimeout(() => {
    const data = { id: 1, name: 'Sample Data' };
    callback(data);
  }, 1000);
}

function processData(data) {
  console.log('Processing data:', data);
}

fetchData(processData);
```

In this example:  

fetchData simulates an asynchronous operation using setTimeout.  
Once the data is "fetched," it calls processData with the fetched data as an argument.  

### Error-First Callbacks  

When dealing with asynchronous operations that might fail, it’s common to use error-first callbacks. This pattern ensures that errors are handled before proceeding with the normal flow.

```javascript

function fetchData(callback) {
  setTimeout(() => {
    const error = null; // Or some error if it occurs
    const data = { id: 1, name: 'Sample Data' };

    callback(error, data);
  }, 1000);
}

function handleData(error, data) {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  console.log('Data received:', data);
}

fetchData(handleData);

```
In this example:  

The fetchData function simulates fetching data and calls the callback with an error (if any) as the first argument and the data as the second.  
The handleData function checks for an error and processes the data if no error occurs.  

### Summary
Callback functions are a powerful feature in JavaScript, especially for handling asynchronous tasks. They allow you to ensure that code is executed only after certain tasks have been completed.





