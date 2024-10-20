# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

class LessThanOne(Exception):
    """ Custom exception for number input less than or equal to 1 """
    def __init__(self, message="Please insert only numbers greater than 1"):
        super().__init__(message)

def validate_number(number):
    """ Checks if the input number is greater than 1 and raises an exception if not """
    if number <= 1:
        raise LessThanOne()

def main():
    while True:
        try:
            num = int(input("Enter a number greater than 1: "))
            validate_number(num)
            break
        except LessThanOne as e:
            print(e)
        except ValueError:
            print("Invalid input. Please enter an integer")

    steps_count = 0
    op_num = num

    while op_num != 1:
            if op_num%2==0:
                op_num //= 2
            else:
                op_num = op_num * 3 + 1
            steps_count += 1

    print(f"According to the Collatz Conjecture, it took {steps_count} steps to reach 1 starting from {num}.")

if __name__ == "__main__":
    main()