import json
def print_persons():
    with open("handling.json") as new_file:
        data = new_file.read()
        persons = json.loads(data)
        for person in persons:
            print(person["name"],person["age"],person["hobbies"])
if __name__ == "__main__":
    print_persons()