'''
Check if a number is a happy number
'''


def happy_input():
    while True:
        try:
            q = int(input("Check for happy number: "))
        except:
            print ("Please input an integer!")
        else:
            if q < 1:
                print ("Input must be greater than 0")
                continue
            else:
                return q

def happy_check(q):
    while q not in [1,4]:
        w = 0
        for a in str(q):
            w+=int(a)**2
        q = w
    return q == 1

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N?: ").lower()
    return r

while True:
    
    q = happy_input()
    
    if happy_check(q):
        print (f"{q} is a happy number")
    else:
        print (f"{q} is not a happy number")
        
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
