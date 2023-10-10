# How javascript works?

Javascript runs inside a certain environment.Basically there are two types of environments.
1. **Browser**
    - Inside browser wewrite client side javascript (i.e adding dynamic interactivity to web pages,form validations etc)
2. **Node.js**
    - Node js is a runtime environment where we write server side javascript code (i.e accepting network requests and responding to them)

 ``` mermaid

flowchart TD;
    Environment --> Browser;
    Environment --> NodeJs;
    Browser --> Google;
    Google --> V8["V8 (Js Engine)"];

```

**Javscript Engine** : It is nothing but a program written in c++ which converts javascript code into a code that processor can understand.Javascript Engine follows ECMA standard.

Different Browsers have different javascript Engines.For example,
  * Google - v8 Engine
  * IE - Chakra
  * Firefox - Spider Monkey
  * Safari - Javascript Core
    
As all js Engines follow ECMA script,they work similarly and executes our javascript code.


# How Js Engine converts Js code to machine code?

``` mermaid

flowchart LR
    subgraph "JS ENGINE"
    direction LR
    jscode["JS CODE"] --> PARSER
    PARSER --> check{"Checks Js syntax?"}
    check --> |correct|AST
    AST --> |AST|INTERPRETER
    INTERPRETER --> |"byte code"|COMPILER
    COMPILER --> |"machine code"|PROCESSOR
    end

```

**PARSER** : 
 * Parser is a program that knows javascript syntax and rules.
 * Parser takes javascript code and checks line by line and throws an error if syntax is wrong.
 * If the entire code syntax is correct parser generates an **ABSTRACT SYNTAX TREE**(AST).
 
 Here is the website link to convert [JS CODE TO AST](https://astexplorer.net/)


**ABSTRACT SYNTAX TREE** (AST):
* **Reason for parser to create AST**  - It is easier to convert into machine code when we have code in tree data structure rather than complete js code.

**INTERPRETER**:(translates line by line)
* Interpreter takes AST and then converts it to IR (intermediate representation i.e byte code).
* why interpreter creates IR?
  .* when code gets compiled to machine code it needs to match the hardware where the code is running.
  .* Machine code written differs for each processors.Here byte code is universal (i.e it doesnt matter on what hardware you ar running,it matches any hardware).This makes it easy for conversion into machine code.

**COMPILER**:(translate all code to machine code at a time before executing)
* compiler takes that byte code and converts it into machine code.
* then the processor takes this machine code and executes our javascript code.

  JAVSCRIPT uses **JIT COMPILER**
  **JIT COMPILER** : Mixture of interpreter and compiler.Translates the source to machine code while running the application.
  eg: 

   


