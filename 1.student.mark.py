import json


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
    for i in range(len(course)):
        if n == course[i]["id"] or n == course[i]["name"]:
            print("Course: ", course[i]["id"], course[i]["name"])
            for j in range(len(student)):
                mark = float(input("Enter mark for student: " + student[j]["id"] + " " + student[j]["name"] + ": "))
                student[j][course[i]["id"]] = mark
        elif n in range(len(course)) and n != course[i]["id"] or n != course[i]["name"]:
            for j in range(len(student)):
                mark = str("No mark")
                student[j][course[i]["id"]] = mark
        else:
            print("No course found")
            exit()


def json_out(lst):
    with open("student.json", "w") as f:
        json.dump(lst, f, indent=4)


if __name__ == "__main__":
    # input number of students
    student = []
    input_student(student)

    # input number of courses
    course = []
    input_course(course)

    # choose course input mark for each student in student list
    input_mark(course)

    # plain output
    #print(student)
    #print(course)

    #course info
    print("\n\n")
    print("Course_id".ljust(15), "Course_name".ljust(15))
    for i in range(len(course)):
        print(course[i]["id"].ljust(15), course[i]["name"].ljust(15))

    #student info
    print("\n\n")
    print("Student_id".ljust(15), "Student_name".ljust(15), "Student_DoB".ljust(15))
    for i in range(len(student)):
        print(student[i]["id"].ljust(15), student[i]["name"].ljust(15), student[i]["dob"].ljust(15))

    # output in table format, use course name as header
    print("\n\n")
    print("Student_id".ljust(15), "Student_name".ljust(15), "Student_DoB".ljust(15), end="")
    for i in range(len(course)):
        print(course[i]["id"].ljust(15), end="")
    print()
    for i in range(len(student)):
        print(student[i]["id"].ljust(15), student[i]["name"].ljust(15), student[i]["dob"].ljust(15), end="")
        for j in range(len(course)):
            print(str(student[i][course[j]["id"]]).ljust(15), end="")
        print()

    # output json file
    json_out(student)
