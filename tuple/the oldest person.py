def oldest_person(people: list):
    biggest = people[0]
    for person in people:
        if person[1] < biggest[1]: 
            biggest = person
    return biggest[0]

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))
