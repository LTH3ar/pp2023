from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import pickle
import subprocess

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
    def input_student(self, action):
        subprocess.call("clear")
        if action == "add":
            input_no_student = int(input("Enter number of students: "))
            for i in range(input_no_student):
                subprocess.call("clear")

                student_id = str(input("Enter student id: "))
                student_name = str(input("Enter student name: "))
                dob = str(input("Enter student date of birth: "))
                gpa = str("N/A")
                student = Student(student_id,
                                  student_name,
                                  dob,
                                  gpa)
                self.__student_list.append(student)

        elif action == "remove":
            subprocess.call("clear")

            new_student_list_tmp = []
            student_id = str(input("Enter student id: "))
            for i in self.__student_list:
                if i.get_id() != student_id:
                    new_student_list_tmp.append(i)

            self.__student_list.clear()
            for i in new_student_list_tmp:
                self.__student_list.append(i)

        elif action == "update":
            subprocess.call("clear")
            student_id = str(input("Enter student id: "))
            student_name = str(input("Enter student name: "))
            dob = str(input("Enter student date of birth: "))

            for i in self.__student_list:
                if student_id == i.get_id():
                    i.set_name(student_name)
                    i.set_dob(dob)
                    break
        input("Press any key to exit")

    def manage_student(self):
        subprocess.call("clear")
        print("1. Add student")
        print("2. Remove student")
        print("3. Update student")
        print("4. Back")
        input_action = str(input("Enter your choice: "))

        if input_action == "":
            input("Press any key to exit")
            return

        if int(input_action) == 1:
            self.input_student("add")
        elif int(input_action) == 2:
            self.input_student("remove")
        elif int(input_action) == 3:
            self.input_student("update")
        elif int(input_action) == 4:
            input("Press any key to exit")
            return

    def input_course(self, action):
        subprocess.call("clear")
        if action == "add":
            input_no_course = int(input("Enter number of courses: "))
            for i in range(input_no_course):
                subprocess.call("clear")

                course_id = str(input("Enter course id: "))
                course_name = str(input("Enter course name: "))
                course_credit = int(input("Enter course credit: "))
                course_mark_mid_portion = float(input("Enter course mark mid portion: "))
                course_mark_final_portion = float(input("Enter course mark final portion: "))

                course = Course(course_id,
                                course_name,
                                course_credit,
                                course_mark_mid_portion,
                                course_mark_final_portion)
                self.__course_list.append(course)

        elif action == "remove":
            subprocess.call("clear")
            new_course_list_tmp = []
            course_id = str(input("Enter course id: "))

            for i in self.__course_list:
                if course_id != i.get_id():
                    new_course_list_tmp.append(i)

            self.__course_list.clear()
            for i in new_course_list_tmp:
                self.__course_list.append(i)

        elif action == "update":
            subprocess.call("clear")
            course_id = str(input("Enter course id: "))
            course_name = str(input("Enter course name: "))
            course_credit = int(input("Enter course credit: "))
            course_mark_mid_portion = float(input("Enter course mark mid portion: "))
            course_mark_final_portion = float(input("Enter course mark final portion: "))

            for i in self.__course_list:
                if course_id == i.get_id():
                    i.set_name(course_name)
                    i.set_credit(course_credit)
                    i.set_mark_mid_portion(course_mark_mid_portion)
                    i.set_mark_final_portion(course_mark_final_portion)
                    break
        input("Press any key to exit")

    def manage_course(self):
        subprocess.call("clear")
        print("1. Add course")
        print("2. Remove course")
        print("3. Update course")
        print("4. Back")
        input_action = str(input("Enter your choice: "))

        if input_action == "":
            input("Press any key to exit")
            return

        if int(input_action) == 1:
            self.input_course("add")
        elif int(input_action) == 2:
            self.input_course("remove")
        elif int(input_action) == 3:
            self.input_course("update")
        elif int(input_action) == 4:
            input("Press any key to exit")
            return




    def input_mark(self, action):
        subprocess.call("clear")

        if action == "add":
            input_no_mark = int(input("Enter number of marks: "))
            for i in range(input_no_mark):
                subprocess.call("clear")
                student_id = str(input("Enter student id: "))
                course_id = str(input("Enter course id: "))
                mark_mid = float(input("Enter mark mid: "))
                mark_final = float(input("Enter mark final: "))
                mark = Mark(student_id, course_id, mark_mid, mark_final)
                self.__mark_list.append(mark)

        elif action == "remove":
            subprocess.call("clear")
            student_id = str(input("Enter student id: "))
            course_id = str(input("Enter course id: "))

            new_mark_list_tmp = []
            for i in self.__mark_list:
                if student_id != i.get_student_id() and course_id != i.get_course_id():
                    new_mark_list_tmp.append(i)

            self.__mark_list.clear()
            for i in new_mark_list_tmp:
                self.__mark_list.append(i)

        elif action == "update":
            subprocess.call("clear")
            student_id = str(input("Enter student id: "))
            course_id = str(input("Enter course id: "))
            mark_mid = float(input("Enter mark mid: "))
            mark_final = float(input("Enter mark final: "))
            for i in self.__mark_list:
                if student_id == i.get_student_id() and course_id == i.get_course_id():
                    i.set_mark_mid(mark_mid)
                    i.set_mark_final(mark_final)
                    break
        input("Press any key to exit")


    def manage_mark(self):
        subprocess.call("clear")
        print("1. Add mark")
        print("2. Remove mark")
        print("3. Update mark")
        print("4. Back")

        input_action = str(input("Enter your choice: "))
        if input_action == "":
            input("Press any key to exit")
            return

        if int(input_action) == 1:
            self.input_mark("add")
        elif int(input_action) == 2:
            self.input_mark("remove")
        elif int(input_action) == 3:
            self.input_mark("update")
        elif int(input_action) == 4:
            input("Press any key to exit")
            return

    def File2List(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data

    def load_data(self):
        subprocess.call("clear")
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
        print("Load student_data successfully")

        data2 = self.File2List(filename2)
        for i in data2:
            course = Course(i.get_id(),
                            i.get_name(),
                            i.get_credit(),
                            i.get_mark_mid_portion(),
                            i.get_mark_final_portion())
            self.__course_list.append(course)
        print("Load course_data successfully")

        data3 = self.File2List(filename3)
        for i in data3:
            mark = Mark(i.get_student_id(),
                        i.get_course_id(),
                        i.get_mark_mid(),
                        i.get_mark_final())
            self.__mark_list.append(mark)
        print("Load mark_data successfully")
        input("Press any key to exit")