def avg_helper(student):
    return all(grade > 70 for grade in student['grades']) 

def transform_dataset(data):
    qualified_dict = {
        'qualified_students':{},
        'subject_summary':{}
    }
    marks_filter = filter(avg_helper,data)
    for student in marks_filter:
        qualified_dict['qualified_students'][student['student_id']] = round(sum(student['grades'])/len(student['grades']),2)
        for subject in student['subjects']:
            if subject in qualified_dict['subject_summary']:
                qualified_dict['subject_summary'][subject] += 1
            else:
                qualified_dict['subject_summary'][subject] = 1
    print(qualified_dict)




    
data = [
    {
        "student_id": "S123", 
        "grades": [88, 92, 85], 
        "subjects": ["Math", "Science", "History"]
    },
    {
        "student_id": "S124", 
        "grades": [65, 95, 80], 
        "subjects": ["Math", "Science", "English"]
    },
    {
        "student_id": "S125", 
        "grades": [91, 89, 92], 
        "subjects": ["Math", "Physics", "History"]
    }
]
transform_dataset(data)
