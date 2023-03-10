class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__dob = None
        self.__gpa = "N/A"

    def get_id(self):
        return self.__id

    def set_id(self, student_id):
        if isinstance(student_id, str) and len(student_id) > 0:
            self.__id = student_id
        else:
            raise ValueError("Invalid student ID")

    def get_name(self):
        return self.__name

    def set_name(self, student_name):
        if isinstance(student_name, str) and len(student_name) > 0:
            self.__name = student_name
        else:
            raise ValueError("Invalid student name")

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        if isinstance(dob, str) and len(dob) > 0:
            self.__dob = dob
        else:
            raise ValueError("Invalid date of birth")

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if isinstance(gpa, float) and 0.0 <= gpa <= 20.0:
            self.__gpa = gpa
        elif gpa == "N/A":
            self.__gpa = gpa
        else:
            raise ValueError("Invalid GPA")
