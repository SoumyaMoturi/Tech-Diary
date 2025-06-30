# Angular Js


## What is Angular?
 - A **javascript frontend framework** which helps with building interactive, modern web user interfaces.
 - It is also a collection of tools and features like CLI, debugging tools and plugins for IDE's.

## Why do we need a framework or why we use Angular?
  we don't need angular or any framework for trivial websites and webapps.But framework simplifies the process of building complex, interactive web user interfaces.
  
- Angular promotes declarative programming, allowing developers to describe what the UI should look like, rather than writing step-by-step instructions like in imperative JavaScript.

```javascript
// Imperative (JavaScript):

const heading = document.createElement('h1');
heading.textContent = 'Welcome, Soumya!';
document.body.appendChild(heading);

// Declarative (Angular Template):

<h1>Welcome, {{ userName }}!</h1>
```
- Angular uses components to separate concerns, meaning each piece of functionality—like UI, behavior, and data—lives in its own self-contained unit. This keeps code modular, easier to test, and simpler to maintain.
Each component has its own template, style, and logic, making it easier to:
 1. Update one piece without touching the others
 2. Reuse components elsewhere (like UserCardComponent in a search result)
 3. Test in isolation
