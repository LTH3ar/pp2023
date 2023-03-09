from domains.student import Student
from domains.course import Course

class Output:

    def __init__(self, stdscr, students, courses):
        self.stdscr = stdscr
        self.in_no_student = int(0)
        self.student = Student
        self.course = Course
        self.students = students
        self.courses = courses


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