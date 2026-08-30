# JavaScript Coding Interview Questions — Detailed Answers

This set focuses on **pure JavaScript language behavior**: output-prediction ("what does this print?") questions, polyfills of built-in methods, and array/object manipulation problems. These are extremely common in Node/full-stack interviews because they test whether you understand JS deeply, not just whether you can memorize algorithms. (See the earlier coding file for classic DSA problems and Node-specific practical implementations like LRU cache/debounce/event emitter — this file is intentionally different content.)

---

## PART A: Output-Prediction / "What Does This Print?" Questions

These test your understanding of closures, hoisting, `this`, coercion, and the event loop. Interviewers love these because they're quick to ask and reveal a lot.

### A1. Closures in a loop
```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
```
**Answer:** `3, 3, 3`
**Why:** `var` is function-scoped, not block-scoped — all three callbacks share the exact same `i`, which has finished looping (reached 3) by the time any callback runs.

**Follow-up: how do you fix it to print `0, 1, 2`?**
```js
// Fix 1: use let (block-scoped, new binding per iteration)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}

// Fix 2: create a new scope manually with an IIFE (pre-ES6 way)
for (var i = 0; i < 3; i++) {
  (function (capturedI) {
    setTimeout(() => console.log(capturedI), 100);
  })(i);
}
```

---

### A2. Type coercion
```js
console.log(1 + '1');      // '11'  — number coerced to string, then concatenated
console.log(1 - '1');      // 0     — string coerced to number for subtraction
console.log('5' + 3 + 2);  // '532' — left-to-right: '5'+3 → '53', then +2 → '532'
console.log(5 + 3 + '2');  // '82'  — left-to-right: 5+3 → 8 (number), then +'2' → '82'
console.log([] + []);      // ''    — both arrays coerce to empty strings, concatenated
console.log([] + {});      // '[object Object]'
console.log(true + true);  // 2     — booleans coerce to 1/0 for arithmetic
```
**Talking point:** `+` is overloaded — if *either* operand is a string, it does string concatenation (after converting the other operand to a string); otherwise it does numeric addition. `-`, `*`, `/` always coerce both sides to numbers since there's no "subtraction" for strings.

---

### A3. `==` vs `===`
```js
console.log(0 == '0');        // true  — '0' coerced to 0
console.log(0 == '');         // true  — '' coerced to 0
console.log(0 == '0' == '');  // false — evaluated left-to-right: (0=='0') is true, then true == '' is false
console.log(null == undefined); // true — special case in the spec
console.log(null === undefined); // false — different types, no coercion with ===
console.log(NaN === NaN);     // false — NaN is never equal to anything, including itself
```
**Best practice to state:** always use `===`/`!==` in production code to avoid unexpected coercion bugs; use `Number.isNaN(x)` (not `x === NaN`) to check for NaN.

---

### A4. Hoisting with function vs. var
```js
console.log(foo()); // "hoisted!" — function declarations are fully hoisted
function foo() { return 'hoisted!'; }

console.log(bar()); // TypeError: bar is not a function
var bar = function () { return 'not hoisted the same way'; };
// Only `var bar` is hoisted (as undefined); the assignment happens at that line, not before
```

### A5. `this` inside a regular function vs. arrow function in an object
```js
const obj = {
  name: 'Cart',
  regular: function () {
    return this.name;
  },
  arrow: () => {
    return this.name; // `this` here is NOT obj — arrow functions don't have their own `this`
  },
};
console.log(obj.regular()); // 'Cart'
console.log(obj.arrow());   // undefined (or throws in strict mode with no `name` on the outer `this`)
```
**Why:** arrow functions capture `this` lexically from where they're *defined*, not how they're called. Since `arrow` is defined at the top level of the module, its `this` refers to the module's `this` (usually `undefined` in strict mode/ES modules), not `obj`.

---

### A6. Async/await + loop ordering
```js
console.log('start');

async function fetchData() {
  console.log('fetching');
  await new Promise((resolve) => setTimeout(resolve, 0));
  console.log('fetched');
}

fetchData();
console.log('end');

// Output: start, fetching, end, fetched
```
**Why:** code before the first `await` inside an async function runs **synchronously** (that's why "fetching" logs before "end"). The `await` yields control back to the caller — so `console.log('end')` runs next — and "fetched" only resumes once the microtask/timer queue reaches it, after the synchronous code finishes.

---

### A7. Object reference vs. primitive
```js
function mutate(obj) {
  obj.value = 100;
}
const a = { value: 1 };
mutate(a);
console.log(a.value); // 100 — objects are passed by reference (to the reference itself)

function reassign(obj) {
  obj = { value: 999 }; // this only reassigns the LOCAL variable, not the caller's object
}
const b = { value: 1 };
reassign(b);
console.log(b.value); // 1 — unaffected, because `obj = {...}` just points the local `obj` variable elsewhere
```
**Precise framing for an interview:** JS is always **pass-by-value** — but for objects, the "value" being passed is a *reference* to the object. Mutating properties of that object affects the original; reassigning the local parameter variable itself does not.

---

## PART B: Polyfills of Built-in Methods

Implementing built-ins from scratch is one of the most common ways interviewers probe "do you actually understand how this works, or just that it exists?"

### B1. Polyfill `Array.prototype.map`
```js
Array.prototype.myMap = function (callback, thisArg) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    if (i in this) { // skip holes in sparse arrays, matching native behavior
      result.push(callback.call(thisArg, this[i], i, this));
    }
  }
  return result;
};

[1, 2, 3].myMap((x) => x * 2); // [2, 4, 6]
```

### B2. Polyfill `Array.prototype.filter`
```js
Array.prototype.myFilter = function (callback, thisArg) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    if (i in this && callback.call(thisArg, this[i], i, this)) {
      result.push(this[i]);
    }
  }
  return result;
};
```

### B3. Polyfill `Array.prototype.reduce`
```js
Array.prototype.myReduce = function (callback, initialValue) {
  let acc = initialValue;
  let startIndex = 0;

  if (acc === undefined) {
    if (this.length === 0) throw new TypeError('Reduce of empty array with no initial value');
    acc = this[0];
    startIndex = 1;
  }

  for (let i = startIndex; i < this.length; i++) {
    if (i in this) acc = callback(acc, this[i], i, this);
  }
  return acc;
};

[1, 2, 3, 4].myReduce((sum, n) => sum + n, 0); // 10
```
**Interviewer likes to see:** handling the case where no `initialValue` is passed (using the first element as the seed) — this is the detail most candidates miss.

### B4. Polyfill `Function.prototype.bind`
```js
Function.prototype.myBind = function (context, ...boundArgs) {
  const originalFn = this; // the function myBind was called on
  return function (...callArgs) {
    return originalFn.apply(context, [...boundArgs, ...callArgs]);
  };
};

function greet(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}
const boundGreet = greet.myBind({ name: 'Alex' }, 'Hello');
boundGreet('!'); // 'Hello, Alex!'
```

### B5. Polyfill `Function.prototype.call` and `.apply`
```js
Function.prototype.myCall = function (context, ...args) {
  context = context || globalThis;
  const fnSymbol = Symbol('fn'); // avoid overwriting an existing property
  context[fnSymbol] = this;
  const result = context[fnSymbol](...args);
  delete context[fnSymbol];
  return result;
};

Function.prototype.myApply = function (context, argsArray = []) {
  context = context || globalThis;
  const fnSymbol = Symbol('fn');
  context[fnSymbol] = this;
  const result = context[fnSymbol](...argsArray);
  delete context[fnSymbol];
  return result;
};
```
**Key idea to explain:** `call`/`apply` work by temporarily attaching the function as a method on the target `context` object, calling it (so `this` naturally becomes `context` inside the function), then cleaning up. Using a `Symbol` avoids accidentally clobbering a real property named `fn`.

### B6. Polyfill `Promise.all` (also shown in the practical file, included here for completeness with `Promise.allSettled` and `Promise.race` alongside it)
```js
function myPromiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = new Array(promises.length);
    let completed = 0;
    if (promises.length === 0) return resolve([]);

    promises.forEach((p, i) => {
      Promise.resolve(p)
        .then((val) => {
          results[i] = val;
          if (++completed === promises.length) resolve(results);
        })
        .catch(reject);
    });
  });
}

function myPromiseAllSettled(promises) {
  return Promise.all(
    promises.map((p) =>
      Promise.resolve(p)
        .then((value) => ({ status: 'fulfilled', value }))
        .catch((reason) => ({ status: 'rejected', reason }))
    )
  );
}

function myPromiseRace(promises) {
  return new Promise((resolve, reject) => {
    promises.forEach((p) => Promise.resolve(p).then(resolve).catch(reject));
  });
}
```

### B7. Polyfill `Object.assign`
```js
function myObjectAssign(target, ...sources) {
  sources.forEach((source) => {
    if (source == null) return; // skip null/undefined sources, matches native behavior
    Object.keys(source).forEach((key) => {
      target[key] = source[key];
    });
  });
  return target;
}
```

---

## PART C: Common Utility Function Implementations

These come up frequently as "write a function that..." prompts, distinct from the built-in polyfills above.

### C1. Memoize
```js
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const slowSquare = (n) => { for (let i = 0; i < 1e8; i++); return n * n; };
const fastSquare = memoize(slowSquare);
fastSquare(5); // slow the first time
fastSquare(5); // instant — cached
```
**Caveat worth mentioning:** `JSON.stringify` as a cache key breaks down for non-serializable args (functions, circular refs) — for those cases you'd need a different key strategy (e.g., a WeakMap keyed on object identity for single-argument object inputs).

### C2. Once (run a function only one time)
```js
function once(fn) {
  let called = false;
  let result;
  return function (...args) {
    if (!called) {
      result = fn.apply(this, args);
      called = true;
    }
    return result;
  };
}

const initialize = once(() => console.log('Initializing...'));
initialize(); // logs
initialize(); // no-op, returns cached result
```
**Commerce use case:** ensuring a "process payment" button handler can't double-fire from a rapid double-click, as a frontend-side safeguard (in addition to backend idempotency keys, which are the real source of truth).

### C3. Compose and Pipe
```js
// pipe: left-to-right execution
const pipe = (...fns) => (initialValue) => fns.reduce((acc, fn) => fn(acc), initialValue);

// compose: right-to-left execution (mathematical function composition order)
const compose = (...fns) => (initialValue) => fns.reduceRight((acc, fn) => fn(acc), initialValue);

const addTax = (price) => price * 1.08;
const applyDiscount = (price) => price * 0.9;
const roundToCents = (price) => Math.round(price * 100) / 100;

const calculateFinalPrice = pipe(applyDiscount, addTax, roundToCents);
calculateFinalPrice(100); // discount → tax → round, in that order
```

### C4. Deep Equal
```js
function deepEqual(a, b) {
  if (a === b) return true; // handles primitives and same-reference objects
  if (typeof a !== 'object' || typeof b !== 'object' || a === null || b === null) return false;

  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;

  return keysA.every((key) => Object.prototype.hasOwnProperty.call(b, key) && deepEqual(a[key], b[key]));
}

deepEqual({ a: 1, b: { c: 2 } }, { a: 1, b: { c: 2 } }); // true
deepEqual({ a: 1 }, { a: 1, b: 2 }); // false
```

### C5. Flatten an Object (nested keys → dot notation)
```js
function flattenObject(obj, prefix = '') {
  return Object.keys(obj).reduce((acc, key) => {
    const newKey = prefix ? `${prefix}.${key}` : key;
    if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
      Object.assign(acc, flattenObject(obj[key], newKey));
    } else {
      acc[newKey] = obj[key];
    }
    return acc;
  }, {});
}

flattenObject({ user: { name: 'Alex', address: { city: 'NYC' } } });
// { 'user.name': 'Alex', 'user.address.city': 'NYC' }
```
**Use case:** useful when logging structured data to a flat-key logging system, or converting nested form state into flat query params.

### C6. Chunk an Array
```js
function chunk(arr, size) {
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}

chunk([1, 2, 3, 4, 5, 6, 7], 3); // [[1,2,3], [4,5,6], [7]]
```
**Use case:** batching API requests (e.g., don't send 10,000 product IDs in one request — chunk into batches of 100).

### C7. Retry with Exponential Backoff
```js
async function retryWithBackoff(fn, maxRetries = 3, baseDelayMs = 200) {
  let attempt = 0;
  while (true) {
    try {
      return await fn();
    } catch (err) {
      attempt++;
      if (attempt >= maxRetries) throw err;
      const delay = baseDelayMs * 2 ** (attempt - 1); // 200ms, 400ms, 800ms...
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}

// Use case: retrying a flaky call to a downstream payment/inventory service
await retryWithBackoff(() => callPaymentGateway(orderId));
```
**Talking point:** mention adding **jitter** (randomizing the delay slightly) in a real production system, to avoid many clients retrying in lockstep and causing a "thundering herd" on the downstream service after an outage.

### C8. Promisify a Callback-Based Function
```js
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn(...args, (err, result) => {
        if (err) reject(err);
        else resolve(result);
      });
    });
  };
}

const fs = require('fs');
const readFileAsync = promisify(fs.readFile);
const data = await readFileAsync('file.txt', 'utf-8');
```
**Mention:** Node has this built in as `util.promisify` — implementing it manually shows you understand the error-first callback convention it relies on.

---

## PART D: Array/String Manipulation Warm-ups (Quick, Common Screening Questions)

### D1. Remove duplicates from an array
```js
const unique = (arr) => [...new Set(arr)];
```

### D2. Check if a string is a palindrome
```js
function isPalindrome(str) {
  const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
  return cleaned === cleaned.split('').reverse().join('');
}
isPalindrome('A man, a plan, a canal: Panama'); // true
```

### D3. Find the first non-repeating character
```js
function firstUniqueChar(str) {
  const counts = {};
  for (const char of str) counts[char] = (counts[char] || 0) + 1;
  for (const char of str) if (counts[char] === 1) return char;
  return null;
}
```

### D4. Count occurrences of each element
```js
function countOccurrences(arr) {
  return arr.reduce((acc, item) => {
    acc[item] = (acc[item] || 0) + 1;
    return acc;
  }, {});
}
countOccurrences(['a', 'b', 'a', 'c', 'b', 'a']); // { a: 3, b: 2, c: 1 }
```

### D5. Deep flatten an array (any nesting depth) — alternative to using `.flat(Infinity)`
```js
function deepFlatten(arr) {
  return arr.reduce(
    (acc, val) => acc.concat(Array.isArray(val) ? deepFlatten(val) : val),
    []
  );
}
// Native equivalent: arr.flat(Infinity)
```

---

## How to Approach These in the Interview

1. **For output-prediction questions (Part A):** talk through your reasoning step by step rather than blurting the answer — interviewers are grading your mental model, not just whether you memorized the outcome.
2. **For polyfills (Part B):** mention the edge case handling explicitly (sparse arrays for `map`/`filter`, missing `initialValue` for `reduce`) — that's usually the actual signal they're looking for, not just "can you loop over an array."
3. **For utility functions (Part C):** after writing the basic version, proactively mention one edge case or production concern (e.g., "in production I'd add jitter to this backoff" or "this memoize cache would need an eviction policy to avoid unbounded growth") — this is what separates a mid-level from senior-leaning answer.
4. **Practice writing these without an IDE's autocomplete** — a live coding round (even virtual) often has minimal tooling support.
