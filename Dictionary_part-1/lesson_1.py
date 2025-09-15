def create_student_dict(name,age,major):
    student_dict = {
            "name": name,
            "age": age,
            "major": major
    }
    return student_dict

print(create_student_dict("Jhon doe",21,"CS"))