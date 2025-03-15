
# JavaScript Tips

## Finding the Size of a Variable in Bytes

- JavaScript doesn't provide a built-in way to directly measure the memory size of a variable. However, you can use the `sizeof` package to estimate the size of a variable. First, you'll need to install it.

### Example Code
```javascript
const sizeof = require('sizeof');
const obj = { name: 'John', age: 30, city: 'New York' };
const size = sizeof(obj);
console.log(`Size of the object: ${size} bytes`);
```

## Handling User Input from Console in VS Code

- To take user input in JavaScript from the terminal using VS Code, you can use the `readline-sync` package.

```javascript
const readlineSync = require('readline-sync');
// Ask a question
const name = readlineSync.question('What is your name? ');
console.log(`Hello, ${name}!`);
```
