# Redux

Redux is a popular state management library that helps you manage and centralize application state in a predictable way. It’s commonly used with React, but it can be used with any JavaScript framework.

## Key Concepts

1. **Store**: The single source of truth that holds the entire state of the application.
2. **Action**: A plain JavaScript object that describes what happened in the app. Actions have a `type` property that indicates the action type and, optionally, a `payload` that holds any extra data.
3. **Reducer**: A pure function that takes the current state and an action, then returns a new state based on the action type.
4. **Dispatch**: A function that sends an action to the reducer to update the state.
5. **Selectors**: Helper functions that extract specific data from the Redux state.

## Redux Flow

1. **Dispatch an Action**: An event occurs (like a button click), and an action is dispatched.
2. **Reducer Updates State**: The action is sent to the reducer, which updates the state based on the action type.
3. **Store Broadcasts Update**: The store updates, and all subscribed components receive the updated state.

## Example

Here’s a simple counter example using Redux:

```javascript
// Actions
const INCREMENT = 'INCREMENT';
const DECREMENT = 'DECREMENT';

const increment = () => ({ type: INCREMENT });
const decrement = () => ({ type: DECREMENT });

// Reducer
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case INCREMENT:
      return { count: state.count + 1 };
    case DECREMENT:
      return { count: state.count - 1 };
    default:
      return state;
  }
};

// Store
import { createStore } from 'redux';
const store = createStore(counterReducer);

// Dispatching Actions
store.dispatch(increment()); // Increment count by 1
store.dispatch(decrement()); // Decrement count by 1

console.log(store.getState()); // { count: 0 } after both actions
```
## Using Redux with React

```javascript
import React from 'react';
import { Provider, useDispatch, useSelector } from 'react-redux';

const Counter = () => {
  const count = useSelector((state) => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
    </div>
  );
};

// App Component
const App = () => (
  <Provider store={store}>
    <Counter />
  </Provider>
);

export default App;
```
