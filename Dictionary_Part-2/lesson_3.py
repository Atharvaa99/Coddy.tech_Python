def print_employee_details(employee_data):
    if not employee_data:
        print("No data available")
    else:
        for key,value in employee_data.items():
            print(f"{key}: {value}")