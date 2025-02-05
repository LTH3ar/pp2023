class Student:
    def __init__(self, student_id, student_name, dob):
        self.id = student_id
        self.name = student_name
        self.dob = dob


class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name
        self.marks = {}

    def input_mark(self, student_id, mark):
        self.marks[student_id] = mark


class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.in_no_student = int(0)

    def input_student(self):
        print("\nEnter student details:")
        student_id = str(input("Student ID: "))
        student_name = str(input("Student name: "))
        dob = str(input("Date of birth (DD-MM-YYYY): "))
        student = Student(student_id, student_name, dob)
        self.students.append(student)
        print(f"Student {student_name} added.")

    def input_course(self):
        print("Enter course details:")
        course_id = str(input("Course ID: "))
        course_name = str(input("Course name: "))
        course = Course(course_id, course_name)
        self.courses.append(course)
        for student in self.students:
            course.input_mark(student.id, "N/A")
        print(f"Course {course_name} added.")

    def input_mark(self):
        print("Enter mark details:")
        for course in self.courses:
            print(f"{course.id}. {course.name}")
        course_id = str(input("Course ID: "))
        in_no_student = int(input("Number of students: "))
        if 1 <= in_no_student <= len(self.students):
            for num in range(0, in_no_student):
                student_id = str(input("\nStudent ID: "))
                mark = float(input("Mark: "))
                for course in self.courses:
                    if course.id == course_id:
                        course.input_mark(student_id, mark)
                        print(f"Mark added for student ID {student_id} in course ID {course_id}.")

        else:
            print("\nInvalid number of students.\n")

    def print_report(self):
        print("Choose a course:")
        for course in self.courses:
            print(f"{course.id}. {course.name}")
        course_id = str(input("Option: "))
        for course in self.courses:
            if course.id == course_id:
                print(f"\nID: {course.id}: {course.name}")
                print(f"\nReport for {course.name}:")
                print("{:<10} {:<20} {:<15} {:<10}".format("ID", "Name", "Date of Birth", "Mark"))
                for student in self.students:
                    mark = course.marks[student.id]
                    print("{:<10} {:<20} {:<15} {:<10}".format(student.id, student.name, student.dob, mark))
                return
        print(f"Course ID {course_id} not found.")


if __name__ == "__main__":
    sm = StudentManagement()
    while True:
        print("\nChoose an option:")
        print("1. Add student")
        print("2. Add course")
        print("3. Add mark")
        print("4. Print report")
        print("5. Exit")
        option = int(input("Option: "))

        if option == 1:
            n = int(input("Number of students: "))
            for i in range(0, n):
                sm.input_student()
        elif option == 2:
            n = int(input("Number of courses: "))
            for i in range(0, n):
                sm.input_course()
        elif option == 3:
            sm.input_mark()
        elif option == 4:
            sm.print_report()
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")
