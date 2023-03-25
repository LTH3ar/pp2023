from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import json
import tarfile
import curses
import os

class Input:
    def __init__(self, student_list, course_list, mark_list, stdscr):
        self.stdscr = stdscr
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
    # =========================================================================================
    # 1. Input student(add, remove, update)
    '''
    input student id, name, dob, gpa, action(add, remove, update)
    if action is add, then gpa is N/A
    if action is remove, then remove student with id
    if action is update, then update student with id
    '''
    def input_student(self, action):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0

        if action == "add":
            lbl_no_student = str("Enter number of students: ")
            self.stdscr.addstr(line_count, 0, lbl_no_student)
            input_no_student = int(self.stdscr.getstr(line_count, len(lbl_no_student) + 1, 10))
            for i in range(input_no_student):
                line_count = 0
                self.stdscr.clear()
                self.stdscr.refresh()

                lbl_student_id = str("Enter student id: ")
                self.stdscr.addstr(line_count, 0, lbl_student_id)
                student_id = (self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20)).decode("utf-8")
                line_count += 1

                lbl_student_name = str("Enter student name: ")
                self.stdscr.addstr(line_count, 0, lbl_student_name)
                student_name = self.stdscr.getstr(line_count, len(lbl_student_name) + 1, 100).decode("utf-8")
                line_count += 1

                lbl_student_dob = str("Enter student date of birth: ")
                self.stdscr.addstr(line_count, 0, lbl_student_dob)
                dob = self.stdscr.getstr(line_count, len(lbl_student_dob) + 1, 10).decode("utf-8")
                line_count += 1

                gpa = str("N/A")
                student = Student(student_id,
                                  student_name,
                                  dob,
                                  gpa)
                self.__student_list.append(student)

        elif action == "remove":
            self.stdscr.clear()
            self.stdscr.refresh()
            line_count = 0
            new_student_list_tmp = []
            lbl_student_id = str("Enter student id: ")
            self.stdscr.addstr(line_count, 0, lbl_student_id)
            student_id = self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20).decode("utf-8")

            for i in self.__student_list:
                if i.get_id() != student_id:
                    new_student_list_tmp.append(i)

            self.__student_list.clear()
            for i in new_student_list_tmp:
                self.__student_list.append(i)

        elif action == "update":
            line_count = 0
            self.stdscr.clear()
            self.stdscr.refresh()

            lbl_student_id = str("Enter student id: ")
            self.stdscr.addstr(line_count, 0, lbl_student_id)
            student_id = self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20).decode("utf-8")
            line_count += 1

            lbl_student_name = str("Enter student name: ")
            self.stdscr.addstr(line_count, 0, lbl_student_name)
            student_name = str(self.stdscr.getstr(line_count, len(lbl_student_name) + 1, 100))
            line_count += 1

            lbl_student_dob = str("Enter student date of birth: ")
            self.stdscr.addstr(line_count, 0, lbl_student_dob)
            dob = str(self.stdscr.getstr(line_count, len(lbl_student_dob) + 1, 10))
            line_count += 1
            for i in self.__student_list:
                if student_id == i.get_id():
                    i.set_name(student_name)
                    i.set_dob(dob)
                    break

    def manage_student(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0
        lbl_action = str("(1)Add/(2)Remove/(3)Update course")
        self.stdscr.addstr(line_count, 0, lbl_action)
        input_action = self.stdscr.getstr(line_count, len(lbl_action) + 1, 10).decode('utf-8')
        line_count += 1

        if input_action == "":
            return -1

        if int(input_action) == 1:
            self.input_student("add")
        elif int(input_action) == 2:
            self.input_student("remove")
        elif int(input_action) == 3:
            self.input_student("update")

    # ==================================================================================================
    # 2. Input course(add, remove, update)
    '''input course id, name, credit, action(add, remove, update)
    if action is add, then add course
    if action is remove, then remove course with id
    if action is update, then update course with id
    '''
    def input_course(self, action):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0

        if action == "add":
            lbl_no_course = str("Enter number of courses: ")
            self.stdscr.addstr(line_count, 0, lbl_no_course)
            input_no_course = int(self.stdscr.getstr(line_count, len(lbl_no_course) + 1, 10))
            for i in range(input_no_course):
                line_count = 0
                self.stdscr.clear()
                self.stdscr.refresh()

                lbl_course_id = str("Enter course id: ")
                self.stdscr.addstr(line_count, 0, lbl_course_id)
                course_id = (self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
                line_count += 1

                lbl_course_name = str("Enter course name: ")
                self.stdscr.addstr(line_count, 0, lbl_course_name)
                course_name = (self.stdscr.getstr(line_count, len(lbl_course_name) + 1, 100))
                line_count += 1

                lbl_course_credit = str("Enter course credit: ")
                self.stdscr.addstr(line_count, 0, lbl_course_credit)
                course_credit = int(self.stdscr.getstr(line_count, len(lbl_course_credit) + 1, 10))
                line_count += 1

                lbl_course_mark_mid_portion = str("Enter course mark mid portion: ")
                self.stdscr.addstr(line_count, 0, lbl_course_mark_mid_portion)
                course_mark_mid_portion = float(self.stdscr.getstr(line_count, len(lbl_course_mark_mid_portion) + 1, 3))
                line_count += 1

                lbl_course_mark_final_portion = str("Enter course mark final portion: ")
                self.stdscr.addstr(line_count, 0, lbl_course_mark_final_portion)
                course_mark_final_portion = float(
                    self.stdscr.getstr(line_count, len(lbl_course_mark_final_portion) + 1, 3))
                line_count += 1

                course = Course(course_id.decode("utf-8"),
                                course_name.decode("utf-8"),
                                course_credit,
                                course_mark_mid_portion,
                                course_mark_final_portion)
                self.__course_list.append(course)

        elif action == "remove":
            self.stdscr.clear()
            self.stdscr.refresh()
            line_count = 0
            new_course_list_tmp = []
            lbl_course_id = str("Enter course id: ")
            self.stdscr.addstr(line_count, 0, lbl_course_id)
            course_id = self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20).decode("utf-8")

            for i in self.__course_list:
                if course_id != i.get_id():
                    new_course_list_tmp.append(i)

            self.__course_list.clear()
            for i in new_course_list_tmp:
                self.__course_list.append(i)

        elif action == "update":
            lbl_course_id = str("Enter course id: ")
            self.stdscr.addstr(line_count, 0, lbl_course_id)
            course_id = (self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
            line_count += 1

            lbl_course_name = str("Enter course name: ")
            self.stdscr.addstr(line_count, 0, lbl_course_name)
            course_name = (self.stdscr.getstr(line_count, len(lbl_course_name) + 1, 100))
            line_count += 1

            lbl_course_credit = str("Enter course credit: ")
            self.stdscr.addstr(line_count, 0, lbl_course_credit)
            course_credit = int(self.stdscr.getstr(line_count, len(lbl_course_credit) + 1, 10))
            line_count += 1

            lbl_course_mark_mid_portion = str("Enter course mark mid portion: ")
            self.stdscr.addstr(line_count, 0, lbl_course_mark_mid_portion)
            course_mark_mid_portion = float(self.stdscr.getstr(line_count, len(lbl_course_mark_mid_portion) + 1, 3))
            line_count += 1

            lbl_course_mark_final_portion = str("Enter course mark final portion: ")
            self.stdscr.addstr(line_count, 0, lbl_course_mark_final_portion)
            course_mark_final_portion = float(
                self.stdscr.getstr(line_count, len(lbl_course_mark_final_portion) + 1, 3))
            line_count += 1

            for i in self.__course_list:
                if course_id.decode("utf-8") == i.get_id():
                    i.set_name(course_name.decode("utf-8"))
                    i.set_credit(course_credit)
                    i.set_mark_mid_portion(course_mark_mid_portion)
                    i.set_mark_final_portion(course_mark_final_portion)
                    break

    def manage_course(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0
        lbl_action = str("(1)Add/(2)Remove/(3)Update course")
        self.stdscr.addstr(line_count, 0, lbl_action)
        input_action = self.stdscr.getstr(line_count, len(lbl_action) + 1, 10)
        line_count += 1

        if input_action.decode("utf-8") == "":
            self.stdscr.clear()
            self.stdscr.refresh()
            return

        if int(input_action) == 1:
            self.input_course("add")
        elif int(input_action) == 2:
            self.input_course("remove")
        elif int(input_action) == 3:
            self.input_course("update")

    #==================================================================================================
    # 3. Input mark(add, remove, update)
    '''input student id, course id, mark, action(add, remove, update)
    if action is add, then add mark
    if action is remove, then remove mark with student id and course id
    if action is update, then update mark with student id and course id
    '''
    def input_mark(self, action):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0
        if action == "add":
            lbl_no_mark = str("Enter number of marks: ")
            self.stdscr.addstr(line_count, 0, lbl_no_mark)
            input_no_mark = int(self.stdscr.getstr(line_count, len(lbl_no_mark) + 1, 10))
            for i in range(input_no_mark):
                self.stdscr.clear()
                self.stdscr.refresh()
                line_count = 0
                lbl_student_id = str("Enter student id: ")
                self.stdscr.addstr(line_count, 0, lbl_student_id)
                student_id = (self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
                line_count += 1

                lbl_course_id = str("Enter course id: ")
                self.stdscr.addstr(line_count, 0, lbl_course_id)
                course_id = (self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
                line_count += 1

                lbl_mark_mid = str("Enter mark mid: ")
                self.stdscr.addstr(line_count, 0, lbl_mark_mid)
                mark_mid = float(self.stdscr.getstr(line_count, len(lbl_mark_mid) + 1, 3))
                line_count += 1

                lbl_mark_final = str("Enter mark final: ")
                self.stdscr.addstr(line_count, 0, lbl_mark_final)
                mark_final = float(self.stdscr.getstr(line_count, len(lbl_mark_final) + 1, 3))
                line_count += 1

                mark = Mark(student_id.decode("utf-8"), course_id.decode("utf-8"), mark_mid, mark_final)
                self.__mark_list.append(mark)

        elif action == "remove":
            lbl_student_id = str("Enter student id: ")
            self.stdscr.addstr(line_count, 0, lbl_student_id)
            student_id = (self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
            line_count += 1

            lbl_course_id = str("Enter course id: ")
            self.stdscr.addstr(line_count, 0, lbl_course_id)
            course_id = (self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
            line_count += 1

            new_mark_list_tmp = []
            for i in self.__mark_list:
                if student_id.decode("utf-8") != i.get_student_id() and course_id != i.get_course_id():
                    new_mark_list_tmp.append(i)

            self.__mark_list.clear()
            for i in new_mark_list_tmp:
                self.__mark_list.append(i)

        elif action == "update":
            lbl_student_id = str("Enter student id: ")
            self.stdscr.addstr(line_count, 0, lbl_student_id)
            student_id = (self.stdscr.getstr(line_count, len(lbl_student_id) + 1, 20))
            line_count += 1

            lbl_course_id = str("Enter course id: ")
            self.stdscr.addstr(line_count, 0, lbl_course_id)
            course_id = (self.stdscr.getstr(line_count, len(lbl_course_id) + 1, 20))
            line_count += 1

            lbl_mark_mid = str("Enter mark mid: ")
            self.stdscr.addstr(line_count, 0, lbl_mark_mid)
            mark_mid = float(self.stdscr.getstr(line_count, len(lbl_mark_mid) + 1, 3))
            line_count += 1

            lbl_mark_final = str("Enter mark final: ")
            self.stdscr.addstr(line_count, 0, lbl_mark_final)
            mark_final = float(self.stdscr.getstr(line_count, len(lbl_mark_final) + 1, 3))
            line_count += 1

            for i in self.__mark_list:
                if student_id.decode("utf-8") == i.get_student_id() and course_id.decode("utf-8") == i.get_course_id():
                    i.set_mark_mid(mark_mid)
                    i.set_mark_final(mark_final)
                    break


    def manage_mark(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0
        lbl_action = str("(1)Add/(2)Remove/(3)Update mark")
        self.stdscr.addstr(line_count, 0, lbl_action)
        input_action = (self.stdscr.getstr(line_count, len(lbl_action) + 1, 10))
        line_count += 1

        if input_action.decode("utf-8") == "":
            return

        if int(input_action) == 1:
            self.input_mark("add")
        elif int(input_action) == 2:
            self.input_mark("remove")
        elif int(input_action) == 3:
            self.input_mark("update")

    # ==================================================================================================
    '''load data from file'''

    def decompress_file(self, filename):
        with tarfile.open(filename, "r:gz") as tar:
            tar.extractall(path=".")

    def File2List(self, filename): #read from json file
        with open(filename, 'r') as file:
            data = json.load(file)
        return data


    #load data from file
    def load_data(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        self.decompress_file("students.dat")
        filename1 = "students_data.json"
        filename2 = "courses_data.json"
        filename3 = "marks_data.json"
        self.__student_list.clear()
        self.__course_list.clear()
        self.__mark_list.clear()

        data1 = self.File2List(filename1)
        for i in data1:
            student = Student(i["_Student__id"],
                              i["_Student__name"],
                              i["_Student__dob"],
                              i["_Student__gpa"])
            self.__student_list.append(student)
        self.stdscr.addstr(0, 0, "Load student_data successfully")
        os.remove(filename1)

        data2 = self.File2List(filename2)
        for i in data2:
            course = Course(i["_Course__id"],
                            i["_Course__name"],
                            i["_Course__credit"],
                            i["_Course__mark_mid_portion"],
                            i["_Course__mark_final_portion"])
            self.__course_list.append(course)
        self.stdscr.addstr(1, 0, "Load course_data successfully")
        os.remove(filename2)

        data3 = self.File2List(filename3)
        for i in data3:
            mark = Mark(i["_Mark__student_id"],
                        i["_Mark__course_id"],
                        i["_Mark__mark_mid"],
                        i["_Mark__mark_final"])
            self.__mark_list.append(mark)
        self.stdscr.addstr(2, 0, "Load mark_data successfully")
        os.remove(filename3)

    def __del__(self):
        curses.endwin()
    # ==================================================================================================
