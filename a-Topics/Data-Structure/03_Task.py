"""
🔹 Task 3 — TUPLE & SET (Logic-Focused)
🧩 Scenario — Course Enrollment Analyzer
"""
# ----------------------------
# Step 1 — Collect Data
# ----------------------------
print("Enter 6 solution of python course")
python_list = []

for i in range(6):
    name = input(f"Python student {i + 1}: ").strip()
    python_list.append(name)

# Convert list to tuple (immutable)
python_student = tuple(python_list)

print("\nEnter the 6 student for cybersecurity:")
cyber_student = set()

for i in range(6):
    name = input(f"CyberScurity student {i + 1}: ").strip()
    cyber_student.add(name)

# ----------------------------
# Step 2 — Tuple Operations
# ----------------------------
print("\n--- Tuple Analysis (Python Course) ---")

search_name = input("Enter a name to count in python course: ").strip()
count_name = python_student.count(search_name)
print(f"Count of '{search_name}':", count_name)

search_idx_name = input("Enter a name to find index of python course: ")

if search_idx_name in python_student:
    index_position = python_student.index(search_idx_name)
    print(f"Index of '{search_idx_name}':", index_position)
else:
    print(f"'{search_idx_name}' not found in python course.")

# ----------------------------
# Step 3 — Set Operations
# ----------------------------
print("\n ----Set Operation (Cybersecurity Course)---- ")

# Add New student
new_student = input("Enter a new student to add to cybersecurity: ").strip()
cyber_student.add(new_student)

#Remove one student
remove_student = input("Enter a student to remove from cyber course: ").strip()

if remove_student in cyber_student:
    cyber_student.remove(remove_student)
else:
    print("Student not found. Nothing remove.")

# ----------------------------
# Set Theory Operations
# ----------------------------
# Convert tuple to set for operationsc
python_set = set(python_student)

both_course = python_set.intersection(cyber_student)
only_pyhton = python_set.difference(cyber_student)
only_cyber = cyber_student.difference(python_set)
all_student = python_set.union(cyber_student)

# ----------------------------
# Final Output
# ----------------------------
print("\n----- Final Result -----")
print("Python Course Student = ", python_student)
print("CyberScecurity course student = ", cyber_student)

print("\nStudent in both course = ", both_course)
print("Student in ONLY python course = ", python_student)
print("student in ONLY cybersecurity course = ", cyber_student)
print("All combine student = ", all_student)