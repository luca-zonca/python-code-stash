# Enter a number and have the program generate the Fibonacci or to the Nth number

class NegativeNumber(Exception):
    """ Custom exception for negative number input """
    def __init__(self, message="Please insert only positive numbers"):
        super().__init__(message)

def validate_number(number):
    """ Validates if the input number is negative and raises an exception if true """
    if number < 0:
        raise NegativeNumber()
    
def generate_fibonacci(n):
    """ Generates the Fibonacci sequence up to the nth number """
    
    # Handles edge cases
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci = [0,1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def main():
    """ Main function to drive the program """
    while True:
        try:
            # Prompt the user for input
            n = int(input("Enter a positive integer for the length of the Fibonacci sequence: "))
            # Validate the input number
            validate_number(n)

            print(generate_fibonacci(n))
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





# Enter a number and have the program generate the Fibonacci sequence to that number