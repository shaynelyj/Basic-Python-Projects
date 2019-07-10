'''
User decide how many times the coin is flipped and print the outcome, number of heads and tails.
'''

def flip_input():
    while True:
        try:
            q = int(input("No. of coin flips: "))
        except:
            print ("Please input an integer!")
        else:
            if q < 1:
                print ("Input must be greater than 0")
                continue
            else:
                return q

def coin_flip(q):
    import random
    head = 0
    tail = 0
    result = []
    while q:
        w = random.randint(0,1)
        
        if w:
            head += 1
            result.append("Head")
        else:
            tail += 1
            result.append("Tail")
        q-=1
    
    print (result)
    print (f"Head: {head}")
    print (f"Tail: {tail}")
    
def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Flip again? Y or N?: ").lower()
    return r

while True:
    
    q = flip_input()
    coin_flip(q)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
