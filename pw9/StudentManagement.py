import sys

from input import Input
from output import Output
import math
import tkinter as tk
import threading
import os


class StudentManagement:
    #init
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.mark_list = []
        self.input_funcs = Input(self.student_list, self.course_list, self.mark_list, self.sm_window)
        self.output_funcs = Output(self.student_list, self.course_list, self.mark_list, self.sm_window)
        threading.Thread(target=self.output_funcs.export_data_daemon, daemon=True).start()

    def gpa_calculator(self):
        max_point = float(20)
        for student in self.student_list:
            gpa_sum = 0
            credits_sum = 0
            for course in self.course_list:
                for mark in self.mark_list:
                    if course.get_id() == mark.get_course_id() and mark.get_student_id() == student.get_id():
                        mark_mid = (mark.get_mark_mid() / max_point) * ((course.get_mark_mid_portion() / 100) * max_point)
                        # floor mark_mid to 1 decimal places
                        mark_mid = math.floor(mark_mid * 10) / 10

                        mark_final = (mark.get_mark_final() / max_point) * ((course.get_mark_final_portion() / 100) * max_point)
                        # floor mark_final to 1 decimal places
                        mark_final = math.floor(mark_final * 10) / 10

                        mark_full = mark_mid + mark_final
                        # floor gpa to 1 decimal places
                        mark_full = math.floor(mark_full * 10) / 10

                        gpa_sum += mark_full * course.get_credit()
                        credits_sum += course.get_credit()

            gpa = gpa_sum / credits_sum
            # floor gpa to 1 decimal places
            gpa = math.floor(gpa * 10) / 10
            student.set_gpa(gpa)

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
            sm_window = tk.Toplevel()
            #rewrite the above code to use tkinter
            sm_window.title("Student search")
            sm_window.geometry("500x500")
            sm_window.configure(bg="white")
            sm_window.resizable(False, False)
            lbl_input_student_id = tk.Label(sm_window, text="Enter student id: ")
            lbl_input_student_id.grid(row=0, column=0)
            txt_input_student_id = tk.Entry(sm_window, width=20)
            txt_input_student_id.grid(row=1, column=0)
            input_student_id = txt_input_student_id.get()
            #submits button
            btn_submit = tk.Button(sm_window, text="Submit", command=lambda: self.output_funcs.output_student(input_student_id))
            btn_submit.grid(row=2, column=0)

        elif input_option == 8:
            sm_window = tk.Toplevel()
            sm_window.title("Course search")
            sm_window.geometry("500x500")
            sm_window.configure(bg="white")
            sm_window.resizable(False, False)
            lbl_input_course_id = tk.Label(sm_window, text="Enter course id: ")
            lbl_input_course_id.grid(row=0, column=0)
            txt_input_course_id = tk.Entry(sm_window, width=20)
            txt_input_course_id.grid(row=1, column=0)
            input_course_id = txt_input_course_id.get()
            #submits button
            btn_submit = tk.Button(sm_window, text="Submit", command=lambda: self.output_funcs.output_course(input_course_id))
            btn_submit.grid(row=2, column=0)

        elif input_option == 9:
            sm_window = tk.Toplevel()
            sm_window.title("Mark search")
            sm_window.geometry("500x500")
            sm_window.configure(bg="white")
            sm_window.resizable(False, False)
            lbl_input_student_id = tk.Label(sm_window, text="Enter student id: ")
            lbl_input_student_id.grid(row=0, column=0)
            txt_input_student_id = tk.Entry(sm_window, width=20)
            txt_input_student_id.grid(row=1, column=0)
            input_student_id = txt_input_student_id.get()
            lbl_input_course_id = tk.Label(sm_window, text="Enter course id: ")
            lbl_input_course_id.grid(row=2, column=0)
            txt_input_course_id = tk.Entry(sm_window, width=20)
            txt_input_course_id.grid(row=3, column=0)
            input_course_id = txt_input_course_id.get()
            #submits button
            btn_submit = tk.Button(sm_window, text="Submit", command=lambda: self.output_funcs.output_mark(input_student_id, input_course_id))
            btn_submit.grid(row=4, column=0)

        elif input_option == 10:
            self.gpa_calculator()

        elif input_option == 11:
            self.input_funcs.load_data()

        elif input_option == 12:
            self.output_funcs.export_data_rename()

        elif input_option == 13:
            if os.path.exists("students_data_tmp.dt"):
                os.remove("students_data_tmp.dt")
            if os.path.exists("courses_data_tmp.dt"):
                os.remove("courses_data_tmp.dt")
            if os.path.exists("marks_data_tmp.dt"):
                os.remove("marks_data_tmp.dt")
            sys.exit()

        else:
            print("Invalid option")

#    def __del__(self):
#        self.sm_window.destroy()

