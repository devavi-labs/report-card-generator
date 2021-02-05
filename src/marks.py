

class Marks:
    subject: str
    total_marks: float
    obtained_marks: float
    grade_point: int

    def __init__(self, subject, total_marks, obtained_marks):
        self.subject = subject
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks
        self.grade_point = self.get_grade_point(total_marks, obtained_marks)

    def get_marks(self):
        return {
            "subject": self.subject,
            "total_marks": self.total_marks,
            "obtained_marks": self.obtained_marks,
            "grade_point": self.grade_point
        }

    def get_grade_point(_, total_marks: float, obtained_marks: float):
        part = total_marks // 10
        gp = 4

        if obtained_marks > part * 9:
            gp = 10
        elif obtained_marks > part * 8:
            gp = 9
        elif obtained_marks > part * 7:
            gp = 8
        elif obtained_marks > part * 6:
            gp = 7
        elif obtained_marks > part * 5:
            gp = 6
        elif obtained_marks > part * 4:
            gp = 5
        else:
            gp = 4

        return gp
