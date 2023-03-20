import pickle
import tkinter as tk
import time
import os

class Output:
    def __init__(self, student_list, course_list, mark_list):
        self.__student_list = student_list
        self.__course_list = course_list
        self.__mark_list = mark_list

    # getters
    def get_student_list(self):
        return self.__student_list

    def get_course_list(self):
        return self.__course_list

    def get_mark_list(self):
        return self.__mark_list

    def output_students_list(self):
        output_tk_window = tk.Toplevel()
        #rewrite the above code to use tkinter
        output_tk_window.title("Student List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        self.scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        self.scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        self.scrollbar = tk.Scrollbar(output_tk_window)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        self.scroll_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scroll_list.yview)

        #add data to scroll list
        for i in self.__student_list:
            self.scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
            self.scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
            self.scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
            self.scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
            self.scroll_list.insert(tk.END, " ")


    def output_courses_list(self):
        output_tk_window = tk.Toplevel()
        #the same for courses and marks
        output_tk_window.title("Course List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        self.scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        self.scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        self.scrollbar = tk.Scrollbar(output_tk_window)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        self.scroll_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scroll_list.yview)

        #add data to scroll list
        for i in self.__course_list:
            self.scroll_list.insert(tk.END, "Course_ID: " + str(i.get_id()))
            self.scroll_list.insert(tk.END, "Course_Name: " + str(i.get_name()))
            self.scroll_list.insert(tk.END, "Credit: " + str(i.get_credit()))
            self.scroll_list.insert(tk.END, "Mid_%: " + str(i.get_mark_mid_portion()))
            self.scroll_list.insert(tk.END, "Final_%: " + str(i.get_mark_final_portion()))
            self.scroll_list.insert(tk.END, " ")


    def output_marks_list(self):
        output_tk_window = tk.Toplevel()
        #the same for courses and marks
        output_tk_window.title("Mark List")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        self.scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        self.scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        self.scrollbar = tk.Scrollbar(output_tk_window)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        self.scroll_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scroll_list.yview)

        #add data to scroll list
        for i in self.__mark_list:
            self.scroll_list.insert(tk.END, "Student_ID: " + str(i.get_student_id()))
            self.scroll_list.insert(tk.END, "Course_ID: " + str(i.get_course_id()))
            self.scroll_list.insert(tk.END, "Midterm: " + str(i.get_mark_mid()))
            self.scroll_list.insert(tk.END, "Final: " + str(i.get_mark_final()))
            self.scroll_list.insert(tk.END, " ")

    def output_student(self, student_id):
        output_tk_window = tk.Toplevel()
        #the same for courses and marks
        output_tk_window.title("Student")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        self.scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        self.scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        self.scrollbar = tk.Scrollbar(output_tk_window)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        self.scroll_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scroll_list.yview)

        #add data to scroll list
        for i in self.__student_list:
            if i.get_id() == student_id:
                self.scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
                self.scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
                self.scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
                self.scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
                self.scroll_list.insert(tk.END, " ")

    def output_course(self, course_id):
        output_tk_window = tk.Toplevel()
        #the same for courses and marks
        output_tk_window.title("Course")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        self.scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        self.scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        self.scrollbar = tk.Scrollbar(output_tk_window)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        self.scroll_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scroll_list.yview)

        #add data to scroll list
        for i in self.__course_list:
            if i.get_id() == course_id:
                self.scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
                self.scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
                self.scroll_list.insert(tk.END, "Credit: " + str(i.get_credit()))
                self.scroll_list.insert(tk.END, "Mid_%: " + str(i.get_mark_mid_portion()))
                self.scroll_list.insert(tk.END, "Final_%: " + str(i.get_mark_final_portion()))
                self.scroll_list.insert(tk.END, " ")


    def output_mark(self, student_id, course_id):
        output_tk_window = tk.Toplevel()
        #the same for courses and marks
        output_tk_window.title("Mark")
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        #add a scroll list
        self.scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        self.scroll_list.grid(row=0, column=0, padx=10, pady=10)

        #add a scrollbar
        self.scrollbar = tk.Scrollbar(output_tk_window)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        #add scrollbar to scroll list
        self.scroll_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scroll_list.yview)

        #add data to scroll list
        for i in self.__mark_list:
            if i.get_student_id() == student_id and i.get_course_id() == course_id:
                self.scroll_list.insert(tk.END, "Student ID: " + str(i.get_student_id()))
                self.scroll_list.insert(tk.END, "Course ID: " + str(i.get_course_id()))
                self.scroll_list.insert(tk.END, "Midterm: " + str(i.get_mark_mid()))
                self.scroll_list.insert(tk.END, "Final: " + str(i.get_mark_final()))
                self.scroll_list.insert(tk.END, " ")


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

    def export_data_daemon(self):
        time.sleep(1)
        filename1 = "students_data_tmp.dt"
        filename2 = "courses_data_tmp.dt"
        filename3 = "marks_data_tmp.dt"
        self.List2File(filename1, self.__student_list)
        self.List2File(filename2, self.__course_list)
        self.List2File(filename3, self.__mark_list)

    def export_data_rename(self):
        filename1 = "students_data_tmp.dt"
        filename2 = "courses_data_tmp.dt"
        filename3 = "marks_data_tmp.dt"
        os.rename(filename1, "students_data.dt")
        os.rename(filename2, "courses_data.dt")
        os.rename(filename3, "marks_data.dt")


#    def __del__(self):
#        self.output_tk_window.destroy()