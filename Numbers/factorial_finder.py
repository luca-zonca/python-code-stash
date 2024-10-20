#The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

class NegativeNumber(Exception):
    """ Custom exception for negative number input """
    def __init__(self, message="Please insert only positive numbers"):
        super().__init__(message)

def validate_number(number):
    """ Validates if the input number is negative and raises an exception if true """
    if number < 0:
        raise NegativeNumber()

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num-1)

def factorial_loop(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

def main():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            validate_number(n)
            break
        except NegativeNumber as e:
            print(e)
        except ValueError:
            print("Please insert only numbers")
    
    print(f"The factorial (recursive) of {n} is {factorial_recursive(n)}")
    print(f"The factorial (loop) of {n} is {factorial_loop(n)}")

if __name__ == "__main__":
    main()