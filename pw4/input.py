from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import json

class Input:
    def __init__(self, student_list, course_list, mark_list):
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
        student_id = str(input("Enter student id: "))
        student_name = str(input("Enter student name: "))
        dob = str(input("Enter date of birth: "))
        gpa = str("N/A")
        student = Student(student_id, student_name, dob, gpa)
        self.__student_list.append(student)

    def input_course(self):
        course_id = str(input("Enter course id: "))
        course_name = str(input("Enter course name: "))
        course_credit = int(input("Enter course credit: "))
        course_mark_mid_portion = float(input("Enter course mark mid portion: "))
        course_mark_final_portion = float(input("Enter course mark final portion: "))
        course = Course(course_id, course_name, course_credit, course_mark_mid_portion, course_mark_final_portion)
        self.__course_list.append(course)

    def input_mark(self):
        student_id = str(input("Enter student id: "))
        for i in self.__student_list:
            if student_id == i.get_id():
                student_id = i.get_id()
                break
        course_id = str(input("Enter course id: "))
        for i in self.__course_list:
            if course_id == i.get_id():
                course_id = i.get_id()
                break
        mark_mid = float(input("Enter mark mid: "))
        mark_final = float(input("Enter mark final: "))
        mark = Mark(student_id, course_id, mark_mid, mark_final)
        self.__mark_list.append(mark)

    def add_student(self):
        input_no_student = int(input("Enter number of students: "))
        for i in range(input_no_student):
            self.input_student()

    def add_course(self):
        input_no_course = int(input("Enter number of courses: "))
        for i in range(input_no_course):
            self.input_course()

    def add_mark(self):
        input_no_mark = int(input("Enter number of marks: "))
        for i in range(input_no_mark):
            self.input_mark()

    def File2List(self, filename): #read from json file
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

    def load_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
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

        data2 = self.File2List(filename2)
        for i in data2:
            course = Course(i["_Course__id"],
                            i["_Course__name"],
                            i["_Course__credit"],
                            i["_Course__mark_mid_portion"],
                            i["_Course__mark_final_portion"])
            self.__course_list.append(course)

        data3 = self.File2List(filename3)
        for i in data3:
            mark = Mark(i["_Mark__student_id"],
                        i["_Mark__course_id"],
                        i["_Mark__mark_mid"],
                        i["_Mark__mark_final"])
            self.__mark_list.append(mark)