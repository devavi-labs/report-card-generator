from .report_card import ReportCard
from .student import Student
from .exam import Exam
import json


def main():
    student = Student()
    exam = Exam(student)

    exam.take_marks()

    report_card = ReportCard(student, exam)

    generated_report_card = report_card.generate()
    print(f'Report Card for student {student.full_name} is generated.')

    file = 'generated/' + student.full_name.split(
        ' ')[0].lower().strip(' .')
    ext = 'report_card.json'
    not_written_yet = True
    suffix = 0

    while not_written_yet == True:
        try:
            path = f'{file}_{suffix}_{ext}' if suffix > 0 else f'{file}_{ext}'
            with open(path, 'x') as output:
                json.dump(generated_report_card, output, indent=4)
                print(f'Report Card is saved at {path}')
                not_written_yet = False
        except FileExistsError:
            suffix += 1
            continue
