# Day 3: Understanding Weights and Biases

## 🎯 Learning Objectives

On Day 3 of my AI From Scratch journey, I explored how weights and biases affect the calculation performed by an artificial neuron.

My goals were to:

- Understand the purpose of weights and biases.
- Learn how positive, negative, and zero weights affect a neuron's output.
- Understand why a bias is added to the weighted input.
- Implement a neuron calculation using user-provided values.
- Practise mathematical calculations before running the code.
- Distinguish manually changing parameters from training a model.

## 🧠 Key Concepts

### 1. Weight

A weight determines how much an input contributes to the neuron's weighted sum.

- A positive weight makes the input contribute positively when the input is positive.
- A negative weight makes the input contribute negatively when the input is positive.
- A zero weight means that the input contributes nothing to the weighted sum.

The effect of a weight depends on the input value and the other components of the model.

### 2. Bias

A bias is an adjustable constant added to the weighted input.

It allows the neuron to shift its weighted sum independently of the input value.

Without a bias, the weighted sum is:

\[
z=xw
\]

With a bias, it becomes:

\[
z=xw+b
\]

### 3. Weighted Sum

For a single input, the formula is:

\[
z=xw+b
\]

Where:

- \(x\) = input
- \(w\) = weight
- \(b\) = bias
- \(z\) = weighted sum before activation

## 💻 Python Implementation

**File:** `day-03-weights-and-biases.py`

```python
# Day 3: Understanding Weights and Biases

# Step 1: Take input from the user
x = float(input("Enter the input value (x): "))
w = float(input("Enter the weight (w): "))
b = float(input("Enter the bias (b): "))

# Step 2: Calculate the weighted input
weighted_input = x * w

# Step 3: Add the bias
z = weighted_input + b

# Step 4: Display the calculations
print("\n--- Neuron Calculation ---")
print("Input:", x)
print("Weight:", w)
print("Bias:", b)
print("Weighted input:", weighted_input)
print("Final result (z):", z)
```

## ▶️ How to Run

From the repository root, run:

```bash
python 02-neurons/day-03-weights-and-biases.py
```

## 🧪 Experiments

| Experiment | Input | Weight | Bias | Result |
|---|---:|---:|---:|---:|
| A: Positive weight | 5 | 2 | 1 | 11 |
| B: Negative weight | 5 | -2 | 1 | -9 |
| C: Zero weight | 5 | 0 | 4 | 4 |

### Additional calculation

Given:

\[
x=10,\quad w=0.5,\quad b=-2
\]

The result is:

\[
z=(10\times0.5)-2=3
\]

## 📚 What I Learned

1. Weights control how inputs contribute to a neuron's weighted sum.
2. Bias shifts the weighted sum by an adjustable constant.
3. Negative weights can produce negative contributions.
4. A zero weight removes that input's contribution to the weighted sum.
5. Python's `float()` allows decimal inputs.
6. Changing a parameter manually is not the same as learning it from data.
7. A weighted sum alone is not a complete trainable neural network.

## ⚠️ Current Limitations

This program calculates a weighted sum and bias. It does not yet include:

- An activation function.
- A loss function.
- Automatic adjustment of weights and bias.
- A training loop.

These concepts will be implemented in later stages of the project.

## 🚀 Next Steps

- Learn why activation functions are used.
- Implement activation functions in Python.
- Explore how neurons can produce nonlinear outputs.
- Build toward a neural network that can learn from examples.

## 📌 Progress

- [x] Implemented a neuron calculation using user inputs.
- [x] Experimented with positive, negative, and zero weights.
- [x] Explored positive and negative biases.
- [x] Practised manual calculations.
- [x] Distinguished manual parameter changes from training.