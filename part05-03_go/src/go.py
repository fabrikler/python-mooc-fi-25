def who_won(game_board: list):

    player1 = 0
    player2 = 0

    for row in game_board:
        for i in row:
            if i == 1:
                player1 += 1
            if i == 2:
                player2 += 1
    
    if player1 > player2:
        return 1
    if player2 > player1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    game_bord = [
        [1, 1, 1, 1, 1, 2, 2, 2, 2],
        [1, 1, 1, 1, 2, 2, 2, 2, 2],
        [1, 1, 1, 0, 0, 2, 2, 2, 2],
        [1, 1, 0, 0, 0, 0, 2, 2, 2],
        [1, 0, 0, 1, 1, 0, 0, 2, 2],
        [1, 0, 1, 1, 1, 1, 0, 0, 2],
        [1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
