
# Day 1: My First Prediction Program

study_hours = int(input("Enter the number of hours you studied: "))

if study_hours < 0:
    prediction = "Invalid input"
elif study_hours >= 4:
    prediction = "Pass"
else:
    prediction = "Fail"

print("\n--- Prediction Result ---")
print("Study Hours:", study_hours)
print("Prediction result:", prediction)