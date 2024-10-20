# Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

import random

class NegativeNumber(Exception):
    """ Custom exception for negative number input """
    def __init__(self, message="Please insert only positive numbers"):
        super().__init__(message)

def validate_number(number):
    """ Validates if the input number is negative and raises an exception if true """
    if number < 0:
        raise NegativeNumber()

def flip_coin(n):
    """ Simulates flipping a coin n times and returns the counts of heads and tails """
    coin = {0:"HEAD", 1:"TAIL"}
    head_count = 0
    tail_count = 0
    results = []

    for _ in range(n):
        coin_flip = random.randint(0,1)
        results.append(coin[coin_flip])
    
        if coin_flip == 0:
            head_count += 1
        else:
            tail_count += 1
    print("Flip results:")
    for result in results:
        print(result)

    return head_count, tail_count

def main():
    """ Main function to drive the program """
    while True:
        try:
            # Prompt the user for input
            n = int(input("How many times would you like to flip the coin? "))
            # Validate the input number
            validate_number(n)

            head_count, tail_count = flip_coin(n)
            print(f"Numbers of HEADs: {head_count}")
            print(f"Numbers of TAILs: {tail_count}")

            # Exit the loop if no exceptions were raised
            break

        except NegativeNumber as e:
            print(e)
        except ValueError:
            print("Please insert only numbers")
        except KeyboardInterrupt:
            print("Operation cancelled")
            break

if __name__ == "__main__":
    main()







