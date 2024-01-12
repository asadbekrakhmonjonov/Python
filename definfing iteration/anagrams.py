def anagrams(string1,string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        print(True)
    else:
        print(False)
if __name__=="__main__":
    anagrams("meta","tame")