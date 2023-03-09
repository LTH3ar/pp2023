class Course:
    def __init__(self, course_id, course_name, course_credit):
        self.id = course_id
        self.name = course_name
        self.credit = course_credit
        self.marks = {}

    def input_mark(self, student_id, mark):
        self.marks[student_id] = mark
