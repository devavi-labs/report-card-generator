from .marks import Marks
from .student import Student
from .exam import Exam


class ReportCard:
    student_name: str
    standard: int
    roll_no: int
    exam_name: str
    marks: list

    def __init__(self, student: Student, exam: Exam):
        self.student_name = student.full_name
        self.standard = student.standard
        self.roll_no = student.roll_no
        self.exam_name = exam.name
        self.marks = exam.marks

    def generate(self):

        total_gp = 0
        marks = []

        for x in self.marks:
            total_gp += x.grade_point
            marks.append(x.get_marks())

        cgpa = total_gp / len(self.marks)

        generated_report_card: dict = {
            "student": {
                "full_name": self.student_name,
                "standard": self.standard,
                "roll_no": self.roll_no
            },
            "exam": self.exam_name,
            "marks": marks,
            "cgpa": cgpa,
            "result": "PASS" if cgpa > 4 else "FAIL"
        }

        return generated_report_card
