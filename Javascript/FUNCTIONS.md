# First-Class Functions

## Overview

In JavaScript, functions are considered **first-class citizens**. This means functions in JavaScript can be treated as objects and can be passed around and manipulated just like any other value (e.g., numbers, strings).

## Key Characteristics

1. **Assignment**: Functions can be assigned to variables.
2. **Passing as Arguments**: Functions can be passed as arguments to other functions.
3. **Returning from Functions**: Functions can be returned from other functions.
4. **Storing in Data Structures**: Functions can be stored in data structures such as arrays or objects.

## Examples

### 1. Assignment

```javascript
// Function assigned to a variable
const greet = function(name) {
    return `Hello, ${name}!`;
};

console.log(greet('Alice')); // Output: Hello, Alice!
```

### 2.Passing as Arguments

```javascript
function callFunction(fn, value) {
    return fn(value);
}

const square = x => x * x;

console.log(callFunction(square, 5)); // Output: 25

```
### 3.Returning from Functions

```javascript
function makeMultiplier(factor) {
    return function(x) {
        return x * factor;
    };
}

const double = makeMultiplier(2);

console.log(double(4)); // Output: 8
```


### 4. Storing in Data Structures

```javascript
const operations = {
    add: (x, y) => x + y,
    subtract: (x, y) => x - y
};

console.log(operations.add(5, 3)); // Output: 8
console.log(operations.subtract(5, 3)); // Output: 2

```


## Conclusion

In JavaScript, the concept of first-class functions allows for greater flexibility and abstraction in your code. Functions can be treated just like any other value, enabling powerful programming techniques such as higher-order functions, functional composition, and dynamic behavior. Understanding and utilizing first-class functions can help you write cleaner, more modular, and maintainable code, making your JavaScript applications more robust and adaptable.





