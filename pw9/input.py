from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import pickle

class Input:
    def __init__(self, student_list, course_list, mark_list):
        self.tk_window = tkinter.Tk()
        self.__student_list = student_list
        self.__course_list = course_list
        self.__mark_list = mark_list

    #setters
    def set_student_list(self, student_list):
        self.__student_list = student_list
    def set_course_list(self, course_list):
        self.__course_list = course_list
    def set_mark_list(self, mark_list):
        self.__mark_list = mark_list

    # methods
    def input_student(self):
        self.stdscr.clear()
        line_count = 0

        lbl_student_id = str("Enter student id: ")
        self.stdscr.addstr(line_count, 0, lbl_student_id)
        student_id = str(self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
        line_count += 1

        lbl_student_name = str("Enter student name: ")
        self.stdscr.addstr(line_count, 0, lbl_student_name)
        student_name = str(self.stdscr.getstr(line_count, len(lbl_student_name) + 1, 100))
        line_count += 1

        lbl_student_dob = str("Enter student date of birth: ")
        self.stdscr.addstr(line_count, 0, lbl_student_dob)
        dob = str(self.stdscr.getstr(line_count, len(lbl_student_dob) + 1, 10))
        line_count += 1

        gpa = str("N/A")

        student = Student(student_id, student_name, dob, gpa)
        self.__student_list.append(student)

    def input_course(self):
        self.stdscr.clear()
        line_count = 0

        lbl_course_id = str("Enter course id: ")
        self.stdscr.addstr(line_count, 0, lbl_course_id)
        course_id = str(self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
        line_count += 1

        lbl_course_name = str("Enter course name: ")
        self.stdscr.addstr(line_count, 0, lbl_course_name)
        course_name = str(self.stdscr.getstr(line_count, len(lbl_course_name) + 1, 100))
        line_count += 1

        lbl_course_credit = str("Enter course credit: ")
        self.stdscr.addstr(line_count, 0, lbl_course_credit)
        course_credit = int(self.stdscr.getstr(line_count, len(lbl_course_credit) + 1, 2))
        line_count += 1

        lbl_course_mark_mid_portion = str("Enter course mark mid portion: ")
        self.stdscr.addstr(line_count, 0, lbl_course_mark_mid_portion)
        course_mark_mid_portion = float(self.stdscr.getstr(line_count, len(lbl_course_mark_mid_portion) + 1, 3))
        line_count += 1

        lbl_course_mark_final_portion = str("Enter course mark final portion: ")
        self.stdscr.addstr(line_count, 0, lbl_course_mark_final_portion)
        course_mark_final_portion = float(self.stdscr.getstr(line_count, len(lbl_course_mark_final_portion) + 1, 3))
        line_count += 1

        course = Course(course_id, course_name, course_credit, course_mark_mid_portion, course_mark_final_portion)
        self.__course_list.append(course)


    def input_mark(self):
        self.stdscr.clear()
        line_count = 0
        lbl_student_id = str("Enter student id: ")
        self.stdscr.addstr(line_count, 0, lbl_student_id)
        student_id = str(self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
        line_count += 1

        for i in self.__student_list:
            if student_id == i.get_id():
                student_id = i.get_id()
                break

        lbl_course_id = str("Enter course id: ")
        self.stdscr.addstr(line_count, 0, lbl_course_id)
        course_id = str(self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
        line_count += 1
        for i in self.__course_list:
            if course_id == i.get_id():
                course_id = i.get_id()
                break
        lbl_mark_mid = str("Enter mark mid: ")
        self.stdscr.addstr(line_count, 0, lbl_mark_mid)
        mark_mid = float(self.stdscr.getstr(line_count, len(lbl_mark_mid) + 1, 10))
        line_count += 1

        lbl_mark_final = str("Enter mark final: ")
        self.stdscr.addstr(line_count, 0, lbl_mark_final)
        mark_final = float(self.stdscr.getstr(line_count, len(lbl_mark_final) + 1, 10))
        line_count += 1

        mark = Mark(student_id, course_id, mark_mid, mark_final)
        self.__mark_list.append(mark)

    def add_student(self):
        self.stdscr.clear()
        line_count = 0
        lbl_no_student = str("Enter number of students: ")
        self.stdscr.addstr(line_count, 0, lbl_no_student)
        input_no_student = int(self.stdscr.getstr(line_count, len(lbl_no_student) + 1, 10))
        line_count += 1
        for i in range(input_no_student):
            self.input_student()

    def add_course(self):
        self.stdscr.clear()
        line_count = 0
        lbl_no_course = str("Enter number of courses: ")
        self.stdscr.addstr(line_count, 0, lbl_no_course)
        input_no_course = int(self.stdscr.getstr(line_count, len(lbl_no_course) + 1, 10))
        line_count += 1
        for i in range(input_no_course):
            self.input_course()

    def add_mark(self):
        self.stdscr.clear()
        line_count = 0
        lbl_no_mark = str("Enter number of marks: ")
        self.stdscr.addstr(line_count, 0, lbl_no_mark)
        input_no_mark = int(self.stdscr.getstr(line_count, len(lbl_no_mark) + 1, 10))
        line_count += 1
        for i in range(input_no_mark):
            self.input_mark()

    def File2List(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data

    def load_data(self):
        self.stdscr.clear()
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.__student_list.clear()
        self.__course_list.clear()
        self.__mark_list.clear()

        data1 = self.File2List(filename1)
        for i in data1:
            student = Student(i.get_id(),
                              i.get_name(),
                              i.get_dob(),
                              i.get_gpa())
            self.__student_list.append(student)
        self.stdscr.addstr(0, 0, "Load student_data successfully")

        data2 = self.File2List(filename2)
        for i in data2:
            course = Course(i.get_id(),
                            i.get_name(),
                            i.get_credit(),
                            i.get_mark_mid_portion(),
                            i.get_mark_final_portion())
            self.__course_list.append(course)
        self.stdscr.addstr(1, 0, "Load course_data successfully")

        data3 = self.File2List(filename3)
        for i in data3:
            mark = Mark(i.get_student_id(),
                        i.get_course_id(),
                        i.get_mark_mid(),
                        i.get_mark_final())
            self.__mark_list.append(mark)
        self.stdscr.addstr(2, 0, "Load mark_data successfully")

    def __del__(self):
        curses.endwin()