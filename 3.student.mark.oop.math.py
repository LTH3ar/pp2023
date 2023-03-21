import math
import json
import subprocess

class Student:
    #init
    def __init__(self, student_id, student_name, dob, gpa):
        self.__id = student_id
        self.__name = student_name
        self.__dob = dob
        self.__gpa = gpa

    #setters
    def set_id(self, student_id):
        self.__id = student_id
    def set_name(self, student_name):
        self.__name = student_name
    def set_dob(self, dob):
        self.__dob = dob
    def set_gpa(self, gpa):
        self.__gpa = gpa

    #getters
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_gpa(self):
        return self.__gpa


class Course:
    #init
    def __init__(self, course_id, course_name, course_credit, course_mark_mid_portion, course_mark_final_portion):
        self.__id = course_id
        self.__name = course_name
        self.__credit = course_credit
        self.__mark_mid_portion = course_mark_mid_portion
        self.__mark_final_portion = course_mark_final_portion

    #setters
    def set_id(self, course_id):
        self.__id = course_id
    def set_name(self, course_name):
        self.__name = course_name
    def set_credit(self, course_credit):
        self.__credit = course_credit
    def set_mark_mid_portion(self, course_mark_mid_portion):
        self.__mark_mid_portion = course_mark_mid_portion
    def set_mark_final_portion(self, course_mark_final_portion):
        self.__mark_final_portion = course_mark_final_portion

    #getters
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit
    def get_mark_mid_portion(self):
        return self.__mark_mid_portion
    def get_mark_final_portion(self):
        return self.__mark_final_portion


class Mark:
    #init
    def __init__(self, student_id, course_id, mark_mid, mark_final):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark_mid = mark_mid
        self.__mark_final = mark_final

    #setters
    def set_student_id(self, student_id):
        self.__student_id = student_id
    def set_course_id(self, course_id):
        self.__course_id = course_id
    def set_mark_mid(self, mark_mid):
        self.__mark_mid = mark_mid
    def set_mark_final(self, mark_final):
        self.__mark_final = mark_final

    #getters
    def get_student_id(self):
        return self.__student_id
    def get_course_id(self):
        return self.__course_id
    def get_mark_mid(self):
        return self.__mark_mid
    def get_mark_final(self):
        return self.__mark_final


class IOFuncs:
    #init
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

    #getters
    def get_student_list(self):
        return self.__student_list
    def get_course_list(self):
        return self.__course_list
    def get_mark_list(self):
        return self.__mark_list

    #methods
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

    def output_students_list(self):
        for i in self.__student_list:
            print("\nID: " + str(i.get_id())
                  + "\nName: " + str(i.get_name())
                  + "\nDoB: " + str(i.get_dob())
                  + "\nGPA: " + str(i.get_gpa())
                  )

    def output_courses_list(self):
        for i in self.__course_list:
            print("\nID: " + str(i.get_id())
                  + "\nName: " + str(i.get_name())
                  + "\nDoB: " + str(i.get_credit())
                  + "\nMid_%: " + str(i.get_mark_mid_portion())
                  + "\nFinal_%: " + str(i.get_mark_final_portion())
                  )

    def output_marks_list(self):
        for i in self.__mark_list:
            print("\nStudent ID: " + str(i.get_student_id())
                  + "\nCourse ID: " + str(i.get_course_id())
                  + "\nMid: " + str(i.get_mark_mid())
                  + "\nFinal: " + str(i.get_mark_final())
                  )

    def output_student(self, student_id):
        for i in self.__student_list:
            if i.get_id() == student_id:
                print("\nID: " + str(i.get_id())
                      + "\nName: " + str(i.get_name())
                      + "\nDoB: " + str(i.get_dob())
                      + "\nGPA: " + str(i.get_gpa())
                      )

    def output_course(self, course_id):
        for i in self.__course_list:
            if i.get_id() == course_id:
                print("\nID: " + str(i.get_id())
                      + "\nName: " + str(i.get_name())
                      + "\nDoB: " + str(i.get_credit())
                      + "\nMid_%: " + str(i.get_mark_mid_portion())
                      + "\nFinal_%: " + str(i.get_mark_final_portion())
                      )

    def output_mark(self, student_id, course_id):
        for i in self.__mark_list:
            if i.get_course_id() == course_id and i.get_student_id() == student_id:
                print("\nCourse ID: " + str(i.get_course_id())
                      + "\nStudent ID: " + str(i.get_student_id())
                      + "\nMid: " + str(i.get_mark_mid())
                      + "\nFinal: " + str(i.get_mark_final())
                      )

    def List2File(self, filename, lst): #write to json file
        with open(filename, "w") as file:
            json.dump(lst, file, default=lambda o: o.__dict__, indent=4)

    def File2List(self, filename): #read from json file
        with open(filename, 'r') as file:
            data = json.load(file)
        return data




class StudentManagement:
    #init
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.mark_list = []
        self.io_funcs = IOFuncs(self.student_list, self.course_list, self.mark_list)

    #methods
    def load_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.student_list.clear()
        self.course_list.clear()
        self.mark_list.clear()

        data1 = self.io_funcs.File2List(filename1)
        for i in data1:
            student = Student(i["_Student__id"],
                              i["_Student__name"],
                              i["_Student__dob"],
                              i["_Student__gpa"])
            self.student_list.append(student)

        data2 = self.io_funcs.File2List(filename2)
        for i in data2:
            course = Course(i["_Course__id"],
                            i["_Course__name"],
                            i["_Course__credit"],
                            i["_Course__mark_mid_portion"],
                            i["_Course__mark_final_portion"])
            self.course_list.append(course)

        data3 = self.io_funcs.File2List(filename3)
        for i in data3:
            mark = Mark(i["_Mark__student_id"],
                        i["_Mark__course_id"],
                        i["_Mark__mark_mid"],
                        i["_Mark__mark_final"])
            self.mark_list.append(mark)

    def export_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.io_funcs.List2File(filename1, self.student_list)
        self.io_funcs.List2File(filename2, self.course_list)
        self.io_funcs.List2File(filename3, self.mark_list)


    def add_student(self):
        input_no_student = int(input("Enter number of students: "))
        for i in range(input_no_student):
            self.io_funcs.input_student()

    def add_course(self):
        input_no_course = int(input("Enter number of courses: "))
        for i in range(input_no_course):
            self.io_funcs.input_course()

    def add_mark(self):
        input_no_mark = int(input("Enter number of marks: "))
        for i in range(input_no_mark):
            self.io_funcs.input_mark()

    def output_students_list(self):
        self.io_funcs.output_students_list()

    def output_courses_list(self):
        self.io_funcs.output_courses_list()

    def output_marks_list(self):
        self.io_funcs.output_marks_list()

    def output_student(self):
        input_student_id = input("Enter student id: ")
        self.io_funcs.output_student(input_student_id)

    def output_course(self):
        input_course_id = input("Enter course id: ")
        self.io_funcs.output_course(input_course_id)

    def output_mark(self):
        input_student_id = input("Enter student id: ")
        input_course_id = input("Enter course id: ")
        self.io_funcs.output_mark(input_student_id, input_course_id)

    def gpa_calculator(self):
        max_point = float(20)
        max_credit = 0
        for credit in self.course_list:
            max_credit += int(credit.get_credit())
        for student in self.student_list:
            gpa_sum = 0
            credits_sum = 0
            for course in self.course_list:
                for mark in self.mark_list:
                    if (course.get_id() == mark.get_course_id()
                            and mark.get_student_id() == student.get_id()):
                        mark_mid = ((float(mark.get_mark_mid()) / max_point)
                                    * ((float(course.get_mark_mid_portion()) / 100) * max_point))
                        # floor mark_mid to 1 decimal places
                        mark_mid = math.floor(mark_mid * 10) / 10

                        mark_final = ((float(mark.get_mark_final()) / max_point)
                                      * ((float(course.get_mark_final_portion()) / 100) * max_point))
                        # floor mark_final to 1 decimal places
                        mark_final = math.floor(mark_final * 10) / 10

                        mark_full = mark_mid + mark_final
                        # floor gpa to 1 decimal places
                        mark_full = math.floor(mark_full * 10) / 10

                        gpa_sum += mark_full * float(course.get_credit())
                        credits_sum += int(course.get_credit())

            if credits_sum < max_credit:
                gpa = "N/A"
            else:
                gpa = gpa_sum / credits_sum
                # floor gpa to 1 decimal places
                gpa = math.floor(gpa * 10) / 10
            student.set_gpa(gpa)

    def main(self):
        while True:
            print("\n1. Add student")
            print("2. Add course")
            print("3. Add mark")
            print("4. Output students list")
            print("5. Output courses list")
            print("6. Output marks list")
            print("7. Output student")
            print("8. Output course")
            print("9. Output mark")
            print("10. GPA calculator")
            print("11. Load data")
            print("12. Export data")
            print("13. Exit")

            input_option = int(input("Enter option: "))

            if input_option == 1:
                subprocess.call('clear', shell=True)
                self.add_student()
            elif input_option == 2:
                subprocess.call('clear', shell=True)
                self.add_course()
            elif input_option == 3:
                subprocess.call('clear', shell=True)
                self.add_mark()
            elif input_option == 4:
                subprocess.call('clear', shell=True)
                self.output_students_list()
            elif input_option == 5:
                subprocess.call('clear', shell=True)
                self.output_courses_list()
            elif input_option == 6:
                subprocess.call('clear', shell=True)
                self.output_marks_list()
            elif input_option == 7:
                subprocess.call('clear', shell=True)
                self.output_student()
            elif input_option == 8:
                subprocess.call('clear', shell=True)
                self.output_course()
            elif input_option == 9:
                subprocess.call('clear', shell=True)
                self.output_mark()
            elif input_option == 10:
                subprocess.call('clear', shell=True)
                self.gpa_calculator()
                print("GPA calculator successfully!")
            elif input_option == 11:
                subprocess.call('clear', shell=True)
                self.load_data()
                print("Load data successfully!")
            elif input_option == 12:
                subprocess.call('clear', shell=True)
                self.export_data()
                print("Export data successfully!")
            elif input_option == 13:
                break
            else:
                print("Invalid option!")

if __name__ == "__main__":
    student_management = StudentManagement()
    student_management.main()






