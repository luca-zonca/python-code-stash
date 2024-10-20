# Enter a string and the program will reverse it and print it out.
# Checks if the string entered by the user is a palindrome (it reads the same forwards as backwards)

import re

def clean_input(word):
    """Removes non-alphanumeric characters and converts to lowercase"""
    return re.sub(r"[^A-Za-z0-9]", "", word).lower()

def main():
    word = input("Enter a word: ").strip()
    cleaned_word = clean_input(word)    
    
    # An empty string ("") is considered False. strip() removes the whitespace (not in place), so pressing enter without typing and entering only whitespace are caught
    while not cleaned_word:
        word = input("\nNo valid input entered, please try again: ").strip()
        cleaned_word = clean_input(word)

    print(f"\nThe reverse of {word} is {word[::-1]}")
    if cleaned_word == cleaned_word[::-1]:
        print(f"{word} is a palindrome!")

if __name__ == "__main__":
    main()
