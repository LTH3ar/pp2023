#import json


def input_student(lst):
    n = int(input("Enter number of students: "))
    for i in range(n):
        student_id = str(input("Enter student id: "))
        student_name = str(input("Enter student name: "))
        dob = str(input("Enter dob: "))
        student.append({"id": student_id, "name": student_name, "dob": dob})


def input_course(lst):
    n = int(input("Enter number of Courses: "))
    for i in range(n):
        course_id = str(input("Enter Course id: "))
        course_name = str(input("Enter Course name: "))
        course.append({"id": course_id, "name": course_name})


def input_mark(lst):
    n = str(input("Enter Course name or id: "))
    student_id = str(input("Enter student id: "))
    for i in range(len(course)):
        if n == course[i]["id"] or n == course[i]["name"]:
            print("Course: ", course[i]["id"], course[i]["name"])
            for j in range(len(student)):
                if student_id == student[j]["id"]:
                    mark = float(input("Enter mark for student: " + student[j]["id"] + " " + student[j]["name"] + ": "))
                    student[j][course[i]["id"]] = mark
            for j in range(len(student)):
                #check if student has mark for course
                if course[i]["id"] not in student[j]:
                    student[j][course[i]["id"]] = "No mark"


def table_out(lst):
    print("Student_id".ljust(15), "Student_name".ljust(15), "Student_DoB".ljust(15), end="")
    for i in range(len(course)):
        print(course[i]["id"].ljust(15), end="")
    print()
    for i in range(len(student)):
        print(student[i]["id"].ljust(15), student[i]["name"].ljust(15), student[i]["dob"].ljust(15), end="")
        for j in range(len(course)):
            print(str(student[i][course[j]["id"]]).ljust(15), end="")
        print()


def student_info_lst(lst):
    print("\n\n")
    print("Student_id".ljust(15), "Student_name".ljust(15), "Student_DoB".ljust(15))
    for i in range(len(student)):
        print(student[i]["id"].ljust(15), student[i]["name"].ljust(15), student[i]["dob"].ljust(15))

def course_info_lst(lst):
    print("\n\n")
    print("Course_id".ljust(15), "Course_name".ljust(15))
    for i in range(len(course)):
        print(course[i]["id"].ljust(15), course[i]["name"].ljust(15))


#def json_out(lst):
#    with open("student.json", "w") as f:
#        json.dump(lst, f, indent=4)


if __name__ == "__main__":
    student = []
    course = []
    sw = True
    while sw:
        print("1. Input student \n2. Input course \n3. Input mark \n4. Output \n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            input_student(student)
        elif choice == 2:
            input_course(course)
        elif choice == 3:
            input_mark(course)
        elif choice == 4:
            table_out(student)
            student_info_lst(student)
            course_info_lst(course)
            print(f"\n\n{student}")
        elif choice == 5:
            sw = False
        else:
            print("Invalid choice")

    exit()

    # output json file
    #json_out(student)
