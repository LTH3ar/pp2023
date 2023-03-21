from input import Input
from output import Output
import subprocess
import math
import numpy as np


class StudentManagement:
    #init
    def __init__(self):
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
        # Print the sorted array
        for s in gpa_arr:
            print(s)
    def gpa_ranking_High2Low(self):
        #sort by numpy
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
        # Print the sorted array
        for s in gpa_arr:
            print(s)

    def main(self):
        while True:
            print("\n1. Add student")
            print("2. Add course")
            print("3. Add mark")
            print("4. Output students list")
            print("5. Output courses list")
            print("6. Output marks list")
            print("7. Output student")
            print("8. Output course")
            print("9. Output mark")
            print("10. GPA calculator")
            print("11. GPA ranking (Low to High)")
            print("12. GPA ranking (High to Low)")
            print("13. Load data")
            print("14. Export data")
            print("15. Exit")

            input_option = int(input("Enter option: "))
            if input_option == 1:
                subprocess.call('clear', shell=True)
                self.input_funcs.add_student()

            elif input_option == 2:
                subprocess.call('clear', shell=True)
                self.input_funcs.add_course()

            elif input_option == 3:
                subprocess.call('clear', shell=True)
                self.input_funcs.add_mark()

            elif input_option == 4:
                subprocess.call('clear', shell=True)
                self.output_funcs.output_students_list()

            elif input_option == 5:
                subprocess.call('clear', shell=True)
                self.output_funcs.output_courses_list()

            elif input_option == 6:
                subprocess.call('clear', shell=True)
                self.output_funcs.output_marks_list()

            elif input_option == 7:
                subprocess.call('clear', shell=True)
                input_student_id = input("Enter student id: ")
                self.output_funcs.output_student(input_student_id)

            elif input_option == 8:
                subprocess.call('clear', shell=True)
                input_course_id = input("Enter course id: ")
                self.output_funcs.output_course(input_course_id)

            elif input_option == 9:
                subprocess.call('clear', shell=True)
                input_student_id = input("Enter student id: ")
                input_course_id = input("Enter course id: ")
                self.output_funcs.output_mark(input_student_id, input_course_id)

            elif input_option == 10:
                subprocess.call('clear', shell=True)
                self.gpa_calculator()

            elif input_option == 11:
                subprocess.call('clear', shell=True)
                self.gpa_ranking_Low2High()

            elif input_option == 12:
                subprocess.call('clear', shell=True)
                self.gpa_ranking_High2Low()

            elif input_option == 13:
                subprocess.call('clear', shell=True)
                self.input_funcs.load_data()

            elif input_option == 14:
                subprocess.call('clear', shell=True)
                self.output_funcs.export_data()

            elif input_option == 15:
                break
            else:
                print("Invalid option")


