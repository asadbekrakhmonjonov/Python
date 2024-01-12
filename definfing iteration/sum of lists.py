def function(a, b):
    sum = []
    for i in range(len(a)):
        result = a[i] + b[i]
        sum.append(result)
    print(sum)
    return
if __name__=="__main__":
    function([1,2,3],[4,5,6])

