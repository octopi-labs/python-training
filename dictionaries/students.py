import pprint

TEST_STRING = "HELLO"

def student_names():
    pass

def teams():
    pass

def student_marks():
    students = {}
    for count in range(1, 4):
        name = input("Enter student {} name: ".format(count))
        subjects = {}
        for sub_count in range(1, 4):
            subject = input("Enter subject {} name: ".format(sub_count))
            marks = input("Enter {} marks: ".format(subject))
            subjects[subject] = marks
        students[name] = subjects
    return students

if __name__ == "__main__":
    students = student_marks()
    pprint.pprint(students)