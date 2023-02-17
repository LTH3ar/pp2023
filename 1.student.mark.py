students = []
courses = []
marks = {}


#input student
def input_student():
    print("Enter student details:")
    student_id = str(input("Student ID: "))
    student_name = str(input("Student name: "))
    dob = str(input("Date of birth (DD-MM-YYYY): "))
    students.append({"student_id": student_id, "student_name": student_name, "dob": dob})
    print(f"Student {student_id} {student_name} added.")


#input course
def input_course():
    print("Enter course details:")
    course_id = str(input("Course ID: "))
    course_name = str(input("Course name: "))
    courses.append({"course_id": course_id, "course_name": course_name})
    marks[course_id] = {}
    for student in students:
        marks[course_id][student["student_id"]] = "N/A"
    print(f"Course {course_id} {course_name} added.")


#input mark
def input_mark():
    print("Enter mark details:")
    course_id = input("Course ID: ")
    student_id = input("Student ID: ")
    mark = float(input("Mark: "))
    marks[course_id][student_id] = mark
    print(f"Mark added for student ID {student_id} in course ID {course_id}.")


#output report
def output_report(): #this function is not totally mine because I'm bad at handling visual stuff
    print("\nChoose a course:")
    for course in courses:
        print(f"{course['course_id']}. {course['course_name']}")
    course_id = str(input("Option: "))
    print(f"\nReport for course :")

    #show course info
    for course in courses:
        if course_id == course["course_id"]:
            print(f"{course['course_id']}. {course['course_name']}")

    print("{:<10} {:<20} {:<15} {:<10}".format("ID", "Name", "Date of Birth", "Mark"))
    for student in students:
        mark = marks[course_id][student['student_id']]
        print("{:<10} {:<20} {:<15} {:<10}".format(student['student_id'], student['student_name'], student['dob'], mark))

if __name__ == "__main__":
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
            for i in range(0,n):
                input_student()
        elif option == 2:
            input_course()
        elif option == 3:
            input_mark()
        elif option == 4:
            output_report()
        elif option == 5:
            break
        else:
            print("Invalid option. Try again.")
    exit()
