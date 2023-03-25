import sys
from input import Input
from output import Output
import math
import curses
import threading
import os
import time
import numpy as np
from domains.student import Student


class StudentManagement:
    #init
    def __init__(self, stdscr_main):
        self.stdscr = stdscr_main
        self.__student_list = []
        self.__course_list = []
        self.__mark_list = []
        self.input_funcs = Input(self.__student_list, self.__course_list, self.__mark_list, self.stdscr)
        self.output_funcs = Output(self.__student_list, self.__course_list, self.__mark_list, self.stdscr)
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
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 0, "Enter student id: ")
        input_student_id = (self.stdscr.getstr(0, len("Enter student id: ") + 1, 20))
        self.output_funcs.output_student(input_student_id.decode("utf-8"))

    def search_course(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 0, "Enter course id: ")
        input_course_id = (self.stdscr.getstr(0, len("Enter course id: ") + 1, 20))
        self.output_funcs.output_course(input_course_id.decode("utf-8"))

    def search_mark_single(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 0, "Enter student id: ")
        input_student_id = (self.stdscr.getstr(0, len("Enter student id: ") + 1, 20))
        self.stdscr.addstr(2, 0, "Enter course id: ")
        input_course_id = (self.stdscr.getstr(2, len("Enter course id: ") + 1, 20))
        self.output_funcs.output_mark(input_student_id.decode("utf-8"), input_course_id.decode("utf-8"))

    def search_mark_all(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 0, "Enter course/student id: ")
        input_id = (self.stdscr.getstr(0, len("Enter course/student id: ") + 1, 20))
        self.output_funcs.output_mark_multiple(input_id.decode("utf-8"))

    def exit_func(self):
        if os.path.exists("students_data_tmp.json"):
            os.remove("students_data_tmp.json")
        if os.path.exists("courses_data_tmp.json"):
            os.remove("courses_data_tmp.json")
        if os.path.exists("marks_data_tmp.json"):
            os.remove("marks_data_tmp.json")
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

    def __del__(self):
        curses.endwin()

