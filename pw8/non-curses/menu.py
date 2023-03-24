from StudentManagement import StudentManagement
import subprocess
class Menu:
    def __init__(self):
        self.student_management = StudentManagement()

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
        subprocess.call("clear", shell=True)

        for option in options:
            print(option)

        print("\n")
        choice = input("Enter your choice: ")
        if str(choice) == "":
            return
        self.student_management.option_select(int(choice))

    def main(self):
        while True:
            self.menu()