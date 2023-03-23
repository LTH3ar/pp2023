class Mark:
    #init
    def __init__(self, student_id, course_id, mark_mid, mark_final):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark_mid = mark_mid
        self.__mark_final = mark_final

    #setters
    def set_student_id(self, student_id):
        if isinstance(student_id, str) and len(student_id):
            self.__student_id = student_id
        else:
            raise ValueError("Invalid student ID")
    def set_course_id(self, course_id):
        if isinstance(course_id, str) and len(course_id):
            self.__course_id = course_id
        else:
            raise ValueError("Invalid course ID")

    def set_mark_mid(self, mark_mid):
        if isinstance(mark_mid, float) and 0 <= mark_mid <= 20:
            self.__mark_mid = mark_mid
        else:
            raise ValueError("Invalid mark for mid-term exam")

    def set_mark_final(self, mark_final):
        if isinstance(mark_final, float) and 0 <= mark_final <= 20:
            self.__mark_final = mark_final
        else:
            raise ValueError("Invalid mark for final exam")

    #getters
    def get_student_id(self):
        return self.__student_id
    def get_course_id(self):
        return self.__course_id
    def get_mark_mid(self):
        return self.__mark_mid
    def get_mark_final(self):
        return self.__mark_final
