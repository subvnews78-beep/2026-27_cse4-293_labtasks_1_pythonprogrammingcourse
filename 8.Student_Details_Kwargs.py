def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Krishna", Python=95, Maths=90, English=85)