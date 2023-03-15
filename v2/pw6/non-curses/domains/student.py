class Student:
    #init
    def __init__(self, student_id, student_name, dob, gpa):
        self.__id = student_id
        self.__name = student_name
        self.__dob = dob
        self.__gpa = gpa

    #setters
    def set_id(self, student_id):
        self.__id = student_id
    def set_name(self, student_name):
        self.__name = student_name
    def set_dob(self, dob):
        self.__dob = dob
    def set_gpa(self, gpa):
        self.__gpa = gpa

    #getters
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_gpa(self):
        return self.__gpa