# ==================================================
# MINI SCHOOL MANAGEMENT SYSTEM
# ==================================================

# ----------------------------
# STEP 1 — Subjects (Tuple)
# ----------------------------
subjects = ("Pyhton", "CyberSecurity", "Networking", "Ai")
print("Available subject:")

for subject in subjects:
    print("-", subject)

# ----------------------------
# STEP 2 — Student Registration
# ----------------------------
students = set()
print("\nEnter 5 student name:")

for i in range(5):
    names = input(f"Student {i+1}: ")
    cleaned_name = names.strip().title()
    # Add to set (automatically prevents duplicates)
    students.add(cleaned_name)

# Display registed student
print("\nRegisted student:")
for student in students:
    print("-", student)

# ----------------------------
# STEP 3 — Student Marks (Dictionary + List)
# ----------------------------
student_record = {}

print("\nEnter marks for each student:")

for student in students:
    marks = []
    print(f"\nEntering marks for {student}: ")

    for subject in subjects:
        mark = int(input(f"{subject} mark: "))
        marks.append(mark)

    student_record[student] = marks

# ----------------------------
# STEP 4 — Analysis Section
# ----------------------------
averages = {}
top_student = None
highest_average = 0
high_achivers = []
all_marks = set()

for student, marks in student_record.items():
    average = sum(marks) / len(marks)
    averages[student] = average

    # Track Top Performer 
    if average > highest_average:
        highest_average = average
        top_student = student

    # Track High Achiver
    if average > 80:
        high_achivers.append(student)

    # Collect Unique mark
    all_marks.update(marks)

# ----------------------------
# STEP 5 — Final Output
# ----------------------------

print("\n==============================")
print("FINAL REPORT")
print("==============================")

print("\nSubject:",subject)

print("\nStudent Records:")
for student, marks in student_record.items():
    print(f"{student} --> {marks}")

print("\nAverage Marks:")
for student, avg in averages.items():
    print(f"{student}: {avg:.2f}")

print("\nTop Performer:")
print(top_student, f"with average {highest_average:.2f}")

print("High achivers (Avg > 80):")
for student in high_achivers:
    print("-", student)

print("All Unique marks:", all_marks)