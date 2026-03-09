from student import Student


class Course_group:

    def __init__(self, student: Student, classmates: list[Student]):
        self.student = student
        self.classmates = classmates
