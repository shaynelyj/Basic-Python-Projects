'''
Find Prime Numbers to the Nth Digit
'''



def prime_input():
    while True:
        try:
            q = int(input("Find prime numbers up to: "))
        except:
            print ("Please input an integer")
        else:
            return q

def prime_check(q):
    for a in range(2,q):
        if q%a == 0:
            return False
    return True

def prime_range(w):
    s = [2]
    if w == 2:
        print (s)
    else:
        a = 3
        while a <= w:
            if prime_check(a):
                s.append(a)
            a+=2
        print (f"{len(s)} prime numbers: {s}")

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    q = prime_input()
    
    if q < 2:
        print ([])
    else:
        prime_range(q)
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
