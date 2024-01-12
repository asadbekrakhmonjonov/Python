def line():
    print("#" * 10)
def square_of_hashes(length):
    while length > 0:
        line()
        length -= 1
if __name__=="__main__":
    square_of_hashes(5)
