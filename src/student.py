class Student:
    full_name: str
    standard: str
    roll_no: str

    def __init__(self):
        self.full_name = input("Enter Full Name: ").strip()
        self.standard = input("Enter Standard: ").strip()
        self.roll_no = input("Enter Roll No.: ").strip()
