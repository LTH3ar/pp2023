import sys
from input import Input
from output import Output
import math
import curses
import numpy as np
from domains.student import Student

class StudentManagement:
    #init
    def __init__(self):
        self.stdscr = curses.initscr()
        self.student_list = []
        self.course_list = []
        self.mark_list = []
        self.input_funcs = Input(self.student_list, self.course_list, self.mark_list)
        self.output_funcs = Output(self.student_list, self.course_list, self.mark_list)

    def gpa_calculator(self):
        max_point = float(20)
        max_credit = 0
        for credit in self.course_list:
            max_credit += int(credit.get_credit())
        for student in self.student_list:
            gpa_sum = 0
            credits_sum = 0
            for course in self.course_list:
                for mark in self.mark_list:
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
            ('__gpa', np.float32)
        ])

        tmp_gpa = []
        for student in self.student_list:
            tmp_gpa.append(student)

        for i in tmp_gpa:
            if i.get_gpa() == "N/A":
                i.set_gpa(np.nan)
        # Create a list of tuples from the student objects
        gpa_list = [(s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()) for s in tmp_gpa]

        # Convert the list to a structured numpy array
        gpa_arr = np.array(gpa_list, dtype=student_dtype)
        # Sort the array by GPA
        gpa_arr = np.sort(gpa_arr, order='__gpa')
        # re convert to list of class Student
        gpa_list = []
        for s in gpa_arr:
            student_id = s[0]
            student_name = s[1]
            student_dob = s[2]
            student_gpa = s[3]
            gpa_list.append(Student(student_id, student_name, student_dob, student_gpa))

        self.output_funcs.output_students_list_sorted(gpa_list)

    def gpa_ranking_High2Low(self):
        student_dtype = np.dtype([
            ('id', np.str_, 16),
            ('name', np.str_, 16),
            ('dob', np.str_, 10),
            ('__gpa', np.float32)
        ])

        tmp_gpa = []
        for student in self.student_list:
            tmp_gpa.append(student)

        for i in tmp_gpa:
            if i.get_gpa() == "N/A":
                i.set_gpa(np.nan)
        # Create a list of tuples from the student objects
        gpa_list = [(s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()) for s in tmp_gpa]

        # Convert the list to a structured numpy array
        gpa_arr = np.array(gpa_list, dtype=student_dtype)
        # Sort the array by GPA
        gpa_arr = np.sort(gpa_arr, order='__gpa')[::-1]
        # re convert to list of class Student
        gpa_list = []
        for s in gpa_arr:
            student_id = s[0]
            student_name = s[1]
            student_dob = s[2]
            student_gpa = s[3]
            gpa_list.append(Student(student_id, student_name, student_dob, student_gpa))

        self.output_funcs.output_students_list_sorted(gpa_list)

    def option_select(self, input_option):

        if input_option == 1:
            self.input_funcs.add_student()

        elif input_option == 2:
            self.input_funcs.add_course()

        elif input_option == 3:
            self.input_funcs.add_mark()

        elif input_option == 4:
            self.output_funcs.output_students_list()

        elif input_option == 5:
            self.output_funcs.output_courses_list()

        elif input_option == 6:
            self.output_funcs.output_marks_list()

        elif input_option == 7:
            self.stdscr.clear()
            self.stdscr.refresh()
            self.stdscr.addstr(0, 0, "Enter student id: ")
            input_student_id = str(self.stdscr.getstr(1, len("Enter student id: ") + 1, 20))
            self.output_funcs.output_student(input_student_id)

        elif input_option == 8:
            self.stdscr.clear()
            self.stdscr.refresh()
            self.stdscr.addstr(0, 0, "Enter course id: ")
            input_course_id = str(self.stdscr.getstr(1, len("Enter course id: ") + 1, 20))
            self.output_funcs.output_course(input_course_id)

        elif input_option == 9:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Enter student id: ")
            input_student_id = str(self.stdscr.getstr(1, len("Enter student id: ") + 1, 20))
            self.stdscr.addstr(2, 0, "Enter course id: ")
            input_course_id = str(self.stdscr.getstr(3, len("Enter course id: ") + 1, 20))
            self.output_funcs.output_mark(input_student_id, input_course_id)

        elif input_option == 10:
            self.gpa_calculator()

        elif input_option == 11:
            self.gpa_ranking_Low2High()

        elif input_option == 12:
            self.gpa_ranking_High2Low()

        elif input_option == 13:
            self.input_funcs.load_data()

        elif input_option == 14:
            self.output_funcs.export_data()

        elif input_option == 15:
            sys.exit()
        else:
            print("Invalid option")

    def __del__(self):
        curses.endwin()

