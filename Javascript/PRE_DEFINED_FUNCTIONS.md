## Table of Contents
- [sort() ](#`sort()`-functions)

# `sort()` Function

The `sort()` function in JavaScript is used to sort the elements of an array in place and returns the sorted array. By default, the `sort()` function sorts the values as strings in ascending order.

## Basic Usage

```javascript
let fruits = ["banana", "apple", "cherry"];
fruits.sort();
console.log(fruits); // Output: ["apple", "banana", "cherry"]

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
