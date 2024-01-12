from random import randint
def lottery_numbers(amount:int,lower:int,upper:int):
    draw = []
    for i in range(amount):
            suc = randint(lower,upper)
            if suc not in draw:
                draw.append(suc)
    print(sorted(draw))
lottery_numbers(7,1,40)