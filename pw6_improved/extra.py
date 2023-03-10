from input import Input
from output import Output
from domains.student import Student
from domains.course import Course
import curses
import math
import numpy as np

class ExtraFunc:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        self.stdscr = curses.initscr()

    def calculate_gpa(self):
        self.stdscr.clear()
        for student in self.students:
            total_mark = float(0)
            total_credit = int(0)
            for course in self.courses:
                if course.get_mark(student.get_id()) != "N/A":
                    total_mark += course.get_mark(student.get_id()) * course.get_credit()
                    total_credit += course.get_credit()
            if total_credit != 0:
                student.set_gpa(total_mark / total_credit)
                # round down to 2 decimal places
                student.set_gpa(math.floor(student.get_gpa() * 100) / 100)
            else:
                student.set_gpa("N/A")
        self.stdscr.addstr("GPA calculated.")

    def gpa_ranking(self):  # numpy used
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "GPA ranking:")
        line_count += 1
        gpa_list = []
        for student in self.students:
            gpa_list.append(student.get_gpa())
        gpa_list = np.array(gpa_list)
        gpa_list = np.sort(gpa_list)
        gpa_list = np.flip(gpa_list)
        for gpa in gpa_list:
            for student in self.students:
                if student.get_gpa() == gpa:
                    self.stdscr.addstr(line_count, 0, f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa()}")
                    line_count += 1

    def __del__(self):
        curses.endwin()
