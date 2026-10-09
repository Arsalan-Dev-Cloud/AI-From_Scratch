
# Day 1: My First Prediction Program

study_hours = int(input("Enter the number of hours you studied: "))

if study_hours >= 4:
    prediction = "Pass"
else:
    prediction = "Fail"

print("\n--- Prediction Result ---")
print("Study hours:", study_hours)
print("Predicted result:", prediction)