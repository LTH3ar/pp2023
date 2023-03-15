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
        if isinstance(course_id, str) and len(course_id) > 0:
            self.__id = course_id
        else:
            raise ValueError("Course ID must be a string")
    def set_name(self, course_name):
        if isinstance(course_name, str) and len(course_name) > 0:
            self.__name = course_name
        else:
            raise ValueError("Course name must be a string")
    def set_credit(self, course_credit):
        if isinstance(course_credit, int) and (0 < course_credit <= 4):
            self.__credit = course_credit
        else:
            raise ValueError("Course credit must be a string")
    def set_mark_mid_portion(self, course_mark_mid_portion):
        if isinstance(course_mark_mid_portion, int) and (0 < course_mark_mid_portion <= 100):
            self.__mark_mid_portion = course_mark_mid_portion
        else:
            raise ValueError("Course mark mid portion must be a integer")
    def set_mark_final_portion(self, course_mark_final_portion):
        if isinstance(course_mark_final_portion, int) and (0 < course_mark_final_portion <= 100):
            self.__mark_final_portion = course_mark_final_portion
        else:
            raise ValueError("Course mark final portion must be a integer")

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