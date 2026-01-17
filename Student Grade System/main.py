#Initialising dictonary
student_grade = { }

#Add a new student
def add_student (name, grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")


#Update a student
def update_student (name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")


#Delete a student 
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} is not found!")


#View all student
def display_all_student():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No student found/added.")
