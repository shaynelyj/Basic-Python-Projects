#Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

import math

while True:
    try:
        q = int(input("No. of decimal points for pi: "))
    except:
        print ("Please input an integer")
    else:
        print (f"{math.pi:1.{q}f}")
        
        r = ""
        while not (r == 'y' or r == 'n'):
            r = input("Calculate again? Y or N: ").lower()
        
        if r == 'y':
            continue
        else:
            print ("Thanks for using!")
            break
