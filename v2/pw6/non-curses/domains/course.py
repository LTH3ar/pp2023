class Course:
    #init
    def __init__(self, course_id, course_name, course_credit, course_mark_mid_portion, course_mark_final_portion):
        self.__id = course_id
        self.__name = course_name
        self.__credit = course_credit
        self.__mark_mid_portion = course_mark_mid_portion
        self.__mark_final_portion = course_mark_final_portion

    #setters
    def set_id(self, course_id):
        self.__id = course_id
    def set_name(self, course_name):
        self.__name = course_name
    def set_credit(self, course_credit):
        self.__credit = course_credit
    def set_mark_mid_portion(self, course_mark_mid_portion):
        self.__mark_mid_portion = course_mark_mid_portion
    def set_mark_final_portion(self, course_mark_final_portion):
        self.__mark_final_portion = course_mark_final_portion

    #getters
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit
    def get_mark_mid_portion(self):
        return self.__mark_mid_portion
    def get_mark_final_portion(self):
        return self.__mark_final_portion