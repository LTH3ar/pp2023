from student_management import StudentManagement
import curses

class Menu:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.student_management = StudentManagement()

    def display_menu(self):
        self.stdscr.clear()
        line_count = int(0)
        self.stdscr.addstr(line_count, 0, "Student management system:")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "1. Input student")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "2. Input course")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "3. Input mark")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "4. Calculate GPA & ranking")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "5. Display student")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "6. Display course")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "7. Display mark")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "8. Exit(discard data)")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "Enter your choice: ")
        line_count += 1
        self.student_management.option_lst()

    def main(self):
        while True:
            self.display_menu()
            self.stdscr.addstr("\nPress any key to continue.")
            self.stdscr.getch()
            self.stdscr.clear()

    def __del__(self):
        curses.endwin()