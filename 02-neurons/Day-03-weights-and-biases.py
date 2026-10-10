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