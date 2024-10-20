# Have the user enter a number and find all Prime Factors (if there are any) and display them.

class LessThanOne(Exception):
    """ Custom exception for number input less than or equal to 1 """
    def __init__(self, message="Please insert only numbers greater than 1"):
        super().__init__(message)

def validate_number(number):
    """ Checks if the input number is greater than 1 and raises an exception if not """
    if number <= 1:
        raise LessThanOne()

def prime_factors(num):
    prime_factors = []
    factor = 2
    while num > 1:
        while num%factor == 0:
            num //= factor
            prime_factors.append(factor)
        factor += 1
    return prime_factors

def main():
    while True:
        try:
            n = int(input("Enter a positive integer greater than 1: "))
            validate_number(n)
            break
        except LessThanOne as e:
            print(e)
        except ValueError:
            print("Please insert only numbers")
    
    factors = prime_factors(n)
    if factors:
        print(f"The prime factor(s) of {n} are {", ".join(map(str, factors))}")
    else:
        print(f"{n} has no prime factors")

if __name__ == "__main__":
    main()