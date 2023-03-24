from StudentManagement import StudentManagement
import curses

class Menu:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.student_management = StudentManagement(self.stdscr)

    def menu(self):
        options = [
            "0. Manage Students",
            "1. Manage Courses",
            "2. Manage Marks",
            "3. Show Students List",
            "4. Show Courses List",
            "5. Show Marks List",
            "6. Search Student",
            "7. Search Course",
            "8. Search Mark",
            "9. Search All Marks",
            "10. GPA Calculator",
            "11. GPA Ranking (Ascending)",
            "12. GPA Ranking (Descending)",
            "13. Load Data",
            "14. Export Data(rename)",
            "15. Export Data(direct)",
            "16. Exit",
        ]
        self.stdscr.clear()
        self.stdscr.refresh()
        line_count = 0

        for option in options:
            self.stdscr.addstr(line_count, 0, option)
            line_count += 1

        lbl_choice = str("Enter your choice: ")
        self.stdscr.addstr(line_count, 0, lbl_choice)
        choice = self.stdscr.getstr(line_count, len(lbl_choice) + 1, 20)
        line_count += 1

        if choice == b"":
            return

        self.student_management.option_select(int(choice))

    def main(self):
        while True:
            self.menu()
            self.stdscr.addstr("\nPress any key to continue.")
            self.stdscr.getch()
            self.stdscr.clear()

    def __del__(self):
        curses.endwin()