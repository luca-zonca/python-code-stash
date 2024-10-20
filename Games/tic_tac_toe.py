import random

def clear_output():
    print("\033[H\033[J", end="")

# BOARD SET UP
def display_board(board):
    clear_output()
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   " + "|" + "   " + "|" + "   ")
    print("------------")
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   " + "|" + "   " + "|" + "   ")
    print("------------")
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   " + "|" + "   " + "|" + "   ")
    
# ASSIGNING X OR O TO PLAYERS
def player_input():
    marker = ""
     
    while marker != "X" and marker != "O":
        marker = input("\nPlayer 1, choose X or O: ").upper()
    
    if marker == "X":
       return ("X", "O")
    else:
       return ("O", "X")

# ASSIGNING MARKER TO DESIRED POSITION
def place_marker(board, marker, position):
    board[position] = marker

# DEFINING WIN CONDITIONS
def win_check(board,marker):
    return (
    (board[1] == marker and board[2] == marker and board[3] == marker) or   # HORIZONTAL
    (board[4] == marker and board[5] == marker and board[6] == marker) or   # HORIZONTAL
    (board[7] == marker and board[8] == marker and board[9] == marker) or   # HORIZONTAL
    (board[1] == marker and board[4] == marker and board[7] == marker) or   # VERTICAL
    (board[2] == marker and board[5] == marker and board[8] == marker) or   # VERTICAL
    (board[3] == marker and board[6] == marker and board[9] == marker) or   # VERTICAL
    (board[1] == marker and board[5] == marker and board[9] == marker) or   # DIAGONAL
    (board[3] == marker and board[5] == marker and board[7] == marker)      # DIAGONAL
    )

# RANDOMLY DECIDING WHO GOES FIRST
def choose_first():
    first = random.randint(1,2)
    if first == 1:
        return "Player 1"
    else:
        return "Player 2"

# CHECKING FOR EMPTY SPACES ON THE BOARD        
def space_check(board,position):
    return board[position] not in ["X", "O"]

# CHECKING IF THE BOARD IS FULL
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# ASKING FOR PLAYER'S NEXT MOVE
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
        
    return position

# ASKING FOR REMATCH
def replay():
    choice = ""

    while choice not in ["Y", "y", "N", "n"]:
        choice = input("Do you want to play again (Y/N)? ")
    
    if choice == "Y" or choice == "y":
        return True
    else:
        return False

print("WELCOME TO TIC-TAC-TOE")
while True:
    game_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " goes first")
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':  # PLAYER 1 TURN 
            # SHOW THE BOARD            
            display_board(game_board)
            # CHOOSE THE POSITION
            position = player_choice(game_board)
            # PLACE THE MARKER ON THE BOARD
            place_marker(game_board, player1_marker, position)

            # CHECK IF THEY WON
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print("PLAYER 1 WON")
                game_on = False
            # CHECK IF THERE'S A TIE
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('TIE GAME')
                    game_on = False
                # NO TIE AND NO WIN -> PLAYER 2 TURN
                else:
                    turn = 'Player 2'

        else: # PLAYER 2 TURN       
            # SHOW THE BOARD
            display_board(game_board)
            # CHOOSE THE POSITION
            position = player_choice(game_board)
            # PLACE THE MARKER ON THE BOARD
            place_marker(game_board, player2_marker, position)

            # CHECK IF THEY WON
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('PLAYER 2 WON')
                game_on = False
            # CHECK IF THERE'S A TIE
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('TIE GAME')
                    game_on = False
                # NO TIE AND NO WIN -> PLAYER 1 TURN
                else:
                    turn = 'Player 1'

    if not replay():
        break
