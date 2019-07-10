'''
Continue to generate the next happy number until user stops
'''

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Show next happy number? Y or N?: ").lower()
    return r

def happy_check(q):
    while q not in [1,4]:
        w = 0
        for a in str(q):
            w+=int(a)**2
        q = w
    return q == 1

def happy_next():
    w = 1
    while True:
        if happy_check(w):
                yield(w)
        w+=1

w = happy_next()

while True:
    
    if replay() == "y":
        print (next(w))
        continue
    else:
        print ("Thanks for using!")
        break
