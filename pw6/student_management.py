from domains.student import Student
from domains.course import Course
from input import Input
from output import Output
from extra import ExtraFunc

import curses

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.stdscr = curses.initscr()
        self.input = Input(self.students, self.courses)
        self.output = Output(self.students, self.courses)
        self.extra = ExtraFunc(self.students, self.courses)

    def option_lst(self):
        choice = int(self.stdscr.getstr())
        if choice == 1:
            self.input.input_student_multiple()
        elif choice == 2:
            self.input.input_course_multiple()
        elif choice == 3:
            self.input.input_mark()
        elif choice == 4:
            self.extra.calculate_gpa()
            #self.extra.gpa_ranking()
        elif choice == 5:
            self.output.display_student()
        elif choice == 6:
            self.output.display_course()
        elif choice == 7:
            self.output.display_mark()
        elif choice == 8:
            self.output.save_data()
            exit()
        elif choice == 9:
            exit()
        elif choice == 10:
            self.input.load_data()
        else:
            self.stdscr.addstr("Invalid choice.")

    def __del__(self):
        curses.endwin()
