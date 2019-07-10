#Dice Simulator.py: Continue to roll dice until user stops
def replay():
    r = ""
    while r not in ['y','n']:
        r = input("\nRoll dice? Y or N?: ").lower()
    return r == 'y'

def roll_dice():
    import random
    while True:
        q = random.randint(1,6)
        yield q
        
z = roll_dice()
while True:
    
    r = replay()
    
    if r:
        print(next(z))
        continue
    else:
        print ("Thanks for using!")
        break
