'''
Collatz-Conjecture: Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

Number = 3

3 x 3 + 1 = 10
10 / 2 = 5
5 x 3 + 1 = 16
16 / 2 = 8
8 / 2 = 4
4 / 2 = 2
2 / 2 = 1
Python project

Collatz Conjecture Check.py: Input a specific integer and check the number of steps required to reach 1
'''

def int_input():
    while True:
        try:
            q = int(input("Number for Collatz Conjecture: "))
        except:
            print ("Please input an integer!")
        else:
            if q < 1:
                print ("Input must be greater than 0")
                continue
            else:
                return q

def collatz_check(q):
    e = q
    w = 0
    while q > 1:

        if q%2 == 0:
            q/=2
        else:
            q = q*3+1
        w+=1
    print (f"No. of Steps for {e} to reach 1: {w}")

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N?: ").lower()
    return r

while True:
    
    q = int_input()
    collatz_check(q)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
