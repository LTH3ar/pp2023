import pickle
import time
import os
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import subprocess

class Output:
    def __init__(self, student_list, course_list, mark_list):
        self.__student_list = student_list
        self.__course_list = course_list
        self.__mark_list = mark_list
        #self.counter = 0

    # getters
    def get_student_list(self):
        return self.__student_list

    def get_course_list(self):
        return self.__course_list

    def get_mark_list(self):
        return self.__mark_list

    # ==================================================================================================
    def output_list(self, lst):
        if isinstance(lst[0], Student):
            for i in lst:
                print("ID: " + str(i.get_id()))
                print("Name: " + str(i.get_name()))
                print("DoB: " + str(i.get_dob()))
                print("GPA: " + str(i.get_gpa()))
                print("\n")
        elif isinstance(lst[0], Course):
            for i in lst:
                print("Course ID: " + str(i.get_id()))
                print("Course Name: " + str(i.get_name()))
                print("Course Credit: " + str(i.get_credit()))
                print("Course Midterm(%): " + str(i.get_mark_mid_portion()))
                print("Course Final(%): " + str(i.get_mark_final_portion()))
                print("\n")
        elif isinstance(lst[0], Mark):
            for i in lst:
                print("Student ID: " + str(i.get_student_id()))
                print("Course ID: " + str(i.get_course_id()))
                print("Mark Mid: " + str(i.get_mark_mid()))
                print("Mark Final: " + str(i.get_mark_final()))
                print("\n")

        else:
            raise Exception("Invalid list")
        input("Press any key to exit")

    def output_students_list(self):
        self.output_list(self.__student_list)

    def output_students_list_sorted(self, lst_sorted):
        self.output_list(lst_sorted)

    def output_courses_list(self):
        self.output_list(self.__course_list)

    def output_marks_list(self):
        self.output_list(self.__mark_list)

    # ==================================================================================================

    def search_list(self, lst, id):
        subprocess.call("clear")
        if isinstance(lst[0], Student):
            for i in lst:
                if i.get_id() == id:
                    print("ID: " + str(i.get_id()))
                    print("Name: " + str(i.get_name()))
                    print("DoB: " + str(i.get_dob()))
                    print("GPA: " + str(i.get_gpa()))
                    print("\n")

        elif isinstance(lst[0], Course):
            for i in lst:
                if i.get_id() == id:
                    print("Course ID: " + str(i.get_id()))
                    print("Course Name: " + str(i.get_name()))
                    print("Course Credit: " + str(i.get_credit()))
                    print("Course Midterm(%): " + str(i.get_mark_mid_portion()))
                    print("Course Final(%): " + str(i.get_mark_final_portion()))
                    print("\n")

        elif isinstance(lst[0], Mark):
            for i in lst:
                if i.get_student_id() == id:
                    print("Student ID: " + str(i.get_student_id()))
                    print("Course ID: " + str(i.get_course_id()))
                    print("Mark Mid: " + str(i.get_mark_mid()))
                    print("Mark Final: " + str(i.get_mark_final()))
                    print("\n")

        else:
            raise Exception("Invalid list")
        input("Press any key to exit")

    def output_student(self, student_id):
        self.search_list(self.__student_list, student_id)

    def output_course(self, course_id):
        self.search_list(self.__course_list, course_id)

    def output_mark_multiple(self, id):
        self.search_list(self.__mark_list, id)

    def output_mark(self, student_id, course_id):
        subprocess.call("clear")
        for i in self.__mark_list:
            if i.get_course_id() == course_id and i.get_student_id() == student_id:
                print("Student ID: " + str(i.get_student_id()))
                print("Course ID: " + str(i.get_course_id()))
                print("Mark Mid: " + str(i.get_mark_mid()))
                print("Mark Final: " + str(i.get_mark_final()))
                print("\n")
        input("Press any key to exit")

    # ==================================================================================================
    def List2File(self, filename, lst):
        with open(filename, "wb") as file:
            pickle.dump(lst, file)

    def export_data(self):
        subprocess.call("clear")
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.List2File(filename1, self.__student_list)
        self.List2File(filename2, self.__course_list)
        self.List2File(filename3, self.__mark_list)
        print("Export data successfully!")
        input("Press any key to exit")

    def export_data_daemon(self):
        while True:
            #self.counter += 1 # for testing
            time.sleep(1)
            filename1 = "students_data_tmp.dt"
            filename2 = "courses_data_tmp.dt"
            filename3 = "marks_data_tmp.dt"
            self.List2File(filename1, self.__student_list)
            self.List2File(filename2, self.__course_list)
            self.List2File(filename3, self.__mark_list)

    def export_data_rename(self):
        subprocess.call("clear")
        filename1 = "students_data_tmp.dt"
        filename2 = "courses_data_tmp.dt"
        filename3 = "marks_data_tmp.dt"
        os.rename(filename1, "students_data.dt")
        os.rename(filename2, "courses_data.dt")
        os.rename(filename3, "marks_data.dt")
        print("Export data successfully!")
        input("Press any key to exit")
    # ==================================================================================================