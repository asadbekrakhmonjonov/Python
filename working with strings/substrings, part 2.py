word = input("Word: ")
length = len(word)
for i in range(length,0,-1):
    for j in range(i-1,length,1):
        print(word[j],end="")
    print()