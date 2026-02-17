"""
Docstring for a-Topics.Nested Loop.02_exercise
🏫 Task 7: University Attendance System
Task Instructions:

• Ask how many classes
• For each class, ask how many students
• For each student, ask if present (yes/no)
• Count and print total present students per class
• After all classes, print total present students in university
"""
classes = int(input("Enter the number of classes: "))

total_presences = 0

for i in range(1, classes + 1):
    print(f"\nClasses {i}: ")

    students = int(input("Enter the number of student in this class: "))
    class_present = 0

    for j in range(1, students + 1):
        status = (input(f"Is student {j} present? (yes/no): ")).lower()

        if status == "yes":
            class_present += 1

    print("Total present students in Class", i, "=", class_present)

    total_presences += class_present

print("\nTotal present students in University =", total_presences)