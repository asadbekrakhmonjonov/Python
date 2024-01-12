def line(length):
    string = "#"
    print(string * length)
def triangle(length):
    number = 1
    while 0 < number <= length:
        line(number)
        number += 1
if __name__=="__main__":
    triangle(6)