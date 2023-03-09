from domains.student import Student
from domains.course import Course
from input import Input
from output import Output
import curses
import math
import numpy as np

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.in_no_student = int(0)
        self.stdscr = curses.initscr()
        self.input = Input(self.stdscr, self.students, self.courses)
        self.output = Output(self.stdscr, self.students, self.courses)

    def calculate_gpa(self):
        self.stdscr.clear()
        for student in self.students:
            total_mark = float(0)
            total_credit = int(0)
            for course in self.courses:
                if course.marks[student.id] != "N/A":
                    total_mark += course.marks[student.id] * course.credit
                    total_credit += course.credit
            if total_credit != 0:
                student.gpa = total_mark / total_credit
                #round down to 2 decimal places
                student.gpa = math.floor(student.gpa * 100) / 100
            else:
                student.gpa = "N/A"
        self.stdscr.addstr("GPA calculated.")

    def gpa_ranking(self): #numpy used
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "GPA ranking:")
        line_count += 1
        gpa_list = []
        for student in self.students:
            gpa_list.append(student.gpa)
        gpa_list = np.array(gpa_list)
        gpa_list = np.sort(gpa_list)
        gpa_list = np.flip(gpa_list)
        for gpa in gpa_list:
            for student in self.students:
                if student.gpa == gpa:
                    self.stdscr.addstr(line_count, 0, f"ID: {student.id}, Name: {student.name}, GPA: {student.gpa}")
                    line_count += 1

    def display_menu(self):
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "Student management system:")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "1. Input student")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "2. Input course")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "3. Input mark")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "4. Calculate GPA & ranking")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "5. Display student")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "6. Display course")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "7. Display mark")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "8. Exit(discard data)")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "Enter your choice: ")
        line_count += 1

        choice = int(self.stdscr.getstr())
        if choice == 1:
            self.stdscr.addstr(line_count, 0, "Number of students: ")
            in_num_student = int(self.stdscr.getstr(10, len("Number of students: "), 999))
            for num in range(0, in_num_student):
                self.input.input_student()
        elif choice == 2:
            self.stdscr.addstr(line_count, 0, "Number of courses: ")
            in_num_course = int(self.stdscr.getstr(10, len("Number of courses: "), 999))
            for num in range(0, in_num_course):
                self.input.input_course()
        elif choice == 3:
            self.input.input_mark()
        elif choice == 4:
            self.calculate_gpa()
            self.gpa_ranking()
        elif choice == 5:
            self.output.display_student()
        elif choice == 6:
            self.output.display_course()
        elif choice == 7:
            self.output.display_mark()
        elif choice == 8:
            self.stdscr.addstr("Goodbye!")
            exit()
        else:
            self.stdscr.addstr("Invalid choice.")

    def main(self):
        while True:
            self.display_menu()
            self.stdscr.addstr("\nPress any key to continue.")
            self.stdscr.getch()
            self.stdscr.clear()
