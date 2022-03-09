"""
    Question 2:
"""
class Student:
    def __init__(self, firstName, lastName, email, allGrades):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.allGrades = allGrades

def main():
    allStudents = []
    with open("students.txt", "r")
        next(studentsFile)
        for line in studentsFile:
            student = Student(splitLine[0], splitLine[1], splitLine[2], splitGrades)
            allStudents.append(student)
    for s in allStudents:
        print(s.firstname)

    allStudents.sort(key = lambda x: x.firstName)
    print("Sorted: \n")
    for s in allStudents:
        print(s.firstName)
main()
