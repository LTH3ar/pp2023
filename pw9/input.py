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
        #student_id = txt_student_id.get()

        lbl_student_name = tk.Label(input_window, text="Enter student name: ", bg="white")
        lbl_student_name.place(x=10, y=60)
        txt_student_name = tk.Entry(input_window, width=100)
        txt_student_name.place(x=10, y=80)
        #student_name = txt_student_name.get()

        lbl_student_dob = tk.Label(input_window, text="Enter student date of birth: ", bg="white")
        lbl_student_dob.place(x=10, y=110)
        txt_student_dob = tk.Entry(input_window, width=10)
        txt_student_dob.place(x=10, y=130)
        #dob = txt_student_dob.get()

        gpa = str("N/A")
        # submit button
        btn_submit = tk.Button(input_window, text="Submit", bg="white", command=lambda: self.submit_student(txt_student_id, txt_student_name, txt_student_dob, gpa))
        btn_submit.place(x=10, y=260)

    def submit_student(self, txt_student_id, txt_student_name, txt_student_dob, gpa):
        student_id = str(txt_student_id.get())
        student_name = str(txt_student_name.get())
        dob = str(txt_student_dob.get())
        student = Student(student_id, student_name, dob, gpa)
        self.__student_list.append(student)
        txt_student_id.delete(0, tk.END)
        txt_student_name.delete(0, tk.END)
        txt_student_dob.delete(0, tk.END)

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
        #course_id = txt_course_id.get()

        lbl_course_name = tk.Label(input_window, text="Enter course name: ", bg="white")
        lbl_course_name.place(x=10, y=60)
        txt_course_name = tk.Entry(input_window, width=100)
        txt_course_name.place(x=10, y=80)
        #course_name = txt_course_name.get()

        lbl_course_credit = tk.Label(input_window, text="Enter course credit: ", bg="white")
        lbl_course_credit.place(x=10, y=110)
        txt_course_credit = tk.Entry(input_window, width=10)
        txt_course_credit.place(x=10, y=130)
        #course_credit = txt_course_credit.get()

        lbl_course_mark_mid_portion = tk.Label(input_window, text="Enter course mark mid portion: ", bg="white")
        lbl_course_mark_mid_portion.place(x=10, y=160)
        txt_course_mark_mid_portion = tk.Entry(input_window, width=10)
        txt_course_mark_mid_portion.place(x=10, y=180)
        #course_mark_mid_portion = txt_course_mark_mid_portion.get()

        lbl_course_mark_final_portion = tk.Label(input_window, text="Enter course mark final portion: ", bg="white")
        lbl_course_mark_final_portion.place(x=10, y=210)
        txt_course_mark_final_portion = tk.Entry(input_window, width=10)
        txt_course_mark_final_portion.place(x=10, y=230)
        #course_mark_final_portion = txt_course_mark_final_portion.get()

        btn_submit = tk.Button(input_window, text="Submit", bg="white", command=lambda: self.submit_course(txt_course_id, txt_course_name, txt_course_credit, txt_course_mark_mid_portion, txt_course_mark_final_portion))
        btn_submit.place(x=10, y=260)

    def submit_course(self, txt_course_id, txt_course_name, txt_course_credit, txt_course_mark_mid_portion, txt_course_mark_final_portion):
        course_id = str(txt_course_id.get())
        course_name = str(txt_course_name.get())
        course_credit = str(txt_course_credit.get())
        course_mark_mid_portion = int(txt_course_mark_mid_portion.get())
        course_mark_final_portion = int(txt_course_mark_final_portion.get())
        course = Course(course_id, course_name, course_credit, course_mark_mid_portion, course_mark_final_portion)
        self.__course_list.append(course)
        txt_course_id.delete(0, tk.END)
        txt_course_name.delete(0, tk.END)
        txt_course_credit.delete(0, tk.END)
        txt_course_mark_mid_portion.delete(0, tk.END)
        txt_course_mark_final_portion.delete(0, tk.END)

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
        #student_id = txt_student_id.get()

        lbl_course_id = tk.Label(input_window, text="Enter course id: ", bg="white")
        lbl_course_id.place(x=10, y=60)
        txt_course_id = tk.Entry(input_window, width=20)
        txt_course_id.place(x=10, y=80)
        #course_id = txt_course_id.get()

        lbl_mark_mid = tk.Label(input_window, text="Enter mark mid: ", bg="white")
        lbl_mark_mid.place(x=10, y=110)
        txt_mark_mid = tk.Entry(input_window, width=10)
        txt_mark_mid.place(x=10, y=130)
        #mark_mid = txt_mark_mid.get()

        lbl_mark_final = tk.Label(input_window, text="Enter mark final: ", bg="white")
        lbl_mark_final.place(x=10, y=160)
        txt_mark_final = tk.Entry(input_window, width=10)
        txt_mark_final.place(x=10, y=180)
        #mark_final = txt_mark_final.get()

        #submit button
        btn_submit = tk.Button(input_window, text="Submit", bg="white", command=lambda: self.submit_mark(txt_student_id, txt_course_id, txt_mark_mid, txt_mark_final))
        btn_submit.place(x=10, y=210)

    def submit_mark(self, txt_student_id, txt_course_id, txt_mark_mid, txt_mark_final):
        student_id = str(txt_student_id.get())
        course_id = str(txt_course_id.get())
        mark_mid = float(txt_mark_mid.get())
        mark_final = float(txt_mark_final.get())
        mark = Mark(student_id, course_id, mark_mid, mark_final)
        self.__mark_list.append(mark)
        txt_student_id.delete(0, tk.END)
        txt_course_id.delete(0, tk.END)
        txt_mark_mid.delete(0, tk.END)
        txt_mark_final.delete(0, tk.END)

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
