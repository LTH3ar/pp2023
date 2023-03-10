from domains.student import Student
from domains.course import Course
import curses
import math
import json
class Input:
    def __init__(self, students, courses):
        self.stdscr = curses.initscr()
        self.in_no_student = int(0)
        self.students = students
        self.courses = courses


    def input_student(self):
        self.stdscr.clear()
        line_count = 0
        self.stdscr.addstr(line_count, 0, "Enter student details: ")
        line_count += 1

        lbl_student_id = str("Student ID: ")
        self.stdscr.addstr(line_count, 0, lbl_student_id)
        student_id = str(self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
        line_count += 1

        lbl_student_name = str("Student name: ")
        self.stdscr.addstr(line_count, 0, lbl_student_name)
        student_name = str(self.stdscr.getstr(line_count, len(lbl_student_name) + 1, 120))
        line_count += 1

        lbl_dob = str("Date of birth (DD-MM-YYYY): ")
        self.stdscr.addstr(line_count, 0, lbl_dob)
        dob = str(self.stdscr.getstr(line_count, len(lbl_dob) + 1, 10))
        line_count += 1

        gpa = str('N/A')
        student = Student()
        student.set_id(student_id)
        student.set_name(student_name)
        student.set_dob(dob)
        student.set_gpa(gpa)

        self.students.append(student)
        self.stdscr.addstr(line_count, 0, f"Student {student_name} added.")

    def input_student_multiple(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Number of students: ")
        in_num_student = int(self.stdscr.getstr(0, len("Number of students: "), 999))
        for num in range(0, in_num_student):
            self.input_student()

    def input_course(self):
        self.stdscr.clear()
        line_count = 0
        self.stdscr.addstr(line_count, 0, "Enter course details:")
        line_count += 1

        lbl_course_id = str("Course ID: ")
        self.stdscr.addstr(line_count, 0, lbl_course_id)
        course_id = str(self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
        line_count += 1

        lbl_course_name = str("Course name: ")
        self.stdscr.addstr(line_count, 0, lbl_course_name)
        course_name = str(self.stdscr.getstr(line_count, len(lbl_course_name) + 1, 120))
        line_count += 1

        lbl_course_credit = str("Course credit: ")
        self.stdscr.addstr(line_count, 0, lbl_course_credit)
        course_credit = int(self.stdscr.getstr(line_count, len(lbl_course_credit) + 1, 2))
        line_count += 1

        course = Course()
        course.set_id(course_id)
        course.set_name(course_name)
        course.set_credit(course_credit)

        self.courses.append(course)
        for student in self.students:
            course.input_mark(student.get_id(), "N/A")
        self.stdscr.addstr(line_count, 0, f"Course {course_name} added.")

    def input_course_multiple(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Number of courses: ")
        in_num_course = int(self.stdscr.getstr(0, len("Number of courses: "), 999))
        for num in range(0, in_num_course):
            self.input_course()

    def input_mark(self):
        self.stdscr.clear()
        line_count = int(0)

        self.stdscr.addstr(line_count, 0, "Enter mark details:")
        line_count += 1

        for course in self.courses:
            self.stdscr.addstr(line_count, 0, f"{course.get_id()}. {course.get_name()}")
            line_count += 1

        lbl_course_id = str("Course ID: ")
        self.stdscr.addstr(line_count, 0, lbl_course_id)
        course_id = str(self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
        line_count += 1

        lbl_no_student = str("Number of students: ")
        self.stdscr.addstr(line_count, 0, lbl_no_student)
        in_no_student = int(self.stdscr.getstr(line_count, len(lbl_no_student) + 1, 999))
        line_count += 1

        if 1 <= in_no_student <= len(self.students):
            for num in range(0, in_no_student):
                self.stdscr.clear()
                line_count = int(0)
                lbl_student_id = str("Student ID: ")
                self.stdscr.addstr(line_count, 0, lbl_student_id)
                student_id = str(self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
                line_count += 1

                lbl_mark = str("Mark: ")
                self.stdscr.addstr(line_count, 0, lbl_mark)
                mark = float(self.stdscr.getstr(line_count, len(lbl_mark) + 1, 5))
                line_count += 1

                # round down to 1 decimal places
                mark = math.floor(mark * 10) / 10
                for course in self.courses:
                    if course.get_id() == course_id:
                        course.input_mark(student_id, mark)

                self.stdscr.addstr(line_count, 0,
                                   f"Mark {mark} added for student {student_id} in course {course_id}.")
        else:
            self.stdscr.addstr(line_count, 0, "Invalid number of students.")

    def load_data_student(self): # json format student_data.dt
        with open('student_data.dt', 'r') as file:
            student_data = json.load(file)
            for student in student_data:
                student_id = student['_Student__id']
                student_name = student['_Student__name']
                dob = student['_Student__dob']
                gpa = student['_Student__gpa']

                new_student = Student()
                new_student.set_id(student_id)
                new_student.set_name(student_name)
                new_student.set_dob(dob)
                new_student.set_gpa(gpa)

                self.students.append(new_student)

    def load_data_course(self):
        with open('course_data.dt', 'r') as file:
            course_data = json.load(file)
            for course in course_data:
                course_id = course['_Course__id']
                course_name = course['_Course__name']
                course_credit = course['_Course__credit']
                new_course = Course()
                new_course.set_id(course_id)
                new_course.set_name(course_name)
                new_course.set_credit(course_credit)

                for student_id, mark in course['_Course__marks'].items():
                    new_course.input_mark(student_id, mark)
                self.courses.append(new_course)

    def load_data(self):
        self.load_data_student()
        self.load_data_course()

    def __del__(self):
        curses.endwin()