def player_move(n, player):
    print(f"{player}, it's your turn. Current value: {n}")
    move = int(input("Enter 1 to subtract 1 or 2 to divide by 2: "))
    if move == 1:
        return n - 1
    elif move == 2:
        return n // 2
    else:
        print("Invalid move. Try again.")
        return player_move(n, player)

def play_game(n):
    turn = 0  # 0 for player 1, 1 for player 2
    while n > 0:
        if turn == 0:
            n = player_move(n, "Player 1")
            print(f"Player 1 moves, new value: {n}")
            if n == 0:
                print("Player 1 wins!")
                return
            turn = 1
        else:
            n = player_move(n, "Player 2")
            print(f"Player 2 moves, new value: {n}")
            if n == 0:
                print("Player 2 wins!")
                return
            turn = 0

if __name__ == "__main__":
    N = int(input("Enter the starting number N: "))
    play_game(N)