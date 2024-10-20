# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
def main():
    for n in range(1,101):
        output = ''
        if n%3==0:
            output += 'Fizz'
        if n%5==0:
            output += 'Buzz'
        if output == '':
            output = n
        print(output)

if __name__ == "__main__":
    main()