def line(times, string):
    if string == "":
        print(times * "*")
    else:
        print(string * times)
if __name__=="__main__":
    line(7, "")
    line(10, "LOL")
    line(3,"")