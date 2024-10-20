# Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
import re

def clean_input(word):
    """Removes non-alphabetic characters and converts to lowercase"""
    return re.sub(r"[^A-Za-z]", "", word).lower()

def main():
    vowels = 'aeiou'
    vowels_count = {v:0 for v in vowels}

    word = input("Enter a word: ").strip()
    cleaned_word = clean_input(word)    
    
    while not cleaned_word:
        word = input("\nNo valid input entered, please try again: ").strip()
        cleaned_word = clean_input(word)

    for c in cleaned_word:
        if c in vowels_count:
            vowels_count[c] += 1

    total_vowels = sum(vowels_count.values())
    
    print(f"\nThere are {total_vowels} vowels in {word}")
    for vowel, count in vowels_count.items():
        print(f"There are {count} {vowel.upper()}s")

if __name__ == "__main__":
    main()