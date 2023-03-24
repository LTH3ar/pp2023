import sys
from input import Input
from output import Output
import math
import subprocess
import threading
import os
import time
import numpy as np
from domains.student import Student


class StudentManagement:
    #init
    def __init__(self):
        self.__student_list = []
        self.__course_list = []
        self.__mark_list = []
        self.input_funcs = Input(self.__student_list, self.__course_list, self.__mark_list)
        self.output_funcs = Output(self.__student_list, self.__course_list, self.__mark_list)
        self.background_thread_run()

    def background_thread_run(self):
        self.background_thread = threading.Thread(target=self.output_funcs.export_data_daemon, daemon=True)
        self.background_thread.start()

    def gpa_calculator(self):
        max_point = float(20)
        max_credit = 0
        for credit in self.__course_list:
            max_credit += int(credit.get_credit())
        for student in self.__student_list:
            gpa_sum = 0
            credits_sum = 0
            for course in self.__course_list:
                for mark in self.__mark_list:
                    if (course.get_id() == mark.get_course_id()
                            and mark.get_student_id() == student.get_id()):
                        mark_mid = ((float(mark.get_mark_mid()) / max_point)
                                    * ((float(course.get_mark_mid_portion()) / 100) * max_point))
                        # floor mark_mid to 1 decimal places
                        mark_mid = math.floor(mark_mid * 10) / 10

                        mark_final = ((float(mark.get_mark_final()) / max_point)
                                      * ((float(course.get_mark_final_portion()) / 100) * max_point))
                        # floor mark_final to 1 decimal places
                        mark_final = math.floor(mark_final * 10) / 10

                        mark_full = mark_mid + mark_final
                        # floor gpa to 1 decimal places
                        mark_full = math.floor(mark_full * 10) / 10

                        gpa_sum += mark_full * float(course.get_credit())
                        credits_sum += int(course.get_credit())
                        print(f"gpa_sum: {gpa_sum}")
                        print(f"credits_sum: {credits_sum}")

            if credits_sum < max_credit:
                gpa = "N/A"
            else:
                gpa = gpa_sum / credits_sum
                # floor gpa to 1 decimal places
                gpa = math.floor(gpa * 10) / 10
            student.set_gpa(gpa)
        print("GPA Calculator Done")
        input("Press any key to exit")

    def gpa_ranking_Low2High(self):
        student_dtype = np.dtype([
            ('id', np.str_, 16),
            ('name', np.str_, 16),
            ('dob', np.str_, 10),
            ('gpa', np.float32)
        ])

        tmp_gpa = []
        for student in self.__student_list:
            tmp_gpa.append(Student(student.get_id(),
                                   student.get_name(),
                                   student.get_dob(),
                                   student.get_gpa()))

        for i in tmp_gpa:
            if i.get_gpa() == "N/A":
                i.set_gpa(np.nan)
        # Create a list of tuples from the student objects
        gpa_list = [(s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()) for s in tmp_gpa]

        # Convert the list to a structured numpy array
        gpa_arr = np.array(gpa_list, dtype=student_dtype)
        # Sort the array by GPA
        gpa_arr = np.sort(gpa_arr, order='gpa')
        # re convert to list of class Student
        tmp_gpa.clear()
        for s in gpa_arr:
            student_id = s[0]
            student_name = s[1]
            student_dob = s[2]
            student_gpa = s[3]
            tmp_gpa.append(Student(student_id, student_name, student_dob, student_gpa))

        self.output_funcs.output_students_list_sorted(tmp_gpa)

    def gpa_ranking_High2Low(self):
        student_dtype = np.dtype([
            ('id', np.str_, 16),
            ('name', np.str_, 16),
            ('dob', np.str_, 10),
            ('gpa', np.float32)
        ])

        tmp_gpa = []
        for student in self.__student_list:
            tmp_gpa.append(Student(student.get_id(),
                                   student.get_name(),
                                   student.get_dob(),
                                   student.get_gpa()))

        for i in tmp_gpa:
            if i.get_gpa() == "N/A":
                i.set_gpa(np.nan)
        # Create a list of tuples from the student objects
        gpa_list = [(s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()) for s in tmp_gpa]

        # Convert the list to a structured numpy array
        gpa_arr = np.array(gpa_list, dtype=student_dtype)
        # Sort the array by GPA
        gpa_arr = np.sort(gpa_arr, order='gpa')[::-1]
        # re convert to list of class Student
        tmp_gpa.clear()
        for s in gpa_arr:
            student_id = s[0]
            student_name = s[1]
            student_dob = s[2]
            student_gpa = s[3]
            tmp_gpa.append(Student(student_id, student_name, student_dob, student_gpa))

        self.output_funcs.output_students_list_sorted(tmp_gpa)

    def search_student(self):
        subprocess.call("clear")
        input_student_id = str(input("Enter student id"))
        self.output_funcs.output_student(input_student_id)

    def search_course(self):
        subprocess.call("clear")
        input_course_id = str(input("Enter course id: "))
        self.output_funcs.output_course(input_course_id)

    def search_mark_single(self):
        subprocess.call("clear")
        input_student_id = str(input("Enter student id: "))
        input_course_id = str(input("Enter course id: "))
        self.output_funcs.output_mark(input_student_id, input_course_id)

    def search_mark_all(self):
        subprocess.call("clear")
        input_id = str(input("Enter course/student id: "))
        self.output_funcs.output_mark_multiple(input_id)

    def exit_func(self):
        if os.path.exists("students_data_tmp.dt"):
            os.remove("students_data_tmp.dt")
        if os.path.exists("courses_data_tmp.dt"):
            os.remove("courses_data_tmp.dt")
        if os.path.exists("marks_data_tmp.dt"):
            os.remove("marks_data_tmp.dt")
        sys.exit()



    def option_select(self, input_option):
        options = [
            self.input_funcs.manage_student,
            self.input_funcs.manage_course,
            self.input_funcs.manage_mark,
            self.output_funcs.output_students_list,
            self.output_funcs.output_courses_list,
            self.output_funcs.output_marks_list,
            self.search_student,
            self.search_course,
            self.search_mark_single,
            self.search_mark_all,
            self.gpa_calculator,
            self.gpa_ranking_Low2High,
            self.gpa_ranking_High2Low,
            self.input_funcs.load_data,
            self.output_funcs.export_data_rename,
            self.output_funcs.export_data,
            self.exit_func
        ]

        for i, option in enumerate(options):
            if i == input_option:
                option()
                break

