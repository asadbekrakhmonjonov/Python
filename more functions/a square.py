def line(string, length):
    print(string * length)
def square(string,length):
    number = length
    while number > 0:
        line(string, length)
        number -= 1
if __name__=="__main__":
    square("*",5)
    square("o",3)