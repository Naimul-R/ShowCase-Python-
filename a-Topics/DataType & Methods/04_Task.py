"""
🧩 Scenario — Employee Management System
"""
# ----------------------------
# Step 1 — Create Dictionary
# ----------------------------
employees = {}

print("Enter 5 employee names and selary.")

for i in range(5):
    name = input(f"Employee {i+1} Name: ").strip()
    selary = int(input(f"Employee {i+1} Selary: "))
    employees[name] = selary

# ----------------------------
# Step 2A — Retrieve Data
# ----------------------------
print("\n---- Retrieve Selary ----")

search_name = input("Enter employee name to retrive selary: ").strip()
selary = employees.get(search_name)

if selary is not None:
    print(f"Selary of {search_name}: {selary}")
else:
    print("Employee not found.")

# ----------------------------
# Step 2B — Update Data
# ----------------------------
print("\n---- Update Selary ----")

update_name = input("Enter employee to update selary: ").strip()
new_selary = int(input("Enter new selary: "))

if update_name in employees:
    employees.update({update_name: new_selary})
    print("Selary update successfully.")
else:
    print("Employee not found. Update not performed.")

# ----------------------------
# Step 2C — Add If Not Exists
# ----------------------------
print("\n---- Add Employee If not exits ----")

default_name = input('Enter employee name to add default selary: ').strip()
employees.setdefault(default_name, 30000)

print("Operation Completed.")

# ----------------------------
# Step 2D — Remove Operations
# ----------------------------
print("\n---- Remove Employee ----")

remove_name = input("Enter employee name to remove: ").strip()

if remove_name in employees:
    removed_selary = employees.pop(remove_name)
    print(f"Removed {remove_name} with selary {removed_selary}.")
else:
    print("Employee not found. Nothing removed.")

# Remove last inserted employee safely
if employees:
    last_removed = employees.popitem()
    print("Last Inserted employee remove: ",last_removed)
else:
    print("dictonary is empty. Nothing to pop.")

# ----------------------------
# Step 3 — Display Information
# ----------------------------
print("\n---- Final Employee Data ----")

print("Employee Name = ", list(employees.keys()))
print("Employee Selary = ", list(employees.value()))
print("Employee Record = ", list(employees.item()))
print("Final Dictonary State = ", employees)