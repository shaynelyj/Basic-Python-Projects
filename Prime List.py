'''
Generate a list of user specified input of prime numbers
'''


def prime_input():
    while True:
        try:
            q = int(input("Number of prime numbers to print: "))
        except:
            print ("Please input an integer")
        else:
            return q

def prime_check(q):
    for a in range(2,q):
        if q%a == 0:
            return False
    return True
        
def prime_list(w):
    e = []
    r = 2
    while len(e) < w:
        if prime_check(r):
            e.append(r)
        r+=1
    print (e)

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    q = prime_input()
    prime_list(q)
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
