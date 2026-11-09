# Vector

A **vector** is a mathematical quantity that has both:

1. **Magnitude** (size or length)
2. **Direction**

Unlike a scalar, which has only magnitude, a vector describes how much of something exists and in which direction it acts.

---

## Examples of Vectors

| Quantity | Magnitude | Direction | Vector? |
|-----------|-----------|-----------|----------|
| Distance | 10 km | No | ❌ |
| Displacement | 10 km | East | ✅ |
| Speed | 20 m/s | No | ❌ |
| Velocity | 20 m/s | East | ✅ |
| Force | 50 N | Right | ✅ |
| Acceleration | 9.8 m/s² | Downward | ✅ |

---

## Representation

Vectors are usually represented using an arrow above a letter:

\[
\vec{A}
\]

Or in component form:

\[
\vec{A} = (x, y)
\]

Example:

\[
\vec{A} = (3, 4)
\]

This means:
- 3 units along the x-axis
- 4 units along the y-axis

---

## Magnitude of a Vector

The magnitude (length) of a vector is calculated using:

\[
|\vec{A}| = \sqrt{x^2 + y^2}
\]

For the vector:

\[
\vec{A} = (3, 4)
\]

\[
|\vec{A}| = \sqrt{3^2 + 4^2}
\]

\[
|\vec{A}| = \sqrt{9 + 16}
\]

\[
|\vec{A}| = 5
\]

---

## Types of Vectors

### 1. Zero Vector
A vector with zero magnitude.

Example:

\[
(0, 0)
\]

### 2. Unit Vector
A vector whose magnitude is 1.

Example:

\[
\hat{i}, \hat{j}, \hat{k}
\]

### 3. Equal Vectors
Vectors having the same magnitude and direction.

### 4. Parallel Vectors
Vectors that point in the same or opposite directions.

---

## Vector Operations

### Addition

\[
(2,3)+(4,5)=(6,8)
\]

### Subtraction

\[
(5,7)-(2,3)=(3,4)
\]

### Scalar Multiplication

\[
2(3,4)=(6,8)
\]

---

## Applications of Vectors

Vectors are widely used in:

- Physics
  - Force
  - Velocity
  - Acceleration
- Engineering
- Computer Graphics
- Robotics
- Navigation Systems
- Machine Learning and Data Science

---

## Vector in Computer Science

In programming, a **vector** often refers to a dynamic array that can store multiple elements.

Example:

```cpp
vector<int> numbers = {10, 20, 30, 40};
```

The vector can grow or shrink
