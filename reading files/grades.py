with open("grades.csv")as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(";")
        name = parts[0]
        grade = parts[1:]
        print(f"Name: {name}")
        print(f"Grades: {grade}")
    
