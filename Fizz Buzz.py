"""
This program will print the numbers from 1 to 100.
For multiples of three, the program will print "Fizz" instead of the number and "Buzz" if the number is multiples of five.
For multiples of both three and five, the program will print "FizzBuzz"
"""

if __name__ == '__main__':
    for a in range(1,101):
        if a % 3 == 0 and a % 5 == 0:
            print ("FizzBuzz")
        elif a % 3 == 0:
            print ("Fizz")
        elif a % 5 == 0:
            print ("Buzz")
        else:
            print (a)
