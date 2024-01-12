import json
with open("Untitled.json") as new_file:
    data = new_file.read()
    courses = json.loads(data)
    for course in courses:
        print(course["abbreviation"])