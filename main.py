#! /usr/bin/env python3
import random

# Function to display the 3D game board
def display_3d_board(boards):
    for i in range(3):
        print("\nGrid", i + 1)
        for j in range(3):
            print("-------------")
            for k in range(3):
                print("|", boards[i][j][k], "|", end=" ")
            print("\n-------------")

# Function to check for a win in the 3D game
def check_win_3d(boards, player):
    # Check along rows, columns, and diagonals in each grid
    for i in range(3):
        # Check rows and columns
        for j in range(3):
            if (boards[i][j][0] == boards[i][j][1] == boards[i][j][2] == player) or \
               (boards[i][0][j] == boards[i][1][j] == boards[i][2][j] == player):
                return True
        # Check diagonals
        if (boards[i][0][0] == boards[i][1][1] == boards[i][2][2] == player) or \
           (boards[i][0][2] == boards[i][1][1] == boards[i][2][0] == player):
            return True
    
    # Check along diagonals connecting the grids
    if (boards[0][0][0] == boards[1][1][1] == boards[2][2][2] == player) or \
       (boards[0][2][0] == boards[1][1][1] == boards[2][0][2] == player) or \
       (boards[0][0][2] == boards[1][1][1] == boards[2][2][0] == player) or \
       (boards[0][2][2] == boards[1][1][1] == boards[2][0][0] == player):
        return True

    # Check along grids
    for j in range(3):
        if (boards[0][j][0] == boards[1][j][0] == boards[2][j][0] == player) or \
           (boards[0][j][1] == boards[1][j][1] == boards[2][j][1] == player) or \
           (boards[0][j][2] == boards[1][j][2] == boards[2][j][2] == player) or \
           (boards[0][0][j] == boards[1][0][j] == boards[2][0][j] == player) or \
           (boards[0][1][j] == boards[1][1][j] == boards[2][1][j] == player) or \
           (boards[0][2][j] == boards[1][2][j] == boards[2][2][j] == player) or \
           (boards[0][0][0] == boards[1][0][0] == boards[2][0][0] == player) or \
           (boards[0][1][0] == boards[1][1][0] == boards[2][1][0] == player) or \
           (boards[0][2][0] == boards[1][2][0] == boards[2][2][0] == player) or \
           (boards[0][0][1] == boards[1][0][1] == boards[2][0][1] == player) or \
           (boards[0][1][1] == boards[1][1][1] == boards[2][1][1] == player) or \
           (boards[0][2][1] == boards[1][2][1] == boards[2][2][1] == player) or \
           (boards[0][0][2] == boards[1][0][2] == boards[2][0][2] == player) or \
           (boards[0][1][2] == boards[1][1][2] == boards[2][1][2] == player) or \
           (boards[0][2][2] == boards[1][2][2] == boards[2][2][2] == player):
            return True

    return False

# Function to check for a tie in the 3D game
def check_tie_3d(boards):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if boards[i][j][k] == " ":
                    return False
    return True

# Function to play the game
def play_game():
    boards = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(3)]
    players = [input("Enter player 1 name: "), input("Enter player 2 name: ")]
    current_player = random.choice(players)
    player_symbols = {players[0]: "X", players[1]: "O"}
    player_scores = {players[0]: 0, players[1]: 0}

    while True:
        print(f"\n{current_player}'s turn:")
        display_3d_board(boards)
        
        move = input("Enter your move (grid,row,col): ").split(",")
        grid, row, col = int(move[0]) - 1, int(move[1]) - 1, int(move[2]) - 1
        if boards[grid][row][col] != " ":
            print("Invalid move. Try again.")
            continue

        boards[grid][row][col] = player_symbols[current_player]
        
        if check_win_3d(boards, player_symbols[current_player]):
            print(f"\n{current_player} wins!")
            player_scores[current_player] += 1
            break
        elif check_tie_3d(boards):
            print("\nIt's a tie!")
            break
        
        current_player = players[(players.index(current_player) + 1) % 2]

    print("\nScores:")
    for player, score in player_scores.items():
        print(f"{player}: {score}")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("\nThanks for playing!")

# Start the game
play_game()