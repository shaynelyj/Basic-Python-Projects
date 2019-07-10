'''
Display all prime factors of a given number
'''


def prime_input():
    while True:
        try:
            q = int(input("Number to check for prime factors: "))
        except:
            print ("Please input an integer!")
        else:
            if q < 2:
                print ("Please input an integer greater than one!")
            else:
                return q

def prime_check(q):
    global w
    w = []
    for a in range(2,q):
        if q%a == 0:
            w.append(a)
    return len(w) == 0
    
def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == "y"

while True:
    
    q = prime_input()
    e = []
    
    while q > 1:
        if prime_check(int(q)):
            e.append(int(q))
            q /= q
        else:
            e.append(w[0])
            q /= w[0]
    
    str1 = "*".join(str(t) for t in e)
    print (str1)
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
