from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import tkinter as tk
import pickle

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
        input_window = tk.Toplevel()
        #rewrite to tk
        input_window.title("Add student")
        input_window.geometry("300x300")
        input_window.resizable(False, False)
        input_window.configure(bg="white")

        lbl_student_id = tk.Label(input_window, text="Enter student id: ", bg="white")
        lbl_student_id.place(x=10, y=10)
        txt_student_id = tk.Entry(input_window, width=20)
        txt_student_id.place(x=10, y=30)
        student_id = txt_student_id.get()

        lbl_student_name = tk.Label(input_window, text="Enter student name: ", bg="white")
        lbl_student_name.place(x=10, y=60)
        txt_student_name = tk.Entry(input_window, width=100)
        txt_student_name.place(x=10, y=80)
        student_name = txt_student_name.get()

        lbl_student_dob = tk.Label(input_window, text="Enter student date of birth: ", bg="white")
        lbl_student_dob.place(x=10, y=110)
        txt_student_dob = tk.Entry(input_window, width=10)
        txt_student_dob.place(x=10, y=130)
        dob = txt_student_dob.get()

        gpa = str("N/A")

        student = Student(student_id, student_name, dob, gpa)
        # submit button
        btn_submit = tk.Button(input_window, text="Submit", bg="white", command=self.__student_list.append(student))
        btn_submit.place(x=10, y=260)

    def input_course(self):
        input_window = tk.Toplevel()
        #rewrite to tk
        input_window.title("Add course")
        input_window.geometry("300x300")
        input_window.resizable(False, False)
        input_window.configure(bg="white")

        lbl_course_id = tk.Label(input_window, text="Enter course id: ", bg="white")
        lbl_course_id.place(x=10, y=10)
        txt_course_id = tk.Entry(input_window, width=20)
        txt_course_id.place(x=10, y=30)
        course_id = txt_course_id.get()

        lbl_course_name = tk.Label(input_window, text="Enter course name: ", bg="white")
        lbl_course_name.place(x=10, y=60)
        txt_course_name = tk.Entry(input_window, width=100)
        txt_course_name.place(x=10, y=80)
        course_name = txt_course_name.get()

        lbl_course_credit = tk.Label(input_window, text="Enter course credit: ", bg="white")
        lbl_course_credit.place(x=10, y=110)
        txt_course_credit = tk.Entry(input_window, width=10)
        txt_course_credit.place(x=10, y=130)
        course_credit = txt_course_credit.get()

        lbl_course_mark_mid_portion = tk.Label(input_window, text="Enter course mark mid portion: ", bg="white")
        lbl_course_mark_mid_portion.place(x=10, y=160)
        txt_course_mark_mid_portion = tk.Entry(input_window, width=10)
        txt_course_mark_mid_portion.place(x=10, y=180)
        course_mark_mid_portion = txt_course_mark_mid_portion.get()

        lbl_course_mark_final_portion = tk.Label(input_window, text="Enter course mark final portion: ", bg="white")
        lbl_course_mark_final_portion.place(x=10, y=210)
        txt_course_mark_final_portion = tk.Entry(input_window, width=10)
        txt_course_mark_final_portion.place(x=10, y=230)
        course_mark_final_portion = txt_course_mark_final_portion.get()

        course = Course(course_id, course_name, course_credit, course_mark_mid_portion, course_mark_final_portion)
        #submit button
        btn_submit = tk.Button(input_window, text="Submit", bg="white", command=self.__course_list.append(course))
        btn_submit.place(x=10, y=260)

    def input_mark(self):
        input_window = tk.Toplevel()
        #rewrite to tk
        input_window.title("Add mark")
        input_window.geometry("300x300")
        input_window.resizable(False, False)
        input_window.configure(bg="white")

        lbl_student_id = tk.Label(input_window, text="Enter student id: ", bg="white")
        lbl_student_id.place(x=10, y=10)
        txt_student_id = tk.Entry(input_window, width=20)
        txt_student_id.place(x=10, y=30)
        student_id = txt_student_id.get()

        for i in self.__student_list:
            if student_id == i.get_id():
                student_id = i.get_id()
                break

        lbl_course_id = tk.Label(input_window, text="Enter course id: ", bg="white")
        lbl_course_id.place(x=10, y=60)
        txt_course_id = tk.Entry(input_window, width=20)
        txt_course_id.place(x=10, y=80)
        course_id = txt_course_id.get()

        for i in self.__course_list:
            if course_id == i.get_id():
                course_id = i.get_id()
                break

        lbl_mark_mid = tk.Label(input_window, text="Enter mark mid: ", bg="white")
        lbl_mark_mid.place(x=10, y=110)
        txt_mark_mid = tk.Entry(input_window, width=10)
        txt_mark_mid.place(x=10, y=130)
        mark_mid = txt_mark_mid.get()

        lbl_mark_final = tk.Label(input_window, text="Enter mark final: ", bg="white")
        lbl_mark_final.place(x=10, y=160)
        txt_mark_final = tk.Entry(input_window, width=10)
        txt_mark_final.place(x=10, y=180)
        mark_final = txt_mark_final.get()

        mark = Mark(student_id, course_id, mark_mid, mark_final)
        #submit button
        btn_submit = tk.Button(input_window, text="Submit", bg="white", command=self.__mark_list.append(mark))
        btn_submit.place(x=10, y=210)

    def add_student(self):
        input_window = tk.Toplevel()
        input_window.title("Add student")
        input_window.geometry("300x300")
        input_window.resizable(False, False)
        input_window.configure(bg="white")

        lbl_no_student = tk.Label(input_window, text="Enter number of students: ", bg="white")
        lbl_no_student.place(x=10, y=10)
        txt_no_student = tk.Entry(input_window, width=10)
        txt_no_student.place(x=10, y=30)
        input_no_student = int(txt_no_student.get())

        for i in range(input_no_student):
            self.input_student()

    def add_course(self):
        input_window = tk.Toplevel()
        input_window.title("Add course")
        input_window.geometry("300x300")
        input_window.resizable(False, False)
        input_window.configure(bg="white")

        lbl_no_course = tk.Label(input_window, text="Enter number of courses: ", bg="white")
        lbl_no_course.place(x=10, y=10)
        txt_no_course = tk.Entry(input_window, width=10)
        txt_no_course.place(x=10, y=30)
        input_no_course = int(txt_no_course.get())

        for i in range(input_no_course):
            self.input_course()

    def add_mark(self):
        input_window = tk.Toplevel()
        input_window.title("Add mark")
        input_window.geometry("300x300")
        input_window.resizable(False, False)
        input_window.configure(bg="white")

        lbl_no_mark = tk.Label(input_window, text="Enter number of marks: ", bg="white")
        lbl_no_mark.place(x=10, y=10)
        txt_no_mark = tk.Entry(input_window, width=10)
        txt_no_mark.place(x=10, y=30)
        input_no_mark = int(txt_no_mark.get())

        for i in range(input_no_mark):
            self.input_mark()

    def File2List(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data

    def load_data(self):
        input_window = tk.Toplevel()
        input_window.title("Load data")
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
        #notify user that data is loaded
        lbl_notify1 = tk.Label(input_window, text="Load student_data successfully", bg="white")
        lbl_notify1.place(x=10, y=10)

        data2 = self.File2List(filename2)
        for i in data2:
            course = Course(i.get_id(),
                            i.get_name(),
                            i.get_credit(),
                            i.get_mark_mid_portion(),
                            i.get_mark_final_portion())
            self.__course_list.append(course)
        lbl_notify2 = tk.Label(input_window, text="Load course_data successfully", bg="white")
        lbl_notify2.place(x=10, y=40)

        data3 = self.File2List(filename3)
        for i in data3:
            mark = Mark(i.get_student_id(),
                        i.get_course_id(),
                        i.get_mark_mid(),
                        i.get_mark_final())
            self.__mark_list.append(mark)
        lbl_notify3 = tk.Label(input_window, text="Load mark_data successfully", bg="white")
        lbl_notify3.place(x=10, y=70)

#    def __del__(self):
#        input_window.destroy()
