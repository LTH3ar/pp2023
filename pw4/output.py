from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import json

class Output:
    def __init__(self, student_list, course_list, mark_list):
        self.__student_list = student_list
        self.__course_list = course_list
        self.__mark_list = mark_list

    # getters
    def get_student_list(self):
        return self.__student_list

    def get_course_list(self):
        return self.__course_list

    def get_mark_list(self):
        return self.__mark_list

    def output_students_list(self):
        for i in self.__student_list:
            print("\nID: " + str(i.get_id())
                  + "\nName: " + str(i.get_name())
                  + "\nDoB: " + str(i.get_dob())
                  + "\nGPA: " + str(i.get_gpa())
                  )

    def output_courses_list(self):
        for i in self.__course_list:
            print("\nID: " + str(i.get_id())
                  + "\nName: " + str(i.get_name())
                  + "\nDoB: " + str(i.get_credit())
                  + "\nMid_%: " + str(i.get_mark_mid_portion())
                  + "\nFinal_%: " + str(i.get_mark_final_portion())
                  )

    def output_marks_list(self):
        for i in self.__mark_list:
            print("\nStudent ID: " + str(i.get_student_id())
                  + "\nCourse ID: " + str(i.get_course_id())
                  + "\nMid: " + str(i.get_mark_mid())
                  + "\nFinal: " + str(i.get_mark_final())
                  )

    def output_student(self, student_id):
        for i in self.__student_list:
            if i.get_id() == student_id:
                print("\nID: " + str(i.get_id())
                      + "\nName: " + str(i.get_name())
                      + "\nDoB: " + str(i.get_dob())
                      + "\nGPA: " + str(i.get_gpa())
                      )

    def output_course(self, course_id):
        for i in self.__course_list:
            if i.get_id() == course_id:
                print("\nID: " + str(i.get_id())
                      + "\nName: " + str(i.get_name())
                      + "\nDoB: " + str(i.get_credit())
                      + "\nMid_%: " + str(i.get_mark_mid_portion())
                      + "\nFinal_%: " + str(i.get_mark_final_portion())
                      )

    def output_mark(self, student_id, course_id):
        for i in self.__mark_list:
            if i.get_course_id() == course_id and i.get_student_id() == student_id:
                print("\nCourse ID: " + str(i.get_course_id())
                    + "\nStudent ID: " + str(i.get_student_id())
                    + "\nMid: " + str(i.get_mark_mid())
                    + "\nFinal: " + str(i.get_mark_final())
                    )

    def List2File(self, filename, lst): #write to json file
        with open(filename, "w") as file:
            json.dump(lst, file, default=lambda o: o.__dict__, indent=4)

    def export_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.List2File(filename1, self.__student_list)
        self.List2File(filename2, self.__course_list)
        self.List2File(filename3, self.__mark_list)