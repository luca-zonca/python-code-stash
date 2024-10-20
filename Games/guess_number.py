import random

def main():
    # Greeting the player
    player_name = input("Hello! What is your name?\n")

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    # Randomly generate the number to guess
    num_to_guess = random.randint(1,20)

    n_guesses = 0
    guess = None

    # Main game loop
    while guess != num_to_guess:
        try:
            guess = int(input("Take a guess: "))

            # Check if guess is within the valid range
            if guess < 1 or guess > 20:
                print("Remember, the number I am thinking of is between 1 and 20")
                # This guess will not be counted in the total number of guesses
                continue
            
            n_guesses += 1


            if guess > num_to_guess:
                print("Your guess is too high")
            elif guess < num_to_guess:
                print("Your guess is too low")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20")
            
    # If the loop exits, the guess was correct
    print(f"Good job {player_name}! You guessed my number in {n_guesses} guesses")

if __name__ == "__main__":
    main()