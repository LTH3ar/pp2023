import pickle
import tkinter as tk
import time
import os
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

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
    '''input: list of objects
       if-statement: check the type of object in the list
       output: a window with a scroll list to display the list of objects corresponding to the type of object
       '''
    def output_list(self, lst):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        # add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        # add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)
        #print(lst)

        # add data to scroll list
        if isinstance(lst[0], Student):
            output_tk_window.title("Student List")
            for i in lst:
                scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
                scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
                scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
                scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
                scroll_list.insert(tk.END, " ")
                #print("student")

        elif isinstance(lst[0], Course):
            output_tk_window.title("Course List")
            for i in lst:
                scroll_list.insert(tk.END, "Course_ID: " + str(i.get_id()))
                scroll_list.insert(tk.END, "Course_Name: " + str(i.get_name()))
                scroll_list.insert(tk.END, "Credit: " + str(i.get_credit()))
                scroll_list.insert(tk.END, "Mid_%: " + str(i.get_mark_mid_portion()))
                scroll_list.insert(tk.END, "Final_%: " + str(i.get_mark_final_portion()))
                scroll_list.insert(tk.END, " ")

        elif isinstance(lst[0], Mark):
            output_tk_window.title("Mark List")
            for i in lst:
                scroll_list.insert(tk.END, "Student_ID: " + str(i.get_student_id()))
                scroll_list.insert(tk.END, "Course_ID: " + str(i.get_course_id()))
                scroll_list.insert(tk.END, "Midterm: " + str(i.get_mark_mid()))
                scroll_list.insert(tk.END, "Final: " + str(i.get_mark_final()))
                scroll_list.insert(tk.END, " ")

        else:
            print("Error")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    '''input: list of student objects'''
    def output_students_list(self):
        self.output_list(self.__student_list)

    # ==================================================================================================
    '''input: list of student objects sorted by GPA'''
    def output_students_list_sorted(self, lst_sorted):
        self.output_list(lst_sorted)

    # ==================================================================================================
    '''input: list of course objects'''
    def output_courses_list(self):
        self.output_list(self.__course_list)

    # ==================================================================================================
    '''input: list of mark objects'''
    def output_marks_list(self):
        self.output_list(self.__mark_list)

    # ==================================================================================================
    '''input: list of student or course or mark objects, id
       if-statement: check the type of object in the list
       loop through the list to find the object with the same id
       output: a window with a scroll list to display the list of objects corresponding to the type of object
       '''
    def search_list(self, lst, id):
        output_tk_window = tk.Toplevel(self.menu_window)
        output_tk_window.geometry("500x500")
        output_tk_window.resizable(True, True)
        output_tk_window.configure(bg="white")

        # add a scroll list
        scroll_list = tk.Listbox(output_tk_window, width=50, height=20)
        scroll_list.grid(row=0, column=0, padx=10, pady=10)

        # add a scrollbar
        scrollbar = tk.Scrollbar(output_tk_window)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # add scrollbar to scroll list
        scroll_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=scroll_list.yview)

        # add data to scroll list
        if isinstance(lst[0], Student):
            output_tk_window.title("Student List")
            for i in lst:
                if i.get_id() == id:
                    scroll_list.insert(tk.END, "ID: " + str(i.get_id()))
                    scroll_list.insert(tk.END, "Name: " + str(i.get_name()))
                    scroll_list.insert(tk.END, "DoB: " + str(i.get_dob()))
                    scroll_list.insert(tk.END, "GPA: " + str(i.get_gpa()))
                    scroll_list.insert(tk.END, " ")

        elif isinstance(lst[0], Course):
            output_tk_window.title("Course List")
            for i in lst:
                if i.get_id() == id:
                    scroll_list.insert(tk.END, "Course_ID: " + str(i.get_id()))
                    scroll_list.insert(tk.END, "Course_Name: " + str(i.get_name()))
                    scroll_list.insert(tk.END, "Credit: " + str(i.get_credit()))
                    scroll_list.insert(tk.END, "Mid_%: " + str(i.get_mark_mid_portion()))
                    scroll_list.insert(tk.END, "Final_%: " + str(i.get_mark_final_portion()))
                    scroll_list.insert(tk.END, " ")

        elif isinstance(lst[0], Mark):
            output_tk_window.title("Mark List")
            for i in lst:
                if (i.get_course_id() == id) or (i.get_student_id() == id):
                    scroll_list.insert(tk.END, "Student_ID: " + str(i.get_student_id()))
                    scroll_list.insert(tk.END, "Course_ID: " + str(i.get_course_id()))
                    scroll_list.insert(tk.END, "Midterm: " + str(i.get_mark_mid()))
                    scroll_list.insert(tk.END, "Final: " + str(i.get_mark_final()))
                    scroll_list.insert(tk.END, " ")

        output_tk_window.protocol("WM_DELETE_WINDOW", output_tk_window.destroy)

    # ==================================================================================================
    '''input: list of student object and student id from the user'''
    def output_student(self, student_id):
        self.search_list(self.__student_list, student_id)

    # ==================================================================================================
    '''input: list of course object and course id from the user'''
    def output_course(self, course_id):
        self.search_list(self.__course_list, course_id)

    # ==================================================================================================
    '''input: list of mark object and student id from the user'''
    def output_mark_multiple(self, id):
        self.search_list(self.__mark_list, id)

    # ==================================================================================================
    '''input: list of mark object and student id, course id from the user
       loop through the list to find the object with the same student id and course id
       output: a window with a scroll list to display the list of objects corresponding to the id'''
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

    # ==================================================================================================
    def export_data(self):
        filename1 = "students_data.dt"
        filename2 = "courses_data.dt"
        filename3 = "marks_data.dt"
        self.List2File(filename1, self.__student_list)
        self.List2File(filename2, self.__course_list)
        self.List2File(filename3, self.__mark_list)
        print("exporting data")

    # ==================================================================================================
    '''export data to a temporary file continuously every 3 seconds'''
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

    # ==================================================================================================
    '''rename the temporary file to the original file name'''
    def export_data_rename(self):
        filename1 = "students_data_tmp.dt"
        filename2 = "courses_data_tmp.dt"
        filename3 = "marks_data_tmp.dt"
        os.rename(filename1, "students_data.dt")
        os.rename(filename2, "courses_data.dt")
        os.rename(filename3, "marks_data.dt")
        print("exporting data")
    #==================================================================================================