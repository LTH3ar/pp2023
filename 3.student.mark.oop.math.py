import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, student_name, dob, gpa):
        self.id = student_id
        self.name = student_name
        self.dob = dob
        self.gpa = gpa

class Course:
    def __init__(self, course_id, course_name, course_credit):
        self.id = course_id
        self.name = course_name
        self.credit = course_credit
        self.marks = {}

    def input_mark(self, student_id, mark):
        self.marks[student_id] = mark

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.in_no_student = int(0)
        self.stdscr = curses.initscr()

    def input_student(self):
        self.stdscr.clear()
        line_count = 0
        self.stdscr.addstr(line_count, 0, "Enter student details: ")
        line_count += 1

        lbl_student_id = str("Student ID: ")
        self.stdscr.addstr(line_count, 0, lbl_student_id)
        student_id = str(self.stdscr.getstr(line_count, len(lbl_student_id)+1, 20))
        line_count += 1

        lbl_student_name = str("Student name: ")
        self.stdscr.addstr(line_count, 0, lbl_student_name)
        student_name = str(self.stdscr.getstr(line_count, len(lbl_student_name)+1, 120))
        line_count += 1

        lbl_dob = str("Date of birth (DD-MM-YYYY): ")
        self.stdscr.addstr(line_count, 0, lbl_dob)
        dob = str(self.stdscr.getstr(line_count, len(lbl_dob)+1, 10))
        line_count += 1

        gpa = str('N/A')
        student = Student(student_id, student_name, dob, gpa)
        self.students.append(student)
        self.stdscr.addstr(line_count, 0, f"Student {student_name} added.")

    def input_course(self):
        self.stdscr.clear()
        line_count = 0
        self.stdscr.addstr(line_count, 0, "Enter course details:")
        line_count += 1

        lbl_course_id = str("Course ID: ")
        self.stdscr.addstr(line_count, 0, lbl_course_id)
        course_id = str(self.stdscr.getstr(line_count, len(lbl_course_id)+1, 20))
        line_count += 1

        lbl_course_name = str("Course name: ")
        self.stdscr.addstr(line_count, 0, lbl_course_name)
        course_name = str(self.stdscr.getstr(line_count, len(lbl_course_name)+1, 120))
        line_count += 1

        lbl_course_credit = str("Course credit: ")
        self.stdscr.addstr(line_count, 0, lbl_course_credit)
        course_credit = int(self.stdscr.getstr(line_count, len(lbl_course_credit)+1, 2))
        line_count += 1

        course = Course(course_id, course_name, course_credit)
        self.courses.append(course)
        for student in self.students:
            course.input_mark(student.id, "N/A")
        self.stdscr.addstr(line_count, 0, f"Course {course_name} added.")


    def input_mark(self):
        self.stdscr.clear()
        line_count = int(0)

        self.stdscr.addstr(line_count, 0, "Enter mark details:")
        line_count += 1

        for course in self.courses:
            self.stdscr.addstr(line_count, 0, f"{course.id}. {course.name}")
            line_count += 1

        lbl_course_id = str("Course ID: ")
        self.stdscr.addstr(line_count, 0, lbl_course_id)
        course_id = str(self.stdscr.getstr(line_count, len(lbl_course_id)+1, 20))
        line_count += 1

        lbl_no_student = str("Number of students: ")
        self.stdscr.addstr(line_count, 0, lbl_no_student)
        in_no_student = int(self.stdscr.getstr(line_count, len(lbl_no_student)+1, 999))
        line_count += 1

        if 1 <= in_no_student <= len(self.students):
            for num in range(0, in_no_student):
                self.stdscr.clear()
                line_count = int(0)
                lbl_student_id = str("Student ID: ")
                self.stdscr.addstr(line_count, 0, lbl_student_id)
                student_id = str(self.stdscr.getstr(line_count, len(lbl_student_id)+1, 20))
                line_count += 1

                lbl_mark = str("Mark: ")
                self.stdscr.addstr(line_count, 0, lbl_mark)
                mark = float(self.stdscr.getstr(line_count, len(lbl_mark)+1, 5))
                line_count += 1

                #round down to 1 decimal places
                mark = math.floor(mark * 10) / 10
                for course in self.courses:
                    if course.id == course_id:
                        course.input_mark(student_id, mark)

                self.stdscr.addstr(line_count, 0, f"Mark {mark} added for student {student_id} in course {course_id}.")
        else:
            self.stdscr.addstr(line_count, 0, "Invalid number of students.")

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

    def display_student(self):
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "Student list:")
        line_count += 1
        for student in self.students:
            self.stdscr.addstr(line_count, 0, f"ID: {student.id}, Name: {student.name}, Date of birth: {student.dob}, GPA: {student.gpa}")
            line_count += 1

    def display_course(self):
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "Course list:")
        line_count += 1
        for course in self.courses:
            self.stdscr.addstr(line_count, 0, f"ID: {course.id}, Name: {course.name}, Credit: {course.credit}")
            line_count += 1

    def display_mark(self):
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "Mark list:")
        line_count += 1
        for course in self.courses:
            self.stdscr.addstr(line_count, 0, f"Course ID: {course.id}, Course name: {course.name}")
            line_count += 1
            for student in self.students:
                self.stdscr.addstr(line_count, 0, f"Student ID: {student.id}, Student name: {student.name}, Mark: {course.marks[student.id]}")
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
                self.input_student()
        elif choice == 2:
            self.stdscr.addstr(line_count, 0, "Number of courses: ")
            in_num_course = int(self.stdscr.getstr(10, len("Number of courses: "), 999))
            for num in range(0, in_num_course):
                self.input_course()
        elif choice == 3:
            self.input_mark()
        elif choice == 4:
            self.calculate_gpa()
            self.gpa_ranking()
        elif choice == 5:
            self.display_student()
        elif choice == 6:
            self.display_course()
        elif choice == 7:
            self.display_mark()
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


if __name__ == "__main__":
    student_management = StudentManagement()
    curses.wrapper(student_management.main())

