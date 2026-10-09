# Day 1: Foundations of AI — My First Prediction

## 🎯 Learning Objectives

Today, I started my journey of learning Artificial Intelligence (AI) from scratch. My goal was to understand the basic concepts of AI and build my first prediction program using Python.

By the end of Day 1, I aimed to understand:

* What Artificial Intelligence (AI) is.
* The difference between AI, Machine Learning (ML), and Deep Learning (DL).
* The basic concepts of data, algorithms, models, training, and inference.
* How a Python program takes input, processes it, and produces output.
* How conditional statements can be used to make simple predictions.

## 📚 Concepts Learned

### 1. What is Artificial Intelligence?

Artificial Intelligence is a field of computer science focused on building systems that perform tasks requiring capabilities commonly associated with human intelligence, such as recognizing patterns, making predictions, understanding language, and solving problems.

### 2. AI vs Machine Learning vs Deep Learning

* **Artificial Intelligence (AI):** The broader field of building intelligent systems.
* **Machine Learning (ML):** A branch of AI in which systems learn patterns from data.
* **Deep Learning (DL):** A branch of machine learning that uses neural networks with multiple layers.

### 3. Important AI Terminology

| Term      | Meaning                                     |
| --------- | ------------------------------------------- |
| Data      | Information used by a program or model      |
| Algorithm | A procedure for solving a problem           |
| Model     | A system that produces outputs from inputs  |
| Training  | The process of learning patterns from data  |
| Inference | Using a trained model to make predictions   |
| Feature   | An input variable used to make a prediction |
| Label     | The target value a model learns to predict  |

### 4. Rule-Based Prediction

Before building a machine learning model, I created a simple rule-based program.

The program uses a predefined condition:

* If study hours are greater than or equal to 4, predict `Pass`.
* Otherwise, predict `Fail`.

This program follows rules written by the developer. It does not learn from data and is therefore not a trained machine learning model.

## 💻 Program Built

**File:** `day-01-first-prediction.py`

The program asks the user to enter the number of study hours and predicts an outcome using an `if-else` statement.

```python
# Day 1: My First Prediction Program

study_hours = int(input("Enter the number of hours you studied: "))

if study_hours >= 4:
    prediction = "Pass"
else:
    prediction = "Fail"

print("\n--- Prediction Result ---")
print("Study hours:", study_hours)
print("Predicted result:", prediction)
```

## 🧠 Python Concepts Practiced

* Variables
* `input()` for accepting user input
* `int()` for converting text into an integer
* `if-else` conditional statements
* Comparison operators (`>=`)
* `print()` for displaying results
* Basic decision-making logic

## 🧪 Test Cases

| Input: Study Hours | Expected Prediction |
| -----------------: | ------------------- |
|                  2 | Fail                |
|                  4 | Pass                |
|                  7 | Pass                |

These results follow the program's predefined rule. They do not represent a real assessment of whether a student will pass an examination.

## 💡 Key Takeaways

1. A program can make a prediction by following predefined rules.
2. Inputs are processed to produce outputs.
3. Features are input variables, while labels are the target values in supervised learning.
4. Rule-based prediction and machine learning are different approaches.
5. Understanding Python fundamentals is important before implementing neural networks from scratch.

## 🚀 Next Steps

* Complete the coding challenge by handling negative inputs.
* Practise conditional statements and user input.
* Learn how a single artificial neuron calculates an output.
* Gradually build a neural network using Python, starting with the mathematics and logic rather than relying entirely on machine learning libraries.

## 📌 Progress

* [x] Learned basic AI terminology.
* [x] Understood the difference between AI, ML, and DL.
* [x] Created my first rule-based prediction program.
* [x] Documented the program and its test cases.
* [ ] Added validation for negative input.
* [ ] Completed all Day 1 exercises.
