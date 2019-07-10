#Dice Simulator Graphic.py: Show graphic representation of Dice output

pattern = {1:"   ", 2:"O  ", 3:" O ",4:"  O",5:"O O"}
combination = {1:"131", 2:"214", 3:"234", 4:"515", 5:"535", 6:"555"}

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("\nRoll dice? Y or N?: ").lower()
    return r == 'y'

def roll_dice():
    import random
    q = random.randint(1,6)
    for a in combination[q]:
        print (pattern[int(a)])
        
while True:
    
    r = replay()
    
    if r:
        print ("")
        roll_dice()
        continue
    else:
        print ("Thanks for using!")
        break
