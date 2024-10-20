import random

choices = ["rock", "paper", "scissors"]

ascii_art = {
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''',
    "paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''',
    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''
}   # ASCII VISUALIZATION OF ROCK, PAPER, SCISSORS

def clear_output():
    """
    Clears the console output. Works for most terminal environments.
    """
    try:
        print("\033[H\033[J", end="")
    except:
        pass

def game_mode():
    """
    Prompts the user to choose the game mode (Best of 3 or Best of 5)
    
    Returns:
        int: The number of rounds to be played
    """
    choice = ""
    acceptable = ["3", "5"]
    
    while choice not in acceptable:
        choice = input("Best of 3 or Best of 5? ")
        if choice not in acceptable:
            print("\nInvalid output. Please insert 3 or 5")
    
    return int(choice)

def computer_choice():
    """
    Randomly selects a choice for the computer from 'rock', 'paper', or 'scissors'.
    
    Returns:
        str: The computer's choice.
    """
    return random.choice(choices)
    
def get_player_choice():
    """
    Prompts the user to choose between 'rock', 'paper', or 'scissors'.
    
    Returns:
        str: The player's choice.
    """
    player = ""
    acceptable = ["rock", "r", "paper", "p", "scissors", "s"]
    
    while player not in acceptable:
        try:
            player = input("Rock, paper, scissors\n").lower()
        except Exception as e:
            print(f"Error getting player's choice: {e}")
            continue
        
        if player not in acceptable:
            print("\nInvalid output. Please insert one of the following: r or rock, p or paper, s or scissors")
        
    if player == "r":
        player = "rock"
    elif player == "p":
        player = "paper"
    elif player == "s":
        player = "scissors"
       
    return player

def check_winner(player, computer, player_score_counter, computer_score_counter):
    """
    Checks the winner of a round and updates the score counters.
    
    Args:
        player (str): The player's choice.
        computer (str): The computer's choice.
        player_score_counter (int): The current score of the player.
        computer_score_counter (int): The current score of the computer.
    
    Returns:
        tuple: Updated player and computer score counters.
    """
    winning_conditions = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
    
    if player == computer:
        print("Tie")
    elif (player, computer) in winning_conditions:
        print("You win the round")
        player_score_counter += 1
    else:
        print("Computer wins the round")
        computer_score_counter += 1
        
    
    return player_score_counter, computer_score_counter
        
def replay():
    """
    Asks the user if they want to play again.
    
    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    play_again_choice = ""
    acceptable = ["yes", "y", "no", "n"]
    
    while play_again_choice not in acceptable:
        play_again_choice = input("Play again? ").lower()
    
    return play_again_choice in ["yes", "y"]

print("WELCOME TO ROCK, PAPER, SCISSORS")

# MAIN GAME LOOP    
while True:
    player_score_counter = 0
    computer_score_counter = 0
    num_rounds = game_mode()
    required_wins = (num_rounds // 2) + 1
    clear_output()
    
    # BEST OF 3/5 LOOP
    while player_score_counter < required_wins and computer_score_counter < required_wins: 
        player = get_player_choice()
        computer = computer_choice()
        clear_output()
        
        print(f"Player chose:\n{ascii_art[player]}")
        print(f"Computer chose:\n{ascii_art[computer]}")
        
        player_score_counter, computer_score_counter = check_winner(player, computer, player_score_counter, computer_score_counter)
        print(f"SCORE\nPlayer: {player_score_counter}, Computer: {computer_score_counter}")
        
        
    if player_score_counter > computer_score_counter:
        print("Congratulations! You won the series!")
    else:
        print("Sorry! The computer won the series.")
    
    if not replay():
        print("Bye")
        break
    
    clear_output()