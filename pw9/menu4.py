from typing import List
import tkinter as tk
import os
from StudentManagement import StudentManagement


class Menu:
    BUTTON_TEXTS: List[str] = [
        "0. Add/Remove/Update student",
        "1. Add/Remove/Update course",
        "2. Add/Remove/Update mark",
        "3. Output students list",
        "4. Output courses list",
        "5. Output marks list",
        "6. Output student",
        "7. Output course",
        "8. Output mark",
        "9. GPA calculator",
        "10. GPA ranking(descending)",
        "11. GPA ranking(ascending)",
        "12. Load data",
        "13. Export data",
        "14. Export data(direct)",
        "15. Exit",
    ]

    def __init__(self) -> None:
        self.menu_window = tk.Tk()
        self.student_management = StudentManagement(self.menu_window)
        self.frame0 = tk.Frame(self.menu_window, relief=tk.RIDGE)
        self.frame0.grid(row=0, column=0, padx=10, pady=5)
        self.frame1 = tk.Frame(self.menu_window, relief=tk.RIDGE)
        self.frame1.grid(row=0, column=1, padx=10, pady=5)
        self.frame2 = tk.Frame(self.menu_window, relief=tk.RIDGE)
        self.frame2.grid(row=0, column=2, padx=10, pady=5)
        self.frame3 = tk.Frame(self.menu_window, relief=tk.RIDGE)
        self.frame3.grid(row=0, column=3, padx=10, pady=5)


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
        self.menu_window.geometry("1250x280")
        self.menu_window.resizable(True, True)

        # divide buttons into four columns
        for i, button_text in enumerate(self.BUTTON_TEXTS):

            if 0 <= i <= 2:
                button = tk.Button(master=self.frame0, text=button_text,
                                   width=30, height=1,
                                   command=lambda i=i: self.student_management.option_select(i))
                button.grid(row=i, column=0, padx=10, pady=5)

            elif 3 <= i <= 8:
                button = tk.Button(master=self.frame1, text=button_text,
                                   width=30, height=1,
                                   command=lambda i=i: self.student_management.option_select(i))
                button.grid(row=i-3, column=0, padx=10, pady=5)
            elif 9 <= i <= 11:
                button = tk.Button(master=self.frame2, text=button_text,
                                   width=30, height=1,
                                   command=lambda i=i: self.student_management.option_select(i))
                button.grid(row=i-9, column=0, padx=10, pady=5)
            else:
                button = tk.Button(master=self.frame3, text=button_text,
                                   width=30, height=1,
                                   command=lambda i=i: self.student_management.option_select(i))
                button.grid(row=i-12, column=0, padx=10, pady=5)


    def main(self) -> None:
        self.menu()
        self.menu_window.protocol("WM_DELETE_WINDOW", self.destroy_protocol)
        self.menu_window.mainloop()
