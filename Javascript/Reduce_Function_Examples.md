# `Array.prototype.reduce` — Interview Questions & Coding Problems

`reduce` comes up constantly in interviews because it's the most general-purpose array method — almost every other array method (`map`, `filter`, `find`, `flat`) can be implemented using it, and it tests whether you can think in terms of accumulation rather than imperative loops.

**Signature:** `arr.reduce((accumulator, currentValue, currentIndex, array) => {...}, initialValue)`

---

## PART A: Conceptual Questions

### A1. What does `reduce` actually do, and how is it different from `forEach`/`map`?

**Answer:** `reduce` executes a "reducer" callback on each element, carrying forward an **accumulator** value from one iteration to the next, and returns a **single final value** at the end (which could be a number, object, array, string — anything).

- `forEach` — iterates for side effects only, returns `undefined`.
- `map` — transforms each element 1:1, returns a new array of the same length.
- `reduce` — collapses the whole array into one accumulated result; can produce a value of any shape, including a completely different structure than the input array (an object, a single number, even a new array of different length).

**Key insight to state in an interview:** `reduce` is the most fundamental of the three — `map` and `filter` can both be implemented on top of `reduce` (shown below), but not vice versa easily. This is why interviewers like asking you to build other methods using `reduce` — it tests whether you understand accumulation as a general pattern.

---

### A2. What happens if you don't pass an `initialValue`?

**Answer:** If no `initialValue` is given, `reduce` uses the **first element of the array as the initial accumulator** and starts iterating from **index 1** instead of index 0.

```js
[1, 2, 3].reduce((acc, cur) => acc + cur);
// acc starts as 1 (arr[0]), iteration begins at index 1
// step: acc=1, cur=2 → 3; then acc=3, cur=3 → 6
// result: 6
```

**Important edge case:** calling `reduce` with **no initial value on an empty array** throws a `TypeError`:
```js
[].reduce((acc, cur) => acc + cur);
// TypeError: Reduce of empty array with no initial value
```
**Best practice to mention:** always pass an explicit `initialValue` unless you specifically want first-element-as-seed behavior — it avoids this crash and makes the accumulator's starting type explicit and predictable (e.g., always start object-building reduces with `{}`, sum reduces with `0`).

---

### A3. Is `reduce` always the right choice? When would you avoid it?

**Answer:** `reduce` is powerful but can hurt readability when overused — a `reduce` doing multiple unrelated things in one callback is harder to follow than a simple `for` loop or a chain of `map`/`filter`. Rule of thumb to state: use `reduce` when you're genuinely **accumulating into a single value** (sum, grouped object, merged result); prefer `map`/`filter`/`find` when a purpose-built method exists and reads more clearly for that specific transformation. Interviewers like hearing this — it shows judgment, not just "I know reduce so I use it everywhere."

---

## PART B: Coding Problems Using `reduce`

### B1. Sum an array
```js
const sum = [1, 2, 3, 4].reduce((acc, n) => acc + n, 0); // 10
```

### B2. Count occurrences of each value
```js
function countOccurrences(arr) {
  return arr.reduce((acc, item) => {
    acc[item] = (acc[item] || 0) + 1;
    return acc;
  }, {});
}
countOccurrences(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']);
// { apple: 3, banana: 2, orange: 1 }
```

### B3. Group an array of objects by a key (very common — "group orders by status")
```js
function groupBy(arr, key) {
  return arr.reduce((acc, item) => {
    const groupKey = item[key];
    if (!acc[groupKey]) acc[groupKey] = [];
    acc[groupKey].push(item);
    return acc;
  }, {});
}

const orders = [
  { id: 1, status: 'paid' },
  { id: 2, status: 'pending' },
  { id: 3, status: 'paid' },
  { id: 4, status: 'cancelled' },
];
groupBy(orders, 'status');
// { paid: [{id:1,...}, {id:3,...}], pending: [{id:2,...}], cancelled: [{id:4,...}] }
```
**Commerce framing:** this exact pattern is how you'd build an order dashboard grouped by status, or group cart items by category for display.

### B4. Flatten a nested array using `reduce`
```js
function flatten(arr) {
  return arr.reduce(
    (acc, val) => acc.concat(Array.isArray(val) ? flatten(val) : val),
    []
  );
}
flatten([1, [2, 3, [4, 5]], 6]); // [1, 2, 3, 4, 5, 6]
```

### B5. Implement `map` using `reduce`
```js
function mapWithReduce(arr, callback) {
  return arr.reduce((acc, cur, i, array) => {
    acc.push(callback(cur, i, array));
    return acc;
  }, []);
}
mapWithReduce([1, 2, 3], (x) => x * 2); // [2, 4, 6]
```

### B6. Implement `filter` using `reduce`
```js
function filterWithReduce(arr, predicate) {
  return arr.reduce((acc, cur, i, array) => {
    if (predicate(cur, i, array)) acc.push(cur);
    return acc;
  }, []);
}
filterWithReduce([1, 2, 3, 4, 5], (n) => n % 2 === 0); // [2, 4]
```
**Common follow-up:** "Now implement `find` using `reduce`." — a good chance to show you know `find` should **short-circuit** (stop on first match), which naive `reduce` doesn't do by default. You'd need to track a "found" flag and skip further work once set, or note that `reduce` isn't actually the ideal tool here since it always visits every element — a good example of the "when to avoid reduce" point from A3.

### B7. Find the maximum value in an array
```js
const max = [3, 7, 2, 9, 4].reduce((acc, cur) => (cur > acc ? cur : acc));
// 9 — using the "no initialValue" form here since we want the first element as the starting max
```

### B8. Calculate cart total (realistic commerce example)
```js
const cart = [
  { name: 'Shirt', price: 25, quantity: 2 },
  { name: 'Jeans', price: 60, quantity: 1 },
  { name: 'Socks', price: 8, quantity: 3 },
];

const total = cart.reduce((acc, item) => acc + item.price * item.quantity, 0);
// 25*2 + 60*1 + 8*3 = 134
```
**Follow-up they might add:** "Now apply a 10% discount and round to 2 decimals."
```js
const totalWithDiscount = Math.round(
  cart.reduce((acc, item) => acc + item.price * item.quantity, 0) * 0.9 * 100
) / 100;
// 120.6
```

### B9. Remove duplicates using `reduce`
```js
function uniqueWithReduce(arr) {
  return arr.reduce((acc, cur) => (acc.includes(cur) ? acc : [...acc, cur]), []);
}
uniqueWithReduce([1, 2, 2, 3, 1, 4]); // [1, 2, 3, 4]
```
**Complexity callout to mention:** this is O(n²) because `.includes()` scans the accumulator array each time. A better version for large arrays uses a `Set` alongside the accumulator for O(1) lookups:
```js
function uniqueWithReduceOptimized(arr) {
  const seen = new Set();
  return arr.reduce((acc, cur) => {
    if (!seen.has(cur)) {
      seen.add(cur);
      acc.push(cur);
    }
    return acc;
  }, []);
}
```

### B10. Chain multiple functions together (compose/pipe) using `reduce`
```js
const pipe = (...fns) => (initialValue) => fns.reduce((acc, fn) => fn(acc), initialValue);

const addTax = (price) => price * 1.08;
const applyDiscount = (price) => price * 0.9;
const round = (price) => Math.round(price * 100) / 100;

const finalPrice = pipe(applyDiscount, addTax, round)(100); // 97.2
```

### B11. Convert an array of key-value pairs into an object
```js
function arrayToObject(pairs) {
  return pairs.reduce((acc, [key, value]) => {
    acc[key] = value;
    return acc;
  }, {});
}
arrayToObject([['name', 'Alex'], ['age', 30]]); // { name: 'Alex', age: 30 }
// (Object.fromEntries does this natively — good to mention as the built-in alternative)
```

### B12. Deeply merge/aggregate — total sales by category (nested aggregation, a step up in difficulty)
```js
const sales = [
  { category: 'Electronics', amount: 200 },
  { category: 'Clothing', amount: 50 },
  { category: 'Electronics', amount: 150 },
  { category: 'Clothing', amount: 75 },
];

const totalsByCategory = sales.reduce((acc, sale) => {
  acc[sale.category] = (acc[sale.category] || 0) + sale.amount;
  return acc;
}, {});
// { Electronics: 350, Clothing: 125 }
```

### B13. Implement `reduce` itself (build the polyfill — a strong senior-level question)
```js
Array.prototype.myReduce = function (callback, initialValue) {
  let acc = initialValue;
  let startIndex = 0;

  if (acc === undefined) {
    if (this.length === 0) {
      throw new TypeError('Reduce of empty array with no initial value');
    }
    acc = this[0];
    startIndex = 1;
  }

  for (let i = startIndex; i < this.length; i++) {
    if (i in this) { // skip holes in sparse arrays, matching native spec behavior
      acc = callback(acc, this[i], i, this);
    }
  }
  return acc;
};

[1, 2, 3, 4].myReduce((acc, n) => acc + n, 0); // 10
```
