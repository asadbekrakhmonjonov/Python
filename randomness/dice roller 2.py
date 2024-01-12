import random

def play(die1: str, die2: str, times: int):
    wins_die1 = 0
    wins_die2 = 0
    ties = 0

    for _ in range(times):
        result_die1 = random.choice([die1, die2])
        result_die2 = random.choice([die1, die2])

        if result_die1 == result_die2:
            ties += 1
        elif result_die1 == die1:
            wins_die1 += 1
        else:
            wins_die2 += 1

    return wins_die1, wins_die2, ties

# Example usage:
result = play("A", "C", 1000)
print(result)

result = play("B", "B", 1000)
print(result)
