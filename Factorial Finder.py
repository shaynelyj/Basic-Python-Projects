#Find the factorial of a number. Eg. 5! = 54321 = 120

def factorial_input():
    while True:
        try:
            q = int(input("Factorial of: "))
        except:
            print ("Please input an integer!")
        else:
            return q

def factorial_finder(q):
    w = 1
    for e in range(1,q+1):
        w*=e
    print (w)
    
def replay():
    r = ""
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N?: ").lower()
    return r

while True:
    
    q = factorial_input()
    factorial_finder(q)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
