def analyze_grades(grades):
    marks = []

    for student in grades:
        marks.append(grades[student])

    avg = sum(marks)/len(marks)
    highest_grade = max(marks)
    lowest_grade = min(marks)
    top_student = ''
    bottom_student = ''
    for student in grades:
        if grades[student] == highest_grade:
            top_student = student
        elif grades[student] == lowest_grade:
            bottom_student = student
        else:
            continue

    return {
            "average":avg,
            "highest":highest_grade,
            "lowest": lowest_grade,
            "top_student": top_student,
            "bottom_student": bottom_student
    }

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)