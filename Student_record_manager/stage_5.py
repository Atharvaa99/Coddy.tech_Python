student_records = {}

def add_student(name,age,courses):
    if name in student_records:
        print(f"Student {name} already exists.")
    else:
        student_records[name] = {
                "age": age,
                "grades": set(),
                "courses":set(courses)
        }
        print(f"Student '{name}' added successfully.")

def add_grade(name,grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name,course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]["courses"]:
            return True
        else:
            return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return "None"
    else:
        sum = 0
        for grade in student_records[name]["grades"]:
            sum += grade
        avg:float = sum / len(student_records[name]["grades"])
        return avg


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again