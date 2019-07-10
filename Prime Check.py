'''
Check if a number is prime
'''

def prime_input():
    while True:
        try:
            q = int(input("Check if number is prime: "))
        except:
            print ("Please input an integer")
        else:
            if q < 2:
                print ("Number must be larger than 1")
                continue
            else:
                return q

def prime_check(q):
    for a in range(2,q):
        if q%a == 0:
            return False
    return True

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    q = prime_input()
    if prime_check(q):
        print (f"{q} is prime")
    else:
        print (f"{q} is not prime")
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
