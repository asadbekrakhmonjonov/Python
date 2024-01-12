name = input("Whom should I sign this to?: ")

file = input("Where should I save this?: ")

with open(f"{file}.txt","w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

with open(f"{file}.txt","a") as my_file3:
    my_file3.write("\nI know this")

with open(f"{file}.txt","r") as my_file2:
    print(my_file2.read())