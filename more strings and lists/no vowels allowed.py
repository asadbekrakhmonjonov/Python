def no_vowels(my_string):
    vowels = ['a','e','i','o','u','y']
    for vowel in vowels:
        my_string = my_string.replace(vowel,"")
    print(my_string)
if __name__=="__main__":
    no_vowels("this is an example")