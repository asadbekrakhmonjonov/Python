def times_ten(start_index:int,end_index:int):
    new_dictionary = {}
    new_dictionary["start_index"] = start_index
    new_dictionary["end_index"] = end_index
    for i in range(start_index,end_index+1,1):
        print(f"{i}:{i*10}",end=", ")
if __name__ =="__main__":
    d = times_ten(3, 6)
    print(d)