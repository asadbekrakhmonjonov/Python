def add_student(students: dict, name: str):
    students[name] = {"name": name, 'courses': []}
    return students

def add_course(students: dict, name: str, course: tuple):
    students[name]['courses'].append(course)
    return students

def print_student(students: dict, name: str):
    if name in students:
        student = students[name]
        print(f"{student['name']}:")
        for course in student['courses']:
            print(f"\t{course[0]} ({course[1]} credits)")
    else:
        print("No such person in the database")
def summary(students: dict):
    print("Database Summary:")
    for name, student in students.items():
        print(f"{student['name']}:")
        total_credits = sum(course[1] for course in student['courses'])
        print(f"\tTotal Credits: {total_credits}")
        if student['courses']:
            avg_credits = total_credits / len(student['courses'])
            print(f"\tAverage Credits per Course: {avg_credits}")
        else:
            print("\tNo courses registered for this student")
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
