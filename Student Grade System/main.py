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


#Create a main function
def main():
    while True:
        print("\nStudent Grade Managment System.")
        print("1. Add Studnet.")
        print("2. Update Student.")
        print("3. Delete Student.")
        print("4. View Student.")
        print("5. Exit.")

        choice = int(input("Enter Your Choice = "))

        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student's grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_student()
        
        elif choice == 5:
            print("Closing the program....")
            break 

        else:
            print("Invalid choice!")

main()