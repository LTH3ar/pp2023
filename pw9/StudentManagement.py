import sys
from input import Input
from output import Output
import math
import tkinter as tk
import threading
import os
import numpy as np
from domains.student import Student


class StudentManagement:
    #init
    def __init__(self, menu_window):
        self.__student_list = []
        self.__course_list = []
        self.__mark_list = []
        self.menu_window = menu_window
        self.input_funcs = Input(self.__student_list,
                                 self.__course_list,
                                 self.__mark_list,
                                 self.menu_window)
        self.output_funcs = Output(self.__student_list,
                                   self.__course_list,
                                   self.__mark_list,
                                   self.menu_window)
        self.background_thread_run()

    def background_thread_run(self):
        self.thread_background = threading.Thread(target=self.output_funcs.export_data_daemon, daemon=True)
        self.thread_background.start()

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
        sm_window = tk.Toplevel(self.menu_window)
        sm_window.title("Student search")
        sm_window.geometry("500x500")
        sm_window.configure(bg="white")
        sm_window.resizable(True, True)
        lbl_input_student_id = tk.Label(sm_window, text="Enter student id: ")
        lbl_input_student_id.grid(row=0, column=0)
        txt_input_student_id = tk.Entry(sm_window, width=20)
        txt_input_student_id.grid(row=1, column=0)
        # submits button
        btn_submit = tk.Button(sm_window,
                               text="Submit",
                               command=lambda: self.output_funcs.output_student(
                                   txt_input_student_id.get()
                               )
                               )
        btn_submit.grid(row=2, column=0)
        sm_window.protocol("WM_DELETE_WINDOW", sm_window.destroy)
        txt_input_student_id.delete(0, tk.END)

    def search_course(self):
        sm_window = tk.Toplevel(self.menu_window)
        sm_window.title("Course search")
        sm_window.geometry("500x500")
        sm_window.configure(bg="white")
        sm_window.resizable(True, True)
        lbl_input_course_id = tk.Label(sm_window, text="Enter course id: ")
        lbl_input_course_id.grid(row=0, column=0)
        txt_input_course_id = tk.Entry(sm_window, width=20)
        txt_input_course_id.grid(row=1, column=0)
        # submits button
        btn_submit = tk.Button(sm_window,
                               text="Submit",
                               command=lambda: self.output_funcs.output_course(
                                   txt_input_course_id.get()
                               )
                               )
        btn_submit.grid(row=2, column=0)
        sm_window.protocol("WM_DELETE_WINDOW", sm_window.destroy)
        txt_input_course_id.delete(0, tk.END)

    def search_mark_single(self):
        sm_window = tk.Toplevel(self.menu_window)
        sm_window.title("Mark search")
        sm_window.geometry("500x500")
        sm_window.configure(bg="white")
        sm_window.resizable(True, True)
        lbl_input_student_id = tk.Label(sm_window, text="Enter student id: ")
        lbl_input_student_id.grid(row=0, column=0)
        txt_input_student_id = tk.Entry(sm_window, width=20)
        txt_input_student_id.grid(row=1, column=0)

        lbl_input_course_id = tk.Label(sm_window, text="Enter course id: ")
        lbl_input_course_id.grid(row=2, column=0)
        txt_input_course_id = tk.Entry(sm_window, width=20)
        txt_input_course_id.grid(row=3, column=0)
        # submits button
        btn_submit = tk.Button(sm_window,
                               text="Submit",
                               command=lambda: self.output_funcs.output_mark(
                                   txt_input_student_id.get(),
                                   txt_input_course_id.get()
                               )
                               )
        btn_submit.grid(row=4, column=0)
        sm_window.protocol("WM_DELETE_WINDOW", sm_window.destroy)
        txt_input_student_id.delete(0, tk.END)
        txt_input_course_id.delete(0, tk.END)

    def search_mark_all(self):
        sm_window = tk.Toplevel(self.menu_window)
        sm_window.title("Mark search(full)")
        sm_window.geometry("500x500")
        sm_window.configure(bg="white")
        sm_window.resizable(True, True)
        lbl_input_id = tk.Label(sm_window, text="Enter course/student id: ")
        lbl_input_id.grid(row=0, column=0)
        txt_input_id = tk.Entry(sm_window, width=20)
        txt_input_id.grid(row=1, column=0)
        # submits button
        btn_submit = tk.Button(sm_window,
                               text="Submit",
                               command=lambda: self.output_funcs.output_mark_multiple(
                                   txt_input_id.get()
                               )
                               )
        btn_submit.grid(row=2, column=0)
        sm_window.protocol("WM_DELETE_WINDOW", sm_window.destroy)
        txt_input_id.delete(0, tk.END)

    def exit_func(self):
        if os.path.exists("students_data_tmp.dt"):
            os.remove("students_data_tmp.dt")
        if os.path.exists("courses_data_tmp.dt"):
            os.remove("courses_data_tmp.dt")
        if os.path.exists("marks_data_tmp.dt"):
            os.remove("marks_data_tmp.dt")
        # sys.exit()
        self.menu_window.destroy()


    def option_select(self, input_option):
        #rewrite the option list to tuple
        options = [
            self.input_funcs.input_student,
            self.input_funcs.input_course,
            self.input_funcs.input_mark,
            self.output_funcs.output_students_list,
            self.output_funcs.output_courses_list,
            self.output_funcs.output_marks_list,
            self.search_student,
            self.search_course,
            self.search_mark_single,
            self.search_mark_all,
            self.gpa_calculator,
            self.gpa_ranking_High2Low,
            self.gpa_ranking_Low2High,
            self.input_funcs.load_data,
            self.output_funcs.export_data_rename,
            self.output_funcs.export_data,
            self.exit_func
        ]

        for i, option in enumerate(options):
            if i == input_option:
                option()
                break