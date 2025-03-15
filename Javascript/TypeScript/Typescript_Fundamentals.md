# Table Of Contents
---
|Topic|SubTopics|
|:---|:---|
|[Why TypeScript?](#why-typescript?)||
|[Key features of Typescript](#key-features-of-typescript)||
|[How TypeScript Compilation Works?](#how-typeScript-compilation-works)||
||[tsc](#tsc)|
||[tsconfig](#tsconfig)|
|[Benefits of Types](#benefits-of-types)||
|[Built-in Types](#built-in-types)||
|[Additional Built-in Types](#additional-builtin-types)||
|[Typescript Functions](#typescript-functions)||
|[Creating and using Interfaces](#creating-and-using-interfaces)||
|[Creating and using Classes](#creating-and-using-classes)||
|[Creating and using generics](#creating-and-using-generics)||
||[Generic Functions](#generic-functions)|
||[Generic Classes](#generic-classes)|
||[Generic Interfaces](#generic-interfaces)|
||[Generic Constraints](#generic-constraints)|
||[Built-in Constraints](#built-in-constraints)|
||[Benefits of Generics](#benefits-of-generics)|
|[code snippets](#code-snippet)||
---


# TypeScript

- TypeScript, a superset of JavaScript developed by Microsoft.

## Why Typescript?

- Detect more errors during development

## Key features of Typescript :

- Strongly Typed
- Classes
- Interfaces
- Generics


## How TypeScript Compilation Works?


- All typescript is compiled to javascript depends on target browser and we can also control the output.


### `tsc`

`tsc` is the TypeScript Compiler. It takes TypeScript code (.ts or .tsx files) and compiles it into JavaScript code (.js files) that can be executed by a JavaScript runtime.


- **To install**
Can install tsc globally using npm (Node Package Manager) by running: 

```text
    npm install -g typescript
```
- **To Compile**
Can compile TypeScript files by running the following command in the terminal

```text
 tsc yourfile.ts
```


**More about Tsc :** https://medium.com/@seanbridger/typescript-basics-1-10-typescript-compiler-tsc-and-tsconfig-f9bf0134c5eb

### `tsconfig`

`tsconfig.json` is a configuration file for TypeScript projects. It allows you to specify compiler options, include/exclude files, and configure other settings for our typeScript project.

- **Create**

Can create a tsconfig.json file manually in the root of your project or use the tsc --init command to generate a basic configuration file.




https://caniuse.com/ - one of the website to check the compatible ecma script target version (ES2017) that are supported on browsers

## Getting Started


```typescript

let x; // x is any type
let y; // y is any type
x = 13; // here x changes to number type
y = 1; // here x changes to number type
let sum = x + y; // sum is number type

```
## Benefits of Types

- The below code completely works fine in javascript where it cnsiders x and y as string concatenation and returns 22.

```typescript
function add(x, y) {
    return x + y;
}
const result = add(2 , "2");
```
But actual expected output is 4 i.e integer addition.So typescript is helpful in this situation. 

```typescript
function add(x : number, y: number) {
    return x + y;
}
const result = add(2 , "2");
```

output for the above snippet is

```text
Argument of type 'string' is not assignable to parameter of type 'number'.
```
## Built-in Types

- string
- number
- boolean
- array

Typescript types can be used on variables and parameters following the `variableName: type` pattern

## Additional Built-in Types

- undefined : never assigned a value then is undefined
- null : it doesn't have a value
- any : it can hold any datatype (string, number, array ..) 
- void : a functions does something and return no value.

- union: 
In cases where a variable can be one or more types a union type can be used.

example: 

```typescript 
let firstName: string | undefined | null
```
- function :
- enum : 
    -- Represent a set of name constants.
    -- Enums are not a "type-level" extension of javascript.
    -- They generate javascript code that is used at runtime.

```typescript

enum ProductType{
    Sports,
    HomeGoods,
    Groceries
}
let productType = ProductType.Sports

```

## Typescript Functions

### Defining functions: 

```typeScript

// function declaration - hoisted
function func_name( param1: param1_type , param2 : param2_type){
    const var1: var_type = param1 + param2;
    return var1;
}
```

```typeScript
// function expression - not hoisted
const addNumbers = function func_name( param1: param1_type , param2 : param2_type){
    const var1: var_type = param1 + param2;
    return var1;
}
```

### Return Values and Types

```typeScript

function func_name( param1: param1_type , param2 : param2_type) : var1_type {
    const var1: var_type = param1 + param2;
    return var1;
}
```

### Asynchronous Functions

Asynchronous functions in TypeScript (and JavaScript) allow you to write code that performs asynchronous operations more readably and maintainably. These functions return a Promise, and you can use the async and await keywords to handle asynchronous code.

```typescript

// Function that returns a promise which resolves after a delay
function delay(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Asynchronous function using async and await
async function exampleAsyncFunction(): Promise<void> {
  console.log("Start");

  await delay(2000); // Wait for 2 seconds

  console.log("End");
}

exampleAsyncFunction(); // Output: Start (waits 2 seconds) End

```

**Explanation:**

- The delay function returns a Promise that resolves after a specified delay.

- The exampleAsyncFunction is an asynchronous function marked with the async keyword.

- Inside the async function, the await keyword is used to pause the execution until the delay function's Promise resolves.

- This allows you to write asynchronous code in a more synchronous-looking style, improving readability.

```typescript
// Interface for the data being fetched
interface User {
  id: number;
  name: string;
  username: string;
  email: string;
}
// Asynchronous function to fetch data from an API
async function fetchUserData(userId: number): Promise<User> {
  const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const userData: User = await response.json();
  return userData;
}
// Example usage
fetchUserData(1).then(user => {
  console.log(user);
}).catch(error => {
  console.error("Error fetching user data:", error);
});
```

**Explanation:**

- The fetchUserData function is an asynchronous function that fetches user data from an API.

- The await keyword is used to wait for the fetch operation and the JSON parsing to complete.

- The function returns a Promise that resolves with the fetched user data.

- The function is called with a user ID, and the result is handled with .then and .catch to log the user data or handle errors.

### Arrow Functions

Arrow functions in TypeScript are a shorthand syntax for writing functions. They allow you to write cleaner and more concise code.

```typescript
// Traditional function
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function
const add = (a: number, b: number): number => a + b;

console.log(add(2, 3)); // Output: 5

```
**Explanation:**

- In the traditional function, you define a function with the function keyword.

- In the arrow function, you use the const keyword to declare a variable and assign it an arrow function.

- The syntax for the arrow function is (parameters) => expression.

- Arrow functions are especially useful for writing small, one-liner functions.

Arrow functions also have a different behavior when it comes to the this keyword. In traditional functions, this refers to the function's execution context, while in arrow functions, this retains the value of the enclosing lexical context.

```typescript

class Person {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  // Traditional function
  greet() {
    setTimeout(function() {
      console.log(`Hello, my name is ${this.name}`);
    }, 1000);
  }

  // Arrow function
  greetArrow() {
    setTimeout(() => {
      console.log(`Hello, my name is ${this.name}`);
    }, 1000);
  }
}

const person = new Person("John");
person.greet(); // Output: Hello, my name is undefined
person.greetArrow(); // Output: Hello, my name is John

```

**Explanation:**

- In the greet method, the traditional function doesn't have access to the this value of the Person instance, so this.name is undefined.

- In the greetArrow method, the arrow function captures the this value from its lexical scope, which is the Person instance, so this.name is "John".

### Optional Parameters

In TypeScript, optional parameters and default parameters allow you to define functions with flexible arguments. Let's look at examples of both:

**Optional Parameters:**

Optional parameters are parameters that may or may not be provided by the caller. You can define an optional parameter by appending a `?` to the parameter name.

```typescript

function greet(name: string, age?: number): string {
  if (age) {
    return `Hello, ${name}! You are ${age} years old.`;
  } else {
    return `Hello, ${name}!`;
  }
}

console.log(greet("Alice")); // Output: Hello, Alice!
console.log(greet("Bob", 25)); // Output: Hello, Bob! You are 25 years old.

```

### Default Parameters

Default parameters are parameters that have a default value if `no value` or `undefined` is provided by the caller.

```typescript
function greet(name: string, age: number = 18): string {
  return `Hello, ${name}! You are ${age} years old.`;
}

console.log(greet("Alice")); // Output: Hello, Alice! You are 18 years old.
console.log(greet("Bob", 25)); // Output: Hello, Bob! You are 25 years old.

```

**Precedence in Function Calls:**

-Required parameters must always be passed.

- Optional parameters may be passed, but if not, they remain undefined.

- Default parameters have a predefined value and will be used if not explicitly passed.

### Combining Optional and Default Parameters

```typescript
function greet(name: string, age?: number, city: string = "Unknown"): string {
  const ageText = age ? `You are ${age} years old` : "Age is unknown";
  return `Hello, ${name}! ${ageText}. You are from ${city}.`;
}

console.log(greet("Alice")); // Output: Hello, Alice! Age is unknown. You are from Unknown.
console.log(greet("Bob", 25)); // Output: Hello, Bob! You are 25 years old. You are from Unknown.
console.log(greet("Charlie", 30, "New York")); // Output: Hello, Charlie! You are 30 years old. You are from New York.
```

In TypeScript, if you pass a default parameter at the end of a function call without passing the optional parameters, it can lead to unexpected results because the default parameter will take the place of the optional parameter if it’s omitted. Here's an example to illustrate this behavior:

```typescript
function greet(name: string, age?: number, city: string = "Unknown"): string {
  const ageText = age ? `You are ${age} years old` : "Age is unknown";
  return `Hello, ${name}! ${ageText}. You are from ${city}.`;
}

// Calling the function without the optional parameter, but with the default parameter
console.log(greet("Alice", "New York")); // Incorrect

```

To avoid this confusion, it's best to ensure that optional parameters are given values before default parameters when calling the function. Alternatively, you can explicitly pass `undefined` for the optional parameter to skip it:

```typescript
// Correct usage
console.log(greet("Alice", undefined, "New York")); // Output: Hello, Alice! Age is unknown. You are from New York.

```

### Rest Parameters

Rest parameters allow you to represent an indefinite number of arguments as an array. You define a rest parameter by using the `...`
syntax before the parameter name.


```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3)); // Output: 6
console.log(sum(4, 5, 6, 7, 8)); // Output: 30

```


### Rest Parameters
Rest parameters allow you to represent an indefinite number of arguments as an array. You define a rest parameter by using the ... syntax before the parameter name.

```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3)); // Output: 6
console.log(sum(4, 5, 6, 7, 8)); // Output: 30

```

**Explanation:**

The sum function takes a rest parameter numbers, which is an array of numbers.

The reduce method is used to sum all the numbers in the array.

### Parameter Destructuring

Parameter destructuring allows you to unpack values from objects or arrays directly in the function signature. This can make your code more readable and concise.

```typescript

interface Person {
  name: string;
  age: number;
  city: string;
}

function greet({ name, age, city }: Person): string {
  return `Hello, ${name}! You are ${age} years old and you live in ${city}.`;
}

const person = {
  name: "Alice",
  age: 25,
  city: "Mumbai"
};

console.log(greet(person)); // Output: Hello, Alice! You are 25 years old and you live in Mumbai.


```


```typescript

function printCoordinates([x, y]: [number, number]): string {
  return `The coordinates are X: ${x}, Y: ${y}`;
}

const coordinates: [number, number] = [10, 20];

console.log(printCoordinates(coordinates)); // Output: The coordinates are X: 10, Y: 20

```

**Explanation:**

- The printCoordinates function takes a tuple (array with a fixed length and types) and destructures its elements (x and y) directly in the parameter list.

- This makes it clear which elements are being accessed and used within the function.


## Creating and using Interfaces

An interface in TypeScript is a powerful way to define the shape of an object. It allows you to specify the structure that an object should have, including properties and their types. Interfaces are used to ensure that objects adhere to a specific structure, which helps with type checking and code readability.

### cases for interfaces : 

- What data am i getting? - discovering what type of object a function or property returns is challanging.
- what data do you pass? - how do you know if you're passing the correct data to a function?
- Drive Consistency - (to maintain consistent data example product A , product B all have same properties like name and id )

so interfaces help for the above scenerio.


### Defining Interfaces

An interface in TypeScript can be defined using the interface keyword, followed by the name of the interface and the shape of the object it describes.

```typescript

interface Person {
  name: string;
  age: number;
  city?: string; // Optional property
}

const person: Person = {
  name: "Alice",
  age: 25,
  city: "Mumbai"
};

console.log(person);

```

**Readonly Properties :**

You can define properties that are read-only, meaning they cannot be modified after being set.

```typescript
interface User {
  readonly id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: "John",
  email: "john@example.com"
};

// user.id = 2; // Error: Cannot assign to 'id' because it is a read-only property.
console.log(user);

```

**Interface Inheritance:**
Interfaces can extend other interfaces, allowing you to create a new interface that includes the properties of one or more existing interfaces.

```typescript
interface Person {
  name: string;
  age: number;
}

interface Employee extends Person {
  employeeId: number;
  position: string;
}

const employee: Employee = {
  name: "Charlie",
  age: 35,
  employeeId: 1234,
  position: "Software Engineer"
};

console.log(employee);

```

**Function Types**
You can define interfaces for functions, specifying the types of parameters and the return type.

```typescript
interface Add {
  (a: number, b: number): number;
}

const add: Add = (a, b) => a + b;

console.log(add(2, 3)); // Output: 5

```

**Indexable Types**

Interfaces can describe objects that can be indexed with a certain type (e.g., strings or numbers).

```typescript
interface StringArray {
  [index: number]: string;
}

const myArray: StringArray = ["Hello", "World"];

console.log(myArray[0]); // Output: Hello
console.log(myArray[1]); // Output: World

```

**Hybrid Types**
An interface can define both a function and properties, allowing you to create objects that act like functions but also have additional properties.

```typescript
interface Counter {
  (start: number): string;
  interval: number;
  reset(): void;
}

function createCounter(): Counter {
  let counter = <Counter>function(start: number) {
    console.log(`Starting at ${start}`);
  };
  counter.interval = 123;
  counter.reset = () => {
    console.log("Counter reset");
  };
  return counter;
}

const counter = createCounter();
counter(10); // Output: Starting at 10
counter.reset(); // Output: Counter reset
console.log(counter.interval); // Output: 123

```

**Interfaces vs Type**:


**Interfaces :** : 

`Declaration`: Defined using the interface keyword.

`Extensibility`: Can be extended using the extends keyword.

`Implementation`: Can be implemented by classes using the implements keyword.

`Merging`: Can be merged, meaning multiple declarations with the same name are merged into one.

```typescript
interface Person {
  name: string;
  age: number;
  city?: string; // Optional property
}

interface Employee extends Person {
  employeeId: number;
  position: string;
}

let person : Person = "samba" // throws an error

```
**Types :**

`Declaration`: Defined using the type keyword.

`Extensibility`: Can be extended using intersection types (&).

`Implementation`: Cannot be implemented by classes.

`Merging`: Cannot be merged like interfaces.

```typescript

type Person = string | {
  name: string;
  age: number;
  city?: string; // Optional property
};

type Employee = Person & {
  employeeId: number;
  position: string;
};

let person : Person = "samba" //doesn't throw error

```
**Key Points:**
- Interfaces are primarily used for defining object shapes and can be extended and merged.
- Types are more flexible and can represent unions, intersections, and other complex types but cannot be implemented by classes or merged.


| Feature          | Interface             | Type                      |
|------------------|-----------------------|---------------------------|
| Declaration      | `interface` keyword   | `type` keyword            |
| Extensibility    | `extends` keyword     | Intersection types (`&`)  |
| Implementation   | Implemented by classes| Not implemented by classes|
| Merging          | Can be merged         | Cannot be merged          |
| Usage            | Primarily for object shapes | More general, including unions |



## Creating and using Classes

Classes can be used to encapsulate data and code.
They act as templates for object instances.

classes act as container with curly braces wrapping everything inside it.

```typescript

class Product{
    //properties

    //constructor

    //functions
}

let product = new Product();

```

### Adding constructor and properties to classes

**Basic Class with Properties:**

```Typescript
class FoodProduct{
    //properties
    id = 0;
    name = "";
    icon = "";
}

let foodProduct = new FoodProduct();
foodProduct.id = 1;
foodProduct.name = "Pizza Slice";
foodProduct.icon = "icon.jpeg";

```

**Explain:**
- This example defines a class FoodProduct with three properties: id, name, and icon.

- The properties are directly declared within the class body and are initialized with default values (0 for id, and empty strings for name and icon).

**Class with Constructor:**

```Typescript
class FoodProduct{
    //properties
    id = 0;
    name = "";
    icon = "";

    //constructor
    constructor(id: number,name : string , icon: string){
        this.id = id;
        this.name = name;
        this.icon = icon;
    }

}

let foodProduct = new FoodProduct(1,"Pizza Slice","icon.jpeg");

```

**Explain :**

- This example also defines a class FoodProduct with the same three properties.

- The main difference is that a constructor is added. The constructor takes three parameters (id, name, and icon) and initializes the properties of the class with the values passed to the constructor.

**Class with Constructor and Auto-Implemented Properties:**

```Typescript
class FoodProduct{
    //properties

    //constructor (auto implemented properties)
    constructor(public id: number,public name : string ,public icon: string){
        
    }

}

let foodProduct = new FoodProduct(1,"Pizza Slice","icon.jpeg");

```

**Explain:**

- This example defines a class FoodProduct with a constructor that uses a shorthand syntax for defining and initializing properties.

- In the constructor, the public modifier before each parameter automatically creates and initializes the properties id, name, and icon.

- There is no need to explicitly declare the properties within the class body or assign them inside the constructor. This shorthand makes the code more concise

### Adding functions to classes

- Functions inside classes doesn't need function keyword at the begining of function.


```typescript

class FoodProduct {
    // constructor (auto implemented properties)
    constructor(public id: number, public name: string, public icon: string) {}

    // method to display product details
    displayDetails(): void {
        console.log(`Product ID: ${this.id}, Name: ${this.name}, Icon: ${this.icon}`);
    }

    // method to change the product name
    changeName(newName: string): void {
        this.name = newName;
    }
}

let foodProduct = new FoodProduct(1, "Pizza Slice", "icon.jpeg");
foodProduct.displayDetails(); // Output: Product ID: 1, Name: Pizza Slice, Icon: icon.jpeg
foodProduct.changeName("Cheese Pizza");
foodProduct.displayDetails(); // Output: Product ID: 1, Name: Cheese Pizza, Icon: icon.jpeg

```

### Extending classes and implementing interfaces

In TypeScript, you can extend classes to create new classes that inherit properties and methods from existing ones. Additionally, you can implement interfaces to ensure that classes adhere to a specific structure.

#### Extending Classes

When you extend a class, you create a new class (subclass) that inherits all properties and methods from an existing class (superclass). The `extends` keyword is used to achieve this.

```typescript
class FoodProduct {
    constructor(public id: number, public name: string, public icon: string) {}

    displayDetails(): void {
        console.log(`Product ID: ${this.id}, Name: ${this.name}, Icon: ${this.icon}`);
    }
}

class PerishableFoodProduct extends FoodProduct {
    constructor(id: number, name: string, icon: string, public expirationDate: Date) {
        super(id, name, icon); // Call the superclass constructor
    }

    displayDetails(): void {
        super.displayDetails(); // Call the superclass method
        console.log(`Expiration Date: ${this.expirationDate.toDateString()}`);
    }
}

let perishableFoodProduct = new PerishableFoodProduct(1, "Milk", "icon_milk.jpeg", new Date(2025, 0, 15));
perishableFoodProduct.displayDetails();
// Output: 
// Product ID: 1, Name: Milk, Icon: icon_milk.jpeg
// Expiration Date: Wed Jan 15 2025

```

**Explanation:**

- FoodProduct is the superclass with properties id, name, icon, and a method displayDetails.

- PerishableFoodProduct is a subclass that extends FoodProduct and adds a new property expirationDate.

- The super keyword is used to call the constructor and methods of the superclass.

- The displayDetails method in the subclass overrides the superclass method and adds additional information.

#### Implementing Interfaces

When you implement an interface, you create a class that adheres to the structure defined by the interface. The `implements` keyword is used to achieve this.

```typescript
interface Product {
    id: number;
    name: string;
    icon: string;
    displayDetails(): void;
}

class FoodProduct implements Product {
    constructor(public id: number, public name: string, public icon: string) {}

    displayDetails(): void {
        console.log(`Product ID: ${this.id}, Name: ${this.name}, Icon: ${this.icon}`);
    }
}

let foodProduct = new FoodProduct(1, "Pizza Slice", "icon.jpeg");
foodProduct.displayDetails(); // Output: Product ID: 1, Name: Pizza Slice, Icon: icon.jpeg

```

**Explanation:**

- The Product interface defines the structure that any class implementing it must follow, including properties id, name, icon, and the method displayDetails.

- The FoodProduct class implements the Product interface and provides the required properties and method.


#### Combining Extending Classes and Implementing Interfaces


```typescript

interface Product {
    id: number;
    name: string;
    icon: string;
    displayDetails(): void;
}

class FoodProduct implements Product {
    constructor(public id: number, public name: string, public icon: string) {}

    displayDetails(): void {
        console.log(`Product ID: ${this.id}, Name: ${this.name}, Icon: ${this.icon}`);
    }
}

class PerishableFoodProduct extends FoodProduct {
    constructor(id: number, name: string, icon: string, public expirationDate: Date) {
        super(id, name, icon);
    }

    displayDetails(): void {
        super.displayDetails();
        console.log(`Expiration Date: ${this.expirationDate.toDateString()}`);
    }
}

let perishableFoodProduct = new PerishableFoodProduct(1, "Milk", "icon_milk.jpeg", new Date(2025, 0, 15));
perishableFoodProduct.displayDetails();
// Output: 
// Product ID: 1, Name: Milk, Icon: icon_milk.jpeg
// Expiration Date: Wed Jan 15 2025

```

**Explanation:**
- The FoodProduct class implements the Product interface and provides the required properties and method.

- The PerishableFoodProduct class extends FoodProduct and adds an additional property expirationDate.

- The displayDetails method in PerishableFoodProduct overrides the superclass method and adds additional information.

**abstract class** - ?

**methods vs functions** - ?



## Creating and using Generics

TypeScript generics provide a way to create reusable and flexible components. They allow you to define functions, classes, and interfaces with a placeholder for the type that can be specified later. This is particularly useful for creating data structures or functions that can work with any data type.


### Generic Functions

Here, `T` is a type variable that acts as a placeholder for the type passed to the function.


```typescript
function identity<T>(arg: T): T {
  return arg;
}
```


### Generic Classes
This class can work with any data type, as specified when the instance is created.


```typescript
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) { return x + y; };

```

### Generic Interfaces

Generic interfaces allow you to define flexible and reusable contracts.

```typescript
interface GenericIdentityFn<T> {
  (arg: T): T;
}

function identity<T>(arg: T): T {
  return arg;
}

let myIdentity: GenericIdentityFn<number> = identity;

```

### Generic Constraints 

we have a function that compares two objects based on a common property. We'll use a constraint to ensure that the objects have this property.

```typescript
interface HasId {
  id: number;
}

function compareById<T extends HasId>(a: T, b: T): number {
  if (a.id > b.id) {
    return 1;
  } else if (a.id < b.id) {
    return -1;
  } else {
    return 0;
  }
}

class Product implements HasId {
  constructor(public id: number, public name: string) {}
}

const product1 = new Product(1, "Product A");
const product2 = new Product(2, "Product B");

console.log(compareById(product1, product2)); // Output: -1

```

In this example, the `HasId` interface ensures that any object passed to the `compareById` function has an `id` property. The Product class implements this interface, so we can safely compare two `Product` objects by their `id`.

### Built-in Constraints

TypeScript comes with several built-in utility types that provide powerful constraints to help developers work more effectively with types. Here are some of the most commonly used built-in constraints, including Partial, Required, Readonly, Record, Pick, and Omit.

-  **`Partial<T>` :**
`Partial<T>` makes all properties in `T` optional. This is useful when you want to create an object that might not have all the properties of a given type.

```typescript
interface User {
  id: number;
  name: string;
  age: number;
}
const partialUser: Partial<User> = { name: 'Alice' };
```

-  **`Required<T>` :** 
`Required<T>`makes all properties in `T` required. This can be useful when you need to ensure that all properties of an object are present.

```typescript
interface User {
  id?: number;
  name?: string;
  age?: number;
}

const user: Required<User> = { id: 1, name: 'Alice', age: 30 };
```

- `Readonly<T>`
`Readonly<T>` makes all properties in `T` read-only. This is useful for creating immutable objects.

```typescript
interface User {
  id: number;
  name: string;
  age: number;
}

const readonlyUser: Readonly<User> = { id: 1, name: 'Alice', age: 30 };
// readonlyUser.id = 2; // Error: Cannot assign to 'id' because it is a read-only property.

```

- `Record<K, T>`
`Record<K, T>` constructs an object type with a set of properties `K` of type `T`. This is useful for creating a type-safe map or dictionary.

```typescript
type UserRoles = 'admin' | 'user' | 'guest';
const roles: Record<UserRoles, string> = {
  admin: 'Administrator',
  user: 'Regular User',
  guest: 'Guest User',
};

```

- `Pick<T, K>`
`Pick<T, K>` creates a new type by picking a set of properties `K` from type `T`. This is useful for creating a subset of an existing type.

```typescript
interface User {
  id: number;
  name: string;
  age: number;
}

type UserPreview = Pick<User, 'id' | 'name'>;

const userPreview: UserPreview = { id: 1, name: 'Alice' };

```

- `Omit<T, K>`
`Omit<T, K>` creates a new type by omitting a set of properties `K` from type `T. This is useful for creating a type that excludes certain properties.

```typescript
interface User {
  id: number;
  name: string;
  age: number;
}

type UserWithoutAge = Omit<User, 'age'>;

const userWithoutAge: UserWithoutAge = { id: 1, name: 'Alice' };

```

### Benefits of Generics:

- Reusability: Write functions or classes once and use them with different types.

- Type Safety: Catch errors at compile time instead of runtime.

- Flexibility: Adapt to different data types without rewriting code.

**Example :** 

Imagine a function that combines two arrays:

```typescript
function combineArrays<T>(arr1: T[], arr2: T[]): T[] {
  return arr1.concat(arr2);
}

let combined = combineArrays<number>([1, 2, 3], [4, 5, 6]);
console.log(combined); // Output: [1, 2, 3, 4, 5, 6]

```

In this example, the function combineArrays is written once and can be used with arrays of any type.


 
## code snippet

```typescript
interface dept {
    deptId: string;
    deptName: string;
}
interface student {
    studentId: number;
    deptId: number
    studentName: string;
}

type Student = dept & student;
const student : Student = {
    studentId : 1,
    deptId: "2",
    studentName: "student1",
}
```

**output** : Type 'string' is not assignable to type 'never'.


2) 
```typescript
interface dept {
    deptId: string;
    deptName: string;
}
interface student {
    studentId: number;
    deptId: number
    studentName: string;
}

type Student = dept | student;
const student : Student = {
    studentId : 1,
    deptId: "2",
    studentName: "student1",
}
```

**output** : Type '{ studentId: number; deptId: string; studentName: string; }' is not assignable to type 'Student'.
  Type '{ studentId: number; deptId: string; studentName: string; }' is not assignable to type 'student'.
    Types of property 'deptId' are incompatible.
      Type 'string' is not assignable to type 'number'.


3)
```typescript
interface dept {
    deptId: string;
    deptName: string;
}
interface student {
    studentId: number;
    deptId: number
    studentName: string;
}

type Student = dept & student;
const student : Student = {
    studentId : 1,
    deptId: 2,
    studentName: "student1",
}
```

 **output:**  Type 'number' is not assignable to type 'never'.

4)
```typescript
interface dept {
    deptId: string;
    deptName: string;
}
interface student {
    studentId: number;
    deptId: number
    studentName: string;
}

type Student = dept | student;
const student : Student = {
    studentId : 1,
    deptId: 2,
    studentName: "student1",
}
```

 **output** : No errors




