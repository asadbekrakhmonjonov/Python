def suggest_clothing():
    temperature = int(input("Temperature: "))
    rain = input("\nWill it rain (yes/no): ")
    suggestion = ["\nWear jeans and a T-shirt"]
    if temperature > 20:
        for i in suggestion:
            print(i)
    if 10 < temperature <= 20:
        for i in suggestion:
            print(i)
    if 5 < temperature <= 10:
        suggestion.append("\nI recommend a jumper as well")
        for i in suggestion:
            print(i)
    if 5 <= temperature < 10:
        suggestion.append("\nTake a jacket with you")
        for i in suggestion:
            print(i)
    if 0 <= temperature < 5:
        suggestion.append("\nMake it a warm coat, actually")
        suggestion.append("\nI think gloves are in order")
        suggestion.append("\nDon't forget your umbrella!")
        for i in suggestion:
            print(i)
suggest_clothing()