'''
Continue to generate next prime number until user stops
'''

def next_input():
    r = ""
    while r not in ['y','n']:
        r = input("Show next prime number? Y or N: ").lower()
    return r == 'y'

def prime_check(q):
    for a in range(2,q):
        if q%a == 0:
            return False
    return True
        
def prime_next():
    a = 2
    while True:
        if prime_check(a):
            yield a
        a+=1

w = prime_next()

while True:
    q = next_input()
    
    if q:
        print(next(w))
        continue
    else:
        print ("Thanks for using!")
        break
