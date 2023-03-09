from student_management import StudentManagement
import curses


if __name__ == "__main__":

    student_management = StudentManagement()
    curses.wrapper(student_management.main())