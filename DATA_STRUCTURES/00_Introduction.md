# Data Structures and Algorithms

### Interview Question Links

- [Top 50+ Ineterview Questions](https://www.interviewbit.com/data-structure-interview-questions/)

# Algorithm:

A collection of steps to solve a problem.

### Why Learn DSA?

- **To optimize your code**, you can use data structures and algorithm techniques. When you gain in-depth knowledge of DSA, you can quickly make decisions about when to choose which data structure and algorithm to optimize your program in terms of time and space complexity.

# DATA STRUCTURES:

A named location that can be used to store and organize data.
Data structures are a fundamental concept in computer science, essential for organizing and storing data efficiently. They can be broadly categorized into two types: Linear and Non-Linear. Below is a detailed segregation of various data structures with a clear mind mapping.

## 1. Linear Data Structures

- **Arrays**

  - Fixed-size, indexed collections of elements.
  - Elements are stored in contiguous memory locations.
  - Accessed by index.
  - **Links**:
    -- <a href="https://www.geeksforgeeks.org/javascript-arrays/#basic-terminologies-of-javascript-array" target="_blank" rel="noopener"><span>Arrays in JavaScript</span> </a>.

- **Linked Lists**
  - **Singly Linked List**: Each node contains data and a reference to the next node.
  - **Doubly Linked List**: Each node contains data and references to both the next and previous nodes.
  - **Circular Linked List**: The last node points back to the first node, forming a circle.
- **Stacks**
  - LIFO (Last In, First Out) principle.
  - Operations: `push` (insert), `pop` (remove).
  - Applications: Function call management, expression evaluation.
- **Queues**
  - FIFO (First In, First Out) principle.
  - Types:
    - **Simple Queue**: Basic enqueue and dequeue operations.
    - **Circular Queue**: The last position is connected back to the first position.
    - **Priority Queue**: Elements are dequeued based on priority.
    - **Double-ended Queue (Deque)**: Insertion and deletion can occur at both ends.

## 2. Non-Linear Data Structures

- **Trees**
  - Hierarchical structure with a root node and child nodes.
  - Types:
    - **Binary Tree**: Each node has at most two children.
    - **Binary Search Tree (BST)**: Left child < root < right child.
    - **AVL Tree**: Self-balancing binary search tree.
    - **Red-Black Tree**: A self-balancing binary search tree with additional properties.
    - **N-ary Tree**: Each node can have at most N children.
    - **Heap**: A special tree-based data structure (Max-Heap, Min-Heap).
- **Graphs**
  - Consist of nodes (vertices) and edges.
  - Types:
    - **Undirected Graph**: Edges have no direction.
    - **Directed Graph (Digraph)**: Edges have a direction.
    - **Weighted Graph**: Edges have weights.
    - **Unweighted Graph**: Edges have no weights.
    - **Cyclic Graph**: Contains at least one cycle.
    - **Acyclic Graph**: Contains no cycles (DAG - Directed Acyclic Graph).

## 3. Hash-based Data Structures

- **Hash Table (Hash Map)**
  - Key-value pairs.
  - Uses a hash function to compute an index into an array of buckets.
  - Applications: Fast data retrieval, caching.

## 4. Advanced Data Structures

- **Trie (Prefix Tree)**
  - A tree-like structure that stores strings efficiently.
  - Commonly used in search operations, especially for dictionaries.
- **Segment Tree**
  - Used for answering range queries efficiently.
- **Suffix Tree**
  - A compressed trie for a string, used in string matching algorithms.
- **Disjoint Set (Union-Find)**

  - Manages a partition of a set into disjoint subsets.
  - Used in network connectivity, Kruskal’s algorithm.
