# from dictionaries.students import TEST_STRING, student_marks
# from dictionaries import students
# import students

#print(students.TEST_STRING)
#students.student_marks()


def switch(param):
    dictionary = {
        "student_names": students.student_names,
        "student_marks": students.student_marks,
        "teams": students.teams
    }
    if param in dictionary.keys():  # param in ["sn", "sm", "t"]
        func = dictionary[param]
    else:
        func = print
    
    return func

if __name__ == "__main__":
    func = switch("student_marks1")
    func()