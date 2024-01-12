def line(times):
    string = "#"
    print(string * times)
def square_of_hashes(times):
    n = times
    while n > 0:
        line(times)
        n -= 1
if __name__=="__main__":
    square_of_hashes(3)