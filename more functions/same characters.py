try:
    def same_chars(string,a,b):
        if string[a] == string[b]:
            return True
        elif a > len(string) or b > len(string):
            return False
        else:
            return False
    print(same_chars("programmer",1, 9))
except IndexError:
    print("False")