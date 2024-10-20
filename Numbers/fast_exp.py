# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.

def main():
    print("Enter 2 integers a and b, to output a^b")
    
    def get_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please insert only numbers")
    
    a = get_integer("a = ")
    b = get_integer("b = ")
    
    print(pow(a,b))

if __name__ == "__main__":
    main()