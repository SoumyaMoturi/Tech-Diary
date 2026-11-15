# Deep Learning

## 1. Deep Learning

**Deep Learning** is a subset of **Machine Learning** that uses Artificial Neural Networks (ANNs) with multiple hidden layers to learn complex patterns from data. It is inspired by the structure and functioning of the human brain.

### Applications
- Image Recognition
- Speech Recognition
- Natural Language Processing (NLP)
- Self-Driving Cars
- Recommendation Systems

---

## 2. Biological Neural Network (BNN)

A **Biological Neural Network** consists of interconnected neurons present in the human brain and nervous system.

### Components of a Biological Neuron

- **Dendrites**: Receive signals from other neurons.
- **Cell Body (Soma)**: Processes incoming signals.
- **Axon**: Sends signals to other neurons.
- **Synapse**: Junction where neurons communicate.

### Characteristics
- Made up of billions of neurons.
- Learns through experience.
- Serves as the inspiration for Artificial Neural Networks.

---

## 3. Artificial Neuron

An **Artificial Neuron** is the fundamental processing unit of an Artificial Neural Network.

### Working of an Artificial Neuron

1. Receives input values.
2. Multiplies inputs with weights.
3. Computes the weighted sum.
4. Applies an activation function.
5. Produces an output.

### Mathematical Representation

\[
y = f(\sum w_i x_i + b)
\]

Where:

- \(x_i\) = Inputs
- \(w_i\) = Weights
- \(b\) = Bias
- \(f\) = Activation Function
- \(y\) = Output

---

## 4. Classification Example: Shahrukh Khan vs Amir Khan

Suppose we want to classify an image as either **Shahrukh Khan** or **Amir Khan**.

### Input Features

- Face shape
- Eye shape
- Hair style
- Beard pattern
- Facial measurements

### Output Classes

- Class 1 → Shahrukh Khan
- Class 2 → Amir Khan

The neural network learns the characteristics of both actors using many training images and predicts the correct class for a new image.

### Classification Flow

```
Input Image
      ↓
Feature Extraction
      ↓
Neural Network
      ↓
-------------------
| Shahrukh Khan   |
| Amir Khan       |
-------------------
      ↓
Predicted Class
```

**This is a Binary Classification Problem** because there are only two possible output classes.

---

## 5. McCulloch-Pitts (MP) Neuron

The **McCulloch-Pitts Neuron (MP Neuron)** was the **first artificial neuron model**, proposed by **Warren McCulloch** and **Walter Pitts** in **1943**.

### Key Characteristics

- Accepts only **Boolean (Binary) Inputs**.
- Input values can be **0 or 1**.
- Produces a **Binary Output (0 or 1)**.
- Uses a threshold value for decision making.
- Forms the foundation of modern neural networks.

### MP Neuron Model

<div align="center">

Input x₁ ─┐  
          │
Input x₂ ─┼──► Summation ► Threshold ► Output Y
          │
Input x₃ ─┘

</div>

### Mathematical Rule

\[
Y =
\begin{cases}
1, & \text{if } \sum x_i \ge \theta \\
0, & \text{otherwise}
\end{cases}
\]

Where:

- \(x_i\) = Binary inputs
- \(\theta\) = Threshold
- \(Y\) = Output

