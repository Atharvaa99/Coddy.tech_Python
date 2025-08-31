age = int(input())
has_license = input().lower() == "true"
has_insurance = input().lower() == "true"

result = age >= 18 and has_insurance == True and has_license == True

print(result)