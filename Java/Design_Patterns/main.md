
# Design Patterns

## Table of Contents

| Section | Topic |
|---------|-------|
| **1. Creational Design Patterns** | 
| **2. Structural Design Patterns** | 
| **3. Behavioral Design Patterns** |
| **4. Quick Tips** | [Summary of pattern usage](#quick-tips) |

## **Creational Design Patterns** (Object Creation)
| Pattern | Description | Example Use Case |
|---------|------------|-----------------|
| **Singleton** | Ensures a class has only one instance & provides a global access point. | Logger, Database Connection |
| **Factory Method** | Defines an interface for creating objects but lets subclasses alter the type. | ShapeFactory for creating different shape objects. |
| **Abstract Factory** | Provides an interface for creating families of related objects. | UI Theme Factory (Windows, MacOS styles). |
| **Builder** | Separates object construction from representation for complex objects. | Creating an HTTP request step by step. |
| **Prototype** | Creates new objects by copying an existing object. | Clone functionality (e.g., duplicating game characters). |

---

## **Structural Design Patterns** (Object Composition)
| Pattern | Description | Example Use Case |
|---------|------------|-----------------|
| **Adapter** | Allows incompatible interfaces to work together. | Connecting legacy code with new systems. |
| **Bridge** | Separates abstraction from implementation. | Remote control (Abstraction) + TV implementation. |
| **Composite** | Treats individual & composed objects uniformly. | File system (Files & Folders). |
| **Decorator** | Adds responsibilities to objects dynamically. | Adding scrollbars to a window. |
| **Facade** | Provides a simplified interface to a complex subsystem. | Web API Gateway for multiple microservices. |
| **Flyweight** | Reduces memory usage by sharing common object data. | Text editor storing unique character objects. |
| **Proxy** | Provides a surrogate for another object to control access. | Lazy-loading heavy objects (e.g., Virtual Proxy). |

---

## **Behavioral Design Patterns** (Object Interaction)
| Pattern | Description | Example Use Case |
|---------|------------|-----------------|
| **Chain of Responsibility** | Passes requests along a chain of handlers. | Middleware in Express.js. |
| **Command** | Encapsulates a request as an object. | Undo/Redo functionality in a text editor. |
| **Interpreter** | Implements a grammar for a language. | SQL query parsing. |
| **Iterator** | Provides a way to traverse collections. | Iterating through a list in Python. |
| **Mediator** | Reduces direct communication between objects. | Chatroom where users don’t interact directly. |
| **Memento** | Captures an object’s state for rollback. | Save/Load game feature. |
| **Observer** | Defines a one-to-many dependency between objects. | Event listeners in JavaScript. |
| **State** | Changes object behavior based on state. | Traffic Light System. |
| **Strategy** | Defines a family of algorithms & selects one dynamically. | Payment methods (Credit Card, PayPal). |
| **Template Method** | Defines a skeleton algorithm with subclass-defined steps. | Cooking recipe with customizable steps. |
| **Visitor** | Separates algorithms from object structure. | Syntax tree processing in compilers. |

---

## **Quick Tips**
- **Use Creational patterns** when object creation logic is complex.  
- **Use Structural patterns** when working with relationships between objects.
- **Use Behavioral patterns** when defining communication between objects.  

![Design Patterns Overview](/pattern1.png)
![Design Patterns Overview](/pattern2.png)


