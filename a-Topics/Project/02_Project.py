class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, mark):
        self.grades.append(mark)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def result(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"
        
    def report(self):
        print(f"{self.name} [{self.student_id}] | Avg: {self.average():.1f} | Grade: {self.result()}")

# --- testing ---
s1 = Student("Rahim", "S001")
s1.add_grade(75)
s1.add_grade(88)
s1.add_grade(62)
s1.report()

s2 = Student("Karim", "S002")
s2.add_grade(45)
s2.add_grade(38)
s2.add_grade(50)
s2.report()

s3 = Student("Nadia", "S003")
s3.add_grade(92)
s3.add_grade(85)
s3.add_grade(90)
s3.report()