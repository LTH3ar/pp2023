class Course:
    def __init__(self):
        self.__id = str("N/A")
        self.__name = str("N/A")
        self.__credit = str("N/A")
        self.__marks = {}

    def get_id(self):
        return self.__id

    def set_id(self, course_id):
        if isinstance(course_id, str):
            self.__id = course_id
        else:
            raise ValueError("Course ID must be a string")

    def get_name(self):
        return self.__name

    def set_name(self, course_name):
        if isinstance(course_name, str):
            self.__name = course_name
        else:
            raise ValueError("Course name must be a string")

    def get_credit(self):
        return self.__credit

    def set_credit(self, course_credit):
        if isinstance(course_credit, str):
            self.__credit = course_credit
        else:
            raise ValueError("Course credit must be a string")

    def input_mark(self, student_id, mark):
        if isinstance(mark, float) and (0.0 <= float(mark) <= 20.0):
            self.__marks[student_id] = mark
        elif str(mark) == "N/A":
            self.__marks[student_id] = "N/A"
        else:
            raise ValueError("Invalid mark")
        #self.__marks[student_id] = mark

    def get_mark(self, student_id):
        return self.__marks.get(student_id)

    def get_full_mark(self):
        return self.__marks