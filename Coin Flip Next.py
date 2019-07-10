'''
Continue to flip the coin until user stops
'''


def replay():
    r = ""
    while r not in ['y','n']:
        r = input("\nFlip coin? Y or N?: ").lower()
    return r == 'y'

def coin_flip():
    import random
    global h
    global t
    h = 0
    t = 0
    while True:
        q = random.randint(0,1)
    
        if q:
            h += 1
            yield "Head"
        else:
            t += 1
            yield "Tail"

z = coin_flip()
while True:
    
    q = replay()
    
    if q:
        print(next(z))
        continue
    else:
        print (f"\nHead: {h}")
        print (f"Tail: {t}")
        print ("Thanks for using!")
        break
