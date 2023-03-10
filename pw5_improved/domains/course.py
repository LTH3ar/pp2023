class Course:
    def __init__(self):
        self.__id = str("N/A")
        self.__name = str("N/A")
        self.__credit = str("N/A")
        self.__marks = {}

    def get_id(self):
        return self.__id

    def set_id(self, course_id):
        self.__id = course_id

    def get_name(self):
        return self.__name

    def set_name(self, course_name):
        self.__name = course_name

    def get_credit(self):
        return self.__credit

    def set_credit(self, course_credit):
        self.__credit = course_credit

    def input_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_mark(self, student_id):
        return self.__marks[student_id]
