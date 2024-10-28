

**Table of Contents** 

|**Topic**| **Sub Topic**|
|:---|:--------|
|[Array Functions](#array-functions)||
| |[map()](#1-map)|
| |[filter()](#2-filter)|
| |[reduce()](#3-reduce)|
| |[forEach()](#4-foreach)|
| |[find()](#5-find)|
| |[findIndex()](#6-findindex)|
| |[some()](#7-some)|
| |[every()](#8-every)|
| |[includes()](#9-includes)|
| |[concat()](#10-concat)|
| |[slice()](#11-slice)|
| |[splice()](#12-splice)|
| |[sort()](#13-sort)|
| |[reverse()](#14-reverse)|

---



# Array Functions

## 1. `map()`
- **Syntax:** `array.map(callback(element[, index[, array]])[, thisArg])`
- **Description:** Creates a new array populated with the results of calling a provided function on every element in the array.

**Example:**
```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8]
```

## 2. `filter()`
- **Syntax:** `array.filter(callback(element[, index[, array]])[, thisArg])`
- **Description:** Creates a new array with all elements that pass the test implemented by the provided function.

**Example:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // Output: [2, 4]
```

## 3. `reduce()`
- **Syntax:** `array.reduce(callback(accumulator, element[, index[, array]])[, initialValue])`
- **Description:** Executes a reducer function on each element of the array, resulting in a single output value.

**Example:**
```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((acc, curr) => acc + curr, 0);
console.log(sum); // Output: 10
```

## 4. `forEach()`
- **Syntax:** `array.forEach(callback(element[, index[, array]])[, thisArg])`
- **Description:** Executes a provided function once for each array element.

**Example:**
```javascript
const colors = ['red', 'green', 'blue'];
colors.forEach(color => console.log(color));
// Output:
// red
// green
// blue
```

## 5. `find()`
- **Syntax:** `array.find(callback(element[, index[, array]])[, thisArg])`
- **Description:** Returns the first element in the array that satisfies the provided testing function. If no elements satisfy, it returns `undefined`.

**Example:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const firstEven = numbers.find(num => num % 2 === 0);
console.log(firstEven); // Output: 2
```

## 6. `findIndex()`
- **Syntax:** `array.findIndex(callback(element[, index[, array]])[, thisArg])`
- **Description:** Returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns `-1`.

**Example:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const index = numbers.findIndex(num => num > 3);
console.log(index); // Output: 3
```

## 7. `some()`
- **Syntax:** `array.some(callback(element[, index[, array]])[, thisArg])`
- **Description:** Checks if at least one element in the array passes the test implemented by the provided function. Returns `true` if found.

**Example:**
```javascript
const numbers = [1, 3, 5, 8];
const hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven); // Output: true
```

## 8. `every()`
- **Syntax:** `array.every(callback(element[, index[, array]])[, thisArg])`
- **Description:** Checks if all elements in the array pass the test implemented by the provided function. Returns `true` if all pass.

**Example:**
```javascript
const numbers = [2, 4, 6, 8];
const allEven = numbers.every(num => num % 2 === 0);
console.log(allEven); // Output: true
```

## 9. `includes()`
- **Syntax:** `array.includes(searchElement[, fromIndex])`
- **Description:** Determines whether an array includes a certain value among its entries. Returns `true` or `false`.

**Example:**
```javascript
const fruits = ['apple', 'banana', 'mango'];
console.log(fruits.includes('banana')); // Output: true
```

## 10. `concat()`
- **Syntax:** `array.concat(value1[, value2[, ...[, valueN]]])`
- **Description:** Merges two or more arrays. Does not change the existing arrays; returns a new array.

**Example:**
```javascript
const array1 = [1, 2];
const array2 = [3, 4];
const merged = array1.concat(array2);
console.log(merged); // Output: [1, 2, 3, 4]
```

## 11. `slice()`
- **Syntax:** `array.slice([begin[, end]])`
- **Description:** Returns a shallow copy of a portion of an array into a new array. Original array is not modified.

**Example:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const sliced = numbers.slice(1, 4);
console.log(sliced); // Output: [2, 3, 4]
```

## 12. `splice()`
- **Syntax:** `array.splice(start[, deleteCount[, item1[, item2[, ...]]]])`
- **Description:** Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.

**Example:**
```javascript
const numbers = [1, 2, 3, 4, 5];
numbers.splice(2, 1, 6);
console.log(numbers); // Output: [1, 2, 6, 4, 5]
```

## 13. `sort()`
- **Syntax:** `array.sort([compareFunction])`
- **Description:** Sorts the elements of an array in place and returns the sorted array. The default sort order is ascending.

**Example:**
```javascript
const numbers = [4, 2, 5, 1, 3];
numbers.sort((a, b) => a - b);
console.log(numbers); // Output: [1, 2, 3, 4, 5]
```

## Important Points:
- The `sort()` function changes the original array.
- The default sorting order is based on string Unicode code points.

## Sorting Numbers
By default, the `sort()` function converts numbers to strings and compares their sequences of UTF-16 code unit values, leading to incorrect results when sorting numbers:

```javascript
let numbers = [4, 2, 5, 1, 3];
numbers.sort();
console.log(numbers); // Output: [1, 2, 3, 4, 5]
```

## Sorting with a Compare Function
To sort numbers correctly, you need to pass a comparison function as an argument to `sort()`. The comparison function should return:
- A negative number if `a` should come before `b`.
- Zero if `a` and `b` are equal.
- A positive number if `a` should come after `b`.

### Example: Sorting Numbers in Ascending Order
```javascript
let numbers = [4, 2, 5, 1, 3];
numbers.sort(function(a, b) {
  return a - b;
});
console.log(numbers); // Output: [1, 2, 3, 4, 5]
```

### Example: Sorting Numbers in Descending Order
```javascript
let numbers = [4, 2, 5, 1, 3];
numbers.sort(function(a, b) {
  return b - a;
});
console.log(numbers); // Output: [5, 4, 3, 2, 1]
```

## Sorting Objects
When sorting an array of objects, you can use a comparison function to determine the order based on one or more object properties.

### Example: Sorting by Property
```javascript
let items = [
  { name: 'John', age: 30 },
  { name: 'Anna', age: 25 },
  { name: 'Mike', age: 28 }
];

items.sort(function(a, b) {
  return a.age - b.age;
});

console.log(items);
// Output: 
// [
//   { name: 'Anna', age: 25 },
//   { name: 'Mike', age: 28 },
//   { name: 'John', age: 30 }
// ]
```

## Custom Sort Order
You can customize the sort order based on your requirements by modifying the comparison function.

### Example: Sorting Strings by Length
```javascript
let words = ["banana", "apple", "cherry", "date"];
words.sort(function(a, b) {
  return a.length - b.length;
});
console.log(words); // Output: ["date", "apple", "banana", "cherry"]
```

## Conclusion
The `sort()` function is a powerful tool for ordering the elements of an array in JavaScript. While it sorts strings effectively by default, it requires a custom comparison function to sort numbers or objects based on specific criteria.


## 14. `reverse()`
- **Syntax:** `array.reverse()`
- **Description:** Reverses an array in place. The first array element becomes the last, and the last becomes the first.

**Example:**
```javascript
const numbers = [1, 2, 3, 4, 5];
numbers.reverse();
console.log(numbers); // Output: [5, 4, 3, 2, 1]
```


 
