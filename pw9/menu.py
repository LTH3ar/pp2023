from StudentManagement import StudentManagement
import os
import tkinter as tk

class Menu:
    def __init__(self):
        self.menu_window = tk.Tk()
        self.student_management = StudentManagement(self.menu_window)
        self.frame = tk.Frame(self.menu_window)
        self.frame.pack()
        self.menu_window.protocol("WM_DELETE_WINDOW", self.student_management.option_select(15))

    def destroy_protocol(self):
        if os.path.exists("students_data_tmp.dt"):
            os.remove("students_data_tmp.dt")
        if os.path.exists("courses_data_tmp.dt"):
            os.remove("courses_data_tmp.dt")
        if os.path.exists("marks_data_tmp.dt"):
            os.remove("marks_data_tmp.dt")
        self.menu_window.destroy()

    def menu(self):
        self.menu_window.title("Menu")
        self.menu_window.geometry("500x500")

        self.menu_window.resizable(True, True)
        # set output number to each button
        self.menu_window.button_1 = tk.Button(self.menu_window,
                                              text="1. Add/Remove/Update student",
                                              command=lambda: self.student_management.option_select(1))
        self.menu_window.button_1.pack()

        self.menu_window.button_2 = tk.Button(self.menu_window,
                                              text="2. Add/Remove/Update course",
                                              command=lambda: self.student_management.option_select(2))
        self.menu_window.button_2.pack()

        self.menu_window.button_3 = tk.Button(self.menu_window,
                                              text="3. Add/Remove/Update mark",
                                              command=lambda: self.student_management.option_select(3))
        self.menu_window.button_3.pack()

        self.menu_window.button_4 = tk.Button(self.menu_window,
                                              text="4. Output students list",
                                              command=lambda: self.student_management.option_select(4))
        self.menu_window.button_4.pack()

        self.menu_window.button_5 = tk.Button(self.menu_window,
                                              text="5. Output courses list",
                                              command=lambda: self.student_management.option_select(5))
        self.menu_window.button_5.pack()

        self.menu_window.button_6 = tk.Button(self.menu_window,
                                              text="6. Output marks list",
                                              command=lambda: self.student_management.option_select(6))
        self.menu_window.button_6.pack()

        self.menu_window.button_7 = tk.Button(self.menu_window,
                                              text="7. Output student",
                                              command=lambda: self.student_management.option_select(7))
        self.menu_window.button_7.pack()

        self.menu_window.button_8 = tk.Button(self.menu_window,
                                              text="8. Output course",
                                              command=lambda: self.student_management.option_select(8))
        self.menu_window.button_8.pack()

        self.menu_window.button_9 = tk.Button(self.menu_window,
                                              text="9. Output mark",
                                              command=lambda: self.student_management.option_select(9))
        self.menu_window.button_9.pack()

        self.menu_window.button_10 = tk.Button(self.menu_window,
                                               text="10. GPA calculator",
                                               command=lambda: self.student_management.option_select(10))
        self.menu_window.button_10.pack()

        self.menu_window.button_11 = tk.Button(self.menu_window,
                                               text="11. GPA ranking(descending)",
                                               command=lambda: self.student_management.option_select(11))
        self.menu_window.button_11.pack()

        self.menu_window.button_12 = tk.Button(self.menu_window,
                                               text="12. GPA ranking(ascending)",
                                               command=lambda: self.student_management.option_select(12))
        self.menu_window.button_12.pack()

        self.menu_window.button_13 = tk.Button(self.menu_window,
                                               text="13. Load data",
                                               command=lambda: self.student_management.option_select(13))
        self.menu_window.button_13.pack()

        self.menu_window.button_14 = tk.Button(self.menu_window,
                                               text="14. Export data",
                                               command=lambda: self.student_management.option_select(14))
        self.menu_window.button_14.pack()

        self.menu_window.button_15 = tk.Button(self.menu_window,
                                               text="15. Exit",
                                               command=lambda: self.student_management.option_select(15))
        self.menu_window.button_15.pack()


    def main(self):
        self.menu()
        self.menu_window.protocol("WM_DELETE_WINDOW", self.destroy_protocol)
        self.menu_window.mainloop()