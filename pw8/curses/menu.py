from StudentManagement import StudentManagement
import curses

class Menu:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.student_management = StudentManagement()

    def menu(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0
        self.stdscr.addstr(line_count, 0, "1. Add student")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "2. Add course")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "3. Add mark")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "4. Output students list")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "5. Output courses list")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "6. Output marks list")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "7. Output student")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "8. Output course")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "9. Output mark")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "10. GPA calculator")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "11. GPA ranking (Low to High)")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "12. GPA ranking (High to Low)")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "13. Load data")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "14. Export data")
        line_count += 1
        self.stdscr.addstr(line_count, 0, "15. Exit")
        line_count += 1
        lbl_choice = str("Enter your choice: ")
        self.stdscr.addstr(line_count, 0, lbl_choice)
        choice = int(self.stdscr.getstr(line_count, len(lbl_choice) + 1, 20))
        line_count += 1
        self.student_management.option_select(choice)

    def main(self):
        while True:
            self.menu()
            self.stdscr.addstr("\nPress any key to continue.")
            self.stdscr.getch()
            self.stdscr.clear()

    def __del__(self):
        curses.endwin()