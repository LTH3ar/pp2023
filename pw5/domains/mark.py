class Mark:
    #init
    def __init__(self, student_id, course_id, mark_mid, mark_final):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark_mid = mark_mid
        self.__mark_final = mark_final

    #setters
    def set_student_id(self, student_id):
        self.__student_id = student_id
    def set_course_id(self, course_id):
        self.__course_id = course_id
    def set_mark_mid(self, mark_mid):
        self.__mark_mid = mark_mid
    def set_mark_final(self, mark_final):
        self.__mark_final = mark_final

    #getters
    def get_student_id(self):
        return self.__student_id
    def get_course_id(self):
        return self.__course_id
    def get_mark_mid(self):
        return self.__mark_mid
    def get_mark_final(self):
        return self.__mark_final