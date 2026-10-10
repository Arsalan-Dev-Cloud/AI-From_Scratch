# Day 2: Building a Single Artificial Neuron

## 🎯 Learning Objectives

On Day 2 of my AI From Scratch journey, I implemented the basic calculation performed by an artificial neuron using pure Python.

My goals were to understand:

- What an artificial neuron is.
- How inputs, weights, and biases work together.
- How to calculate a neuron's weighted sum.
- How changing weights and biases affects the output.
- Why manually calculating an output is different from training a neural network.

## 🧠 What Is an Artificial Neuron?

An artificial neuron is a computational unit used in neural networks. It receives one or more inputs, combines them using weights and a bias, and can then pass the result through an activation function.

In this exercise, I implemented the weighted-sum calculation without an activation function.

## 📐 Mathematical Formula

For a neuron with one input:

\[
z = xw + b
\]

Where:

- \(x\) = input value
- \(w\) = weight
- \(b\) = bias
- \(z\) = weighted sum before activation

For multiple inputs, the formula becomes:

\[
z = x_1w_1+x_2w_2+\cdots+x_nw_n+b
\]

Each input has its own weight, which determines its contribution to the weighted sum.

## 💻 Python Implementation

**File:** `day-02-single-neuron.py`

```python
# Day 2: My First Artificial Neuron

# Step 1: Define the input
x = 3

# Step 2: Define the weight
w = 2

# Step 3: Define the bias
b = 1

# Step 4: Calculate the neuron's output
z = (x * w) + b

# Step 5: Display the result
print("Input:", x)
print("Weight:", w)
print("Bias:", b)
print("Neuron output:", z)
```

## ▶️ How to Run

From the root of the repository, execute:

```bash
python 02-neurons/day-02-single-neuron.py
```

## 🧪 Expected Output

```text
Input: 3
Weight: 2
Bias: 1
Neuron output: 7
```

## 🔬 Experiments and Calculations

### Experiment 1: Positive weight

Given:

\[
x=5,\quad w=3,\quad b=2
\]

Calculation:

\[
z=(5\times3)+2=17
\]

### Experiment 2: Negative weight

Given:

\[
x=4,\quad w=-2,\quad b=3
\]

Calculation:

\[
z=(4\times-2)+3=-5
\]

A negative weight can make an input decrease the weighted sum as the input increases.

### Experiment 3: Zero weight

If the weight is zero:

\[
z=(x\times0)+b=b
\]

The input has no contribution to the weighted sum, so the output before activation equals the bias.

## 📚 Key Concepts Learned

- An artificial neuron combines inputs using weights and a bias.
- Weights control how strongly inputs contribute to the weighted sum.
- Bias provides an adjustable constant in the calculation.
- Negative weights can reduce the weighted sum.
- A zero weight removes the input's contribution.
- The weighted sum is calculated before an activation function is applied.
- A manually configured neuron does not learn until a training procedure adjusts its parameters.

## ⚠️ Important Distinction

This program implements the basic mathematical operation of a neuron. It does not yet contain an activation function, a loss function, or a training algorithm.

Therefore, it is a foundational neuron calculation rather than a complete trainable neural network.

## 🚀 Next Steps

- Study weights and biases in greater depth.
- Understand activation functions such as ReLU and sigmoid.
- Implement neurons that accept multiple inputs.
- Build a layer containing multiple neurons.
- Learn how training adjusts weights and biases.

## 📌 Progress

- [x] Implemented a single-neuron weighted sum.
- [x] Calculated outputs manually.
- [x] Explored positive, negative, and zero weights.
- [x] Understood the role of bias.
- [x] Distinguished a fixed calculation from learning.