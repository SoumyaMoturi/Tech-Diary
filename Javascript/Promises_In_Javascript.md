# Promise Methods in JavaScript

## `Promise.all()`

Takes an array of promises and returns a single promise that resolves when all the promises have resolved or rejects if any promise is rejected.

```javascript
Promise.all([promise1, promise2])
  .then((results) => {
    console.log(results); // Array of results from each promise
  })
  .catch((error) => {
    console.error('One or more promises failed:', error);
  });
```

## `Promise.race()`

Returns a promise that resolves or rejects as soon as one of the promises in the array resolves or rejects.

```javascript
Promise.race([promise1, promise2])
  .then((result) => {
    console.log('First promise resolved:', result);
  })
  .catch((error) => {
    console.error('First promise rejected:', error);
  });

```


## `Promise.allSettled()`

Returns a promise that resolves after all of the given promises have either resolved or rejected, with an array of objects describing the outcome of each promise.

```javascript
Promise.allSettled([promise1, promise2])
  .then((results) => {
    results.forEach((result) => console.log(result.status));
  });

```

## `Promise.any()`

Returns a promise that resolves as soon as any of the promises in the array resolves, ignoring any rejections.

```javascript
Promise.any([promise1, promise2])
  .then((result) => {
    console.log('First promise resolved:', result);
  })
  .catch((error) => {
    console.error('All promises rejected:', error);
  });

```





