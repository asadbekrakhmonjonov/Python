def factorials(n:int):
    dictionary = {}
    dictionary["number"] = n
    result = 1
    for i in range(1,n+1,1):
        result *= i
    print(result)
factorials(3)