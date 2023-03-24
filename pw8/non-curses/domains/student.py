import numpy as np
class Student:
    #init
    def __init__(self, student_id, student_name, dob, gpa):
        self.__id = student_id
        self.__name = student_name
        self.__dob = dob
        self.__gpa = gpa

    #setters
    def set_id(self, student_id):
        if isinstance(student_id, str) and len(student_id) > 0:
            self.__id = student_id
        else:
            raise ValueError("Invalid student ID")
    def set_name(self, student_name):
        if isinstance(student_name, str) and len(student_name) > 0:
            self.__name = student_name
        else:
            raise ValueError("Invalid student name")
    def set_dob(self, dob):
        if isinstance(dob, str) and len(dob) > 0:
            self.__dob = dob
        else:
            raise ValueError("Invalid date of birth")
    def set_gpa(self, gpa):
        if isinstance(gpa, float) and 0.0 <= gpa <= 20.0:
            self.__gpa = gpa
        elif gpa == "N/A" or gpa is np.nan or gpa is None:
            self.__gpa = gpa
        else:
            raise ValueError("Invalid GPA")

    #getters
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_gpa(self):
        return self.__gpa