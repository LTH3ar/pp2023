from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import pickle
import curses
import time
import os

class Output:
    def __init__(self, student_list, course_list, mark_list):
        self.stdscr = curses.initscr()
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
        self.stdscr.clear()
        line_count = 0
        for i in self.__student_list:
            self.stdscr.addstr(line_count, 0, "ID: " + str(i.get_id()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Name: " + str(i.get_name()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "DoB: " + str(i.get_dob()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "GPA: " + str(i.get_gpa()))
            line_count += 2

    def output_courses_list(self):
        self.stdscr.clear()
        line_count = 0
        for i in self.__course_list:
            self.stdscr.addstr(line_count, 0, "Course_ID: " + str(i.get_id()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Course_Name: " + str(i.get_name()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Credit: " + str(i.get_credit()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Mid_%: " + str(i.get_mark_mid_portion()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Final_%: " + str(i.get_mark_final_portion()))
            line_count += 2

    def output_marks_list(self):
        self.stdscr.clear()
        line_count = 0
        for i in self.__mark_list:
            self.stdscr.addstr(line_count, 0, "Student ID: " + str(i.get_student_id()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Course ID: " + str(i.get_course_id()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Mid: " + str(i.get_mark_mid()))
            line_count += 1
            self.stdscr.addstr(line_count, 0, "Final: " + str(i.get_mark_final()))
            line_count += 2


    def output_student(self, student_id):
        self.stdscr.clear()
        line_count = 0
        for i in self.__student_list:
            if i.get_id() == student_id:
                self.stdscr.addstr(line_count, 0, "ID: " + str(i.get_id()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Name: " + str(i.get_name()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "DoB: " + str(i.get_dob()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "GPA: " + str(i.get_gpa()))
                line_count += 2

    def output_course(self, course_id):
        self.stdscr.clear()
        line_count = 0
        for i in self.__course_list:
            if i.get_id() == course_id:
                self.stdscr.addstr(line_count, 0, "Course_ID: " + str(i.get_id()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Course_Name: " + str(i.get_name()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Credit: " + str(i.get_credit()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Mid_%: " + str(i.get_mark_mid_portion()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Final_%: " + str(i.get_mark_final_portion()))
                line_count += 2

    def output_mark(self, student_id, course_id):
        self.stdscr.clear()
        line_count = 0
        for i in self.__mark_list:
            if i.get_course_id() == course_id and i.get_student_id() == student_id:
                self.stdscr.addstr(line_count, 0, "Student ID: " + str(i.get_student_id()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Course ID: " + str(i.get_course_id()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Mid: " + str(i.get_mark_mid()))
                line_count += 1
                self.stdscr.addstr(line_count, 0, "Final: " + str(i.get_mark_final()))
                line_count += 2

    def List2File(self, filename, lst):
        with open(filename, "wb") as file:
            pickle.dump(lst, file)

    def export_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.List2File(filename1, self.__student_list)
        self.List2File(filename2, self.__course_list)
        self.List2File(filename3, self.__mark_list)

    def export_data_daemon(self):
        while True:
            time.sleep(1)
            filename1 = "students_data_tmp.dt"
            filename2 = "courses_data_tmp.dt"
            filename3 = "marks_data_tmp.dt"
            self.List2File(filename1, self.__student_list)
            self.List2File(filename2, self.__course_list)
            self.List2File(filename3, self.__mark_list)

    def export_data_rename(self):
        filename1 = "students_data_tmp.dt"
        filename2 = "courses_data_tmp.dt"
        filename3 = "marks_data_tmp.dt"
        os.rename(filename1, "students_data.dt")
        os.rename(filename2, "courses_data.dt")
        os.rename(filename3, "marks_data.dt")


    def __del__(self):
        curses.endwin()