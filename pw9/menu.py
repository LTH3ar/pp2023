from StudentManagement import StudentManagement
import curses
import tkinter as tk

class Menu:
    def __init__(self):
        self.student_management = StudentManagement()
        self.menu_window = self.student_management.sm_window
        self.choice = int(0)

    def set_choice(self, num):
        self.choice = num

    def menu(self):
        #tk
        self.menu_window.title("Menu")
        self.menu_window.geometry("300x300")
        self.menu_window.resizable(True, True)
        # set output number to each button
        self.menu_window.button_1 = tk.Button(self.menu_window, text="1. Add student", command=lambda: self.set_choice(1))
        self.menu_window.button_1.pack()
        self.menu_window.button_2 = tk.Button(self.menu_window, text="2. Add course", command=lambda: self.set_choice(2))
        self.menu_window.button_2.pack()
        self.menu_window.button_3 = tk.Button(self.menu_window, text="3. Add mark", command=lambda: self.set_choice(3))
        self.menu_window.button_3.pack()
        self.menu_window.button_4 = tk.Button(self.menu_window, text="4. Output students list", command=lambda: self.set_choice(4))
        self.menu_window.button_4.pack()
        self.menu_window.button_5 = tk.Button(self.menu_window, text="5. Output courses list", command=lambda: self.set_choice(5))
        self.menu_window.button_5.pack()
        self.menu_window.button_6 = tk.Button(self.menu_window, text="6. Output marks list", command=lambda: self.set_choice(6))
        self.menu_window.button_6.pack()
        self.menu_window.button_7 = tk.Button(self.menu_window, text="7. Output student", command=lambda: self.set_choice(7))
        self.menu_window.button_7.pack()
        self.menu_window.button_8 = tk.Button(self.menu_window, text="8. Output course", command=lambda: self.set_choice(8))
        self.menu_window.button_8.pack()
        self.menu_window.button_9 = tk.Button(self.menu_window, text="9. Output mark", command=lambda: self.set_choice(9))
        self.menu_window.button_9.pack()
        self.menu_window.button_10 = tk.Button(self.menu_window, text="10. GPA calculator", command=lambda: self.set_choice(10))
        self.menu_window.button_10.pack()
        self.menu_window.button_11 = tk.Button(self.menu_window, text="11. Load data", command=lambda: self.set_choice(11))
        self.menu_window.button_11.pack()
        self.menu_window.button_12 = tk.Button(self.menu_window, text="12. Export data", command=lambda: self.set_choice(12))
        self.menu_window.button_12.pack()
        self.menu_window.button_13 = tk.Button(self.menu_window, text="13. Exit", command=lambda: self.set_choice(13))
        self.menu_window.button_13.pack()
        self.menu_window.mainloop()

        self.student_management.option_select(self.choice)

    def main(self):
        while True:
            self.menu()

    def __del__(self):
        self.menu_window.destroy()