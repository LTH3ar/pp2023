class Student:
    def __init__(self):
        self.__id = str("N/A")
        self.__name = str("N/A")
        self.__dob = str("N/A")
        self.__gpa = str("N/A")

    def get_id(self):
        return self.__id

    def set_id(self, student_id):
        self.__id = student_id

    def get_name(self):
        return self.__name

    def set_name(self, student_name):
        self.__name = student_name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa
