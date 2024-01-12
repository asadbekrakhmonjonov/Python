def who_won(game_board):
    player1_count = sum(row.count(1) for row in game_board)
    player2_count = sum(row.count(2) for row in game_board)

    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0

# Example usage:
board = [
    [1, 0, 2, 0, 1],
    [2, 1, 1, 2, 0],
    [0, 2, 0, 0, 1],
    [1, 0, 2, 1, 2],
    [2, 1, 0, 2, 1]
]

result = who_won(board)
print(f"The winner is Player {result}")
