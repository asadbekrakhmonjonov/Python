""" Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line. """
def ask():
    number = int(input("Please type in a positive integer: "))
    for i in range(-4,number+1,1):
        print(i)
if __name__=="__main__":
    ask()