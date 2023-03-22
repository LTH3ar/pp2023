import pickle
import tkinter as tk
import time
import os
import threading

class Output:
    def __init__(self, student_list, course_list, mark_list, menu_window):
        self.__student_list = student_list
        self.__course_list = course_list
        self.__mark_list = mark_list
        self.menu_window = menu_window

    # getters
    def get_student_list(self):
        return self.__student_list

    def get_course_list(self):
        return self.__course_list

    def get_mark_list(self):
        return self.__mark_list

    # ==================================================================================================
    def output_students_list(self):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.title("Student List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        #clear scroll list
        scroll_list.delete(0, tk.END)
        for i in self.__student_list:
            scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
            scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
            scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
            scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
            scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def output_students_list_sorted(self, lst_sorted):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.title("Student List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        for i in lst_sorted:
            scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
            scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
            scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
            scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
            scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def output_courses_list(self):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.title("Course List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        for i in self.__course_list:
            scroll_list.insert(tk.END, "Course_ID: " + str(i.get_id()))
            scroll_list.insert(tk.END, "Course_Name: " + str(i.get_name()))
            scroll_list.insert(tk.END, "Credit: " + str(i.get_credit()))
            scroll_list.insert(tk.END, "Mid_%: " + str(i.get_mark_mid_portion()))
            scroll_list.insert(tk.END, "Final_%: " + str(i.get_mark_final_portion()))
            scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def output_marks_list(self):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.title("Mark List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        for i in self.__mark_list:
            scroll_list.insert(tk.END, "Student_ID: " + str(i.get_student_id()))
            scroll_list.insert(tk.END, "Course_ID: " + str(i.get_course_id()))
            scroll_list.insert(tk.END, "Midterm: " + str(i.get_mark_mid()))
            scroll_list.insert(tk.END, "Final: " + str(i.get_mark_final()))
            scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def output_student(self, student_id):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.title("Student")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        for i in self.__student_list:
            if i.get_id() == student_id:
                scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
                scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
                scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
                scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
                scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def output_course(self, course_id):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.title("Course")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        for i in self.__course_list:
            if i.get_id() == course_id:
                scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
                scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
                scroll_list.insert(tk.END, "Credit: " + str(i.get_credit()))
                scroll_list.insert(tk.END, "Mid_%: " + str(i.get_mark_mid_portion()))
                scroll_list.insert(tk.END, "Final_%: " + str(i.get_mark_final_portion()))
                scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def output_mark(self, student_id, course_id):
        output_tk_window = tk.Toplevel()
        output_tk_window.title("Mark")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        #add data to scroll list
        for i in self.__mark_list:
            if i.get_student_id() == student_id and i.get_course_id() == course_id:
                scroll_list.insert(tk.END, "Student ID: " + str(i.get_student_id()))
                scroll_list.insert(tk.END, "Course ID: " + str(i.get_course_id()))
                scroll_list.insert(tk.END, "Midterm: " + str(i.get_mark_mid()))
                scroll_list.insert(tk.END, "Final: " + str(i.get_mark_final()))
                scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    def List2File(self, filename, lst):
        with open(filename, "wb") as file:
            pickle.dump(lst, file)

    def export_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.List2File(filename1, self.__student_list)
        self.List2File(filename2, self.__course_list)
        self.List2File(filename3, self.__mark_list)
        print("exporting data")

    def export_data_daemon(self):
        while True:
            time.sleep(3)
            filename1 = "students_data_tmp.dt"
            filename2 = "courses_data_tmp.dt"
            filename3 = "marks_data_tmp.dt"
            self.List2File(filename1, self.__student_list)
            print("exporting students data")
            self.List2File(filename2, self.__course_list)
            print("exporting courses data")
            self.List2File(filename3, self.__mark_list)
            print("exporting marks data")



    def export_data_rename(self):
        filename1 = "students_data_tmp.dt"
        filename2 = "courses_data_tmp.dt"
        filename3 = "marks_data_tmp.dt"
        os.rename(filename1, "students_data.dt")
        os.rename(filename2, "courses_data.dt")
        os.rename(filename3, "marks_data.dt")
        print("exporting data")
#==================================================================================================