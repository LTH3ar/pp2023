from StudentManagement import StudentManagement
import tkinter as tk
import threading

class Menu:
    def __init__(self):
        self.menu_window = tk.Tk()
        self.student_management = StudentManagement()

    def menu(self):
        self.menu_window.title("Menu")
        self.menu_window.geometry("500x500")
        self.menu_window.resizable(True, True)
        # set output number to each button
        self.menu_window.button_1 = tk.Button(self.menu_window,
                                              text="1. Add student",
                                              command=lambda: self.student_management.option_select(1))
        self.menu_window.button_1.pack()
        self.menu_window.button_2 = tk.Button(self.menu_window,
                                              text="2. Add course",
                                              command=lambda: self.student_management.option_select(2))
        self.menu_window.button_2.pack()
        self.menu_window.button_3 = tk.Button(self.menu_window,
                                              text="3. Add mark",
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
                                               text="11. Load data",
                                               command=lambda: self.student_management.option_select(11))
        self.menu_window.button_11.pack()
        self.menu_window.button_12 = tk.Button(self.menu_window,
                                               text="12. Export data",
                                               command=lambda: self.student_management.option_select(12))
        self.menu_window.button_12.pack()
        self.menu_window.button_13 = tk.Button(self.menu_window,
                                               text="13. Exit",
                                               command=lambda: self.student_management.option_select(13))
        self.menu_window.button_13.pack()
        self.menu_window.mainloop()

    def main(self):
        self.menu()
