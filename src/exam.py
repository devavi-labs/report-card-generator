from .marks import Marks
from .student import Student


class Exam:
    name: str
    student: Student
    marks = []

    def __init__(self, student: Student):
        self.student = student
        self.name = input("Enter Exam Name: ")

    def take_marks(self):
        has_more = True

        while has_more == True:
            subject = input("Enter Subject: ").strip()
            total_marks = float(input("Enter Total Marks: "))
            obtained_marks = float(input("Enter Obtained Marks: "))

            if obtained_marks > total_marks:
                print("Obtained marks can\"t be greater than total marks")
                continue

            marks = Marks(subject, total_marks, obtained_marks)

            self.marks.append(marks)

            more = input("Have another subject? (Y/N): ")

            if more.lower() == "y":
                continue
            else:
                has_more = False
