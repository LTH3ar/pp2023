from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import tkinter as tk
import pickle

class Input:
    def __init__(self, student_list, course_list, mark_list, menu_window):
        self.__student_list = student_list
        self.__course_list = course_list
        self.__mark_list = mark_list
        self.menu_window = menu_window

    #setters
    def set_student_list(self, student_list):
        self.__student_list.clear()
        self.__student_list = student_list
    def set_course_list(self, course_list):
        self.__course_list.clear()
        self.__course_list = course_list
    def set_mark_list(self, mark_list):
        self.__mark_list.clear()
        self.__mark_list = mark_list

    # methods
    #=========================================================================================
    # 1. Input student(add, remove, update)
    '''
    input student id, name, dob, gpa, action(add, remove, update)
    if action is add, then gpa is N/A
    if action is remove, then remove student with id
    if action is update, then update student with id
    '''
    def input_student(self):
        input_window = tk.Toplevel(self.menu_window)
        input_window.title("Add/Remove/Update student")
        input_window.geometry("450x300")
        input_window.resizable(True, True)
        input_window.configure(bg="white")

        lbl_student_id = tk.Label(input_window,
                                  text="Enter student id: ",
                                  bg="white")
        lbl_student_id.place(x=10, y=10)
        txt_student_id = tk.Entry(input_window, width=50)
        txt_student_id.place(x=10, y=30)

        lbl_student_name = tk.Label(input_window,
                                    text="Enter student name: ",
                                    bg="white")
        lbl_student_name.place(x=10, y=60)
        txt_student_name = tk.Entry(input_window, width=50)
        txt_student_name.place(x=10, y=80)

        lbl_student_dob = tk.Label(input_window,
                                   text="Enter student date of birth: ",
                                   bg="white")
        lbl_student_dob.place(x=10, y=110)
        txt_student_dob = tk.Entry(input_window, width=50)
        txt_student_dob.place(x=10, y=130)

        selected_action = tk.StringVar(input_window)
        selected_action.set("add")
        lbl_action = tk.Label(input_window, text="Select action: ", bg="white")
        lbl_action.place(x=10, y=160)
        action_lst = ["add", "remove", "update"]
        option_action = tk.OptionMenu(input_window, selected_action, *action_lst)
        option_action.place(x=10, y=180)

        if selected_action.get() == "add":
            gpa = str("N/A")

        # submit button
        btn_submit = tk.Button(input_window,
                               text="Submit",
                               bg="white",
                               command=lambda: self.submit_student(
                                                    txt_student_id,
                                                    txt_student_name,
                                                    txt_student_dob,
                                                    gpa,
                                                    selected_action.get()))
        btn_submit.place(x=10, y=260)

        input_window.protocol("WM_DELETE_WINDOW", input_window.destroy)

    # submit student info
    def submit_student(self,
                       txt_student_id,
                       txt_student_name,
                       txt_student_dob,
                       gpa,
                       action):
        student_id = str(txt_student_id.get())

        if action == "add":
            student_name = str(txt_student_name.get())
            dob = str(txt_student_dob.get())
            if any(student.get_id() == student_id for student in self.__student_list):
                raise ValueError("Student ID already exists")
            student = Student(student_id,
                              student_name,
                              dob,
                              gpa)
            self.__student_list.append(student)
            print("Student added successfully")

        elif action == "remove":
            new_student_list_tmp = []
            for student in self.__student_list:
                if student.get_id() == student_id:
                    continue
                new_student_list_tmp.append(student)
            self.__student_list.clear()
            for student in new_student_list_tmp:
                self.__student_list.append(student)
            print("Student removed successfully")

        elif action == "update":
            student_name = str(txt_student_name.get())
            dob = str(txt_student_dob.get())
            for student in self.__student_list:
                if student.get_id() == student_id:
                    student.set_name(student_name)
                    student.set_dob(dob)
                    break
            print("Student updated successfully")

        else:
            raise ValueError("Invalid action")

        txt_student_id.delete(0, tk.END)
        txt_student_name.delete(0, tk.END)
        txt_student_dob.delete(0, tk.END)

    #==================================================================================================
    # 2. Input course(add, remove, update)
    '''input course id, name, credit, action(add, remove, update)
    if action is add, then add course
    if action is remove, then remove course with id
    if action is update, then update course with id
    '''
    def input_course(self):
        input_window = tk.Toplevel(self.menu_window)
        input_window.title("Add/Remove/Update course")
        input_window.geometry("450x400")
        input_window.resizable(True, True)
        input_window.configure(bg="white")

        lbl_course_id = tk.Label(input_window,
                                 text="Enter course id: ",
                                 bg="white")
        lbl_course_id.place(x=10, y=10)
        txt_course_id = tk.Entry(input_window, width=50)
        txt_course_id.place(x=10, y=30)

        lbl_course_name = tk.Label(input_window,
                                   text="Enter course name: ",
                                   bg="white")
        lbl_course_name.place(x=10, y=60)
        txt_course_name = tk.Entry(input_window, width=50)
        txt_course_name.place(x=10, y=80)

        lbl_course_credit = tk.Label(input_window,
                                     text="Enter course credit: ",
                                     bg="white")
        lbl_course_credit.place(x=10, y=110)
        txt_course_credit = tk.Entry(input_window, width=50)
        txt_course_credit.place(x=10, y=130)

        lbl_course_mark_mid_portion = tk.Label(input_window,
                                               text="Enter course mark mid portion: ",
                                               bg="white")
        lbl_course_mark_mid_portion.place(x=10, y=160)
        txt_course_mark_mid_portion = tk.Entry(input_window, width=50)
        txt_course_mark_mid_portion.place(x=10, y=180)

        lbl_course_mark_final_portion = tk.Label(input_window,
                                                 text="Enter course mark final portion: ",
                                                 bg="white")
        lbl_course_mark_final_portion.place(x=10, y=210)
        txt_course_mark_final_portion = tk.Entry(input_window, width=50)
        txt_course_mark_final_portion.place(x=10, y=230)

        selected_action = tk.StringVar(input_window)
        selected_action.set("add")
        lbl_action = tk.Label(input_window, text="Select action: ", bg="white")
        lbl_action.place(x=10, y=260)
        action_lst = ["add", "remove", "update"]
        option_action = tk.OptionMenu(input_window, selected_action, *action_lst)
        option_action.place(x=10, y=280)

        btn_submit = tk.Button(input_window,
                               text="Submit",
                               bg="white",
                               command=lambda: self.submit_course(
                                                    txt_course_id,
                                                    txt_course_name,
                                                    txt_course_credit,
                                                    txt_course_mark_mid_portion,
                                                    txt_course_mark_final_portion,
                                                    selected_action.get()))
        btn_submit.place(x=10, y=330)
        input_window.protocol("WM_DELETE_WINDOW", input_window.destroy)

    #submit course info
    def submit_course(self,
                      txt_course_id,
                      txt_course_name,
                      txt_course_credit,
                      txt_course_mark_mid_portion,
                      txt_course_mark_final_portion,
                      action):
        course_id = str(txt_course_id.get())
        course_name = str(txt_course_name.get())
        course_credit = str(txt_course_credit.get())
        course_mark_mid_portion = int(txt_course_mark_mid_portion.get())
        course_mark_final_portion = int(txt_course_mark_final_portion.get())

        if action == "add":
            if any(course.get_id() == course_id for course in self.__course_list):
                raise ValueError("Course ID already exists")
            course = Course(course_id,
                            course_name,
                            course_credit,
                            course_mark_mid_portion,
                            course_mark_final_portion)
            self.__course_list.append(course)
            print("Course added successfully")

        elif action == "remove":
            new_course_list_tmp = []
            for course in self.__course_list:
                if course.get_id() == course_id:
                    continue
                new_course_list_tmp.append(course)
            self.__course_list.clear()
            for course in new_course_list_tmp:
                self.__course_list.append(course)
            print("Course removed successfully")

        elif action == "update":
            for course in self.__course_list:
                if course.get_id() == course_id:
                    course.set_name(course_name)
                    course.set_credit(course_credit)
                    course.set_mark_mid_portion(course_mark_mid_portion)
                    course.set_mark_final_portion(course_mark_final_portion)
                    break
            print("Course updated successfully")

        else:
            raise ValueError("Invalid action")

        txt_course_id.delete(0, tk.END)
        txt_course_name.delete(0, tk.END)
        txt_course_credit.delete(0, tk.END)
        txt_course_mark_mid_portion.delete(0, tk.END)
        txt_course_mark_final_portion.delete(0, tk.END)

    #==================================================================================================
    # 3. Input mark(add, remove, update)
    '''input student id, course id, mark, action(add, remove, update)
    if action is add, then add mark
    if action is remove, then remove mark with student id and course id
    if action is update, then update mark with student id and course id
    '''
    def input_mark(self):
        input_window = tk.Toplevel(self.menu_window)
        input_window.title("Add/Remove/Update mark")
        input_window.geometry("450x400")
        input_window.resizable(True, True)
        input_window.configure(bg="white")

        lbl_student_id = tk.Label(input_window,
                                  text="Enter student id: ",
                                  bg="white")
        lbl_student_id.place(x=10, y=10)
        txt_student_id = tk.Entry(input_window, width=50)
        txt_student_id.place(x=10, y=30)

        lbl_course_id = tk.Label(input_window,
                                 text="Enter course id: ",
                                 bg="white")
        lbl_course_id.place(x=10, y=60)
        txt_course_id = tk.Entry(input_window, width=50)
        txt_course_id.place(x=10, y=80)

        lbl_mark_mid = tk.Label(input_window,
                                text="Enter mark mid: ",
                                bg="white")
        lbl_mark_mid.place(x=10, y=110)
        txt_mark_mid = tk.Entry(input_window, width=50)
        txt_mark_mid.place(x=10, y=130)

        lbl_mark_final = tk.Label(input_window,
                                  text="Enter mark final: ",
                                  bg="white")
        lbl_mark_final.place(x=10, y=160)
        txt_mark_final = tk.Entry(input_window, width=50)
        txt_mark_final.place(x=10, y=180)

        selected_action = tk.StringVar(input_window)
        selected_action.set("add")
        lbl_action = tk.Label(input_window, text="Select action: ", bg="white")
        lbl_action.place(x=10, y=210)
        action_lst = ["add", "remove", "update"]
        option_action = tk.OptionMenu(input_window, selected_action, *action_lst)
        option_action.place(x=10, y=230)

        #submit button
        btn_submit = tk.Button(input_window,
                               text="Submit",
                               bg="white",
                               command=lambda: self.submit_mark(
                                                    txt_student_id,
                                                    txt_course_id,
                                                    txt_mark_mid,
                                                    txt_mark_final,
                                                    selected_action.get()))
        btn_submit.place(x=10, y=280)
        input_window.protocol("WM_DELETE_WINDOW", input_window.destroy)

    #submit mark info
    def submit_mark(self,
                    txt_student_id,
                    txt_course_id,
                    txt_mark_mid,
                    txt_mark_final,
                    action):
        student_id = str(txt_student_id.get())
        course_id = str(txt_course_id.get())
        mark_mid = float(txt_mark_mid.get())
        mark_final = float(txt_mark_final.get())

        if action == "add":
            if any(mark.get_student_id() == student_id
                   and mark.get_course_id() == course_id for mark in self.__mark_list):
                raise ValueError("Student ID and Course ID already exists")
            mark = Mark(student_id,
                        course_id,
                        mark_mid,
                        mark_final)
            self.__mark_list.append(mark)
            print("Mark added successfully")

        elif action == "remove":
            new_mark_list_tmp = []
            for mark in self.__mark_list:
                if mark.get_student_id() == student_id and mark.get_course_id() == course_id:
                    continue
                new_mark_list_tmp.append(mark)
            self.__mark_list.clear()
            for mark in new_mark_list_tmp:
                self.__mark_list.append(mark)
            print("Mark removed successfully")

        elif action == "update":
            for mark in self.__mark_list:
                if mark.get_student_id() == student_id and mark.get_course_id() == course_id:
                    mark.set_mark_mid(mark_mid)
                    mark.set_mark_final(mark_final)
                    break
            print("Mark updated successfully")

        txt_student_id.delete(0, tk.END)
        txt_course_id.delete(0, tk.END)
        txt_mark_mid.delete(0, tk.END)
        txt_mark_final.delete(0, tk.END)
    #==================================================================================================
    '''load data from file'''
    def File2List(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data

    #load data
    def load_data(self):
        input_window = tk.Toplevel(self.menu_window)
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
        lbl_notify1 = tk.Label(input_window,
                               text="Load student_data successfully",
                               bg="white")
        lbl_notify1.place(x=10, y=10)
        data2 = self.File2List(filename2)
        for i in data2:
            course = Course(i.get_id(),
                            i.get_name(),
                            i.get_credit(),
                            i.get_mark_mid_portion(),
                            i.get_mark_final_portion())
            self.__course_list.append(course)
        lbl_notify2 = tk.Label(input_window,
                               text="Load course_data successfully",
                               bg="white")
        lbl_notify2.place(x=10, y=40)
        data3 = self.File2List(filename3)
        for i in data3:
            mark = Mark(i.get_student_id(),
                        i.get_course_id(),
                        i.get_mark_mid(),
                        i.get_mark_final())
            self.__mark_list.append(mark)
        lbl_notify3 = tk.Label(input_window,
                               text="Load mark_data successfully",
                               bg="white")
        lbl_notify3.place(x=10, y=70)
        input_window.protocol("WM_DELETE_WINDOW", input_window.destroy)
    #==================================================================================================