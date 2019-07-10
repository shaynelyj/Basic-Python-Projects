#Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number

def cc_input():
    while True:
        try:
            cc = int(input("Credit Card number: "))
        except:
            print("Please input an integer!")
        else:
            return cc

def cc_check(q):
    w = [int(x) for x in str(q)]
    for e in range (-2, -len(w)-1,-2):
        w[e]*=2
        
        if w[e] > 9:
            r = 0
            for a in str(w[e]):
                r += int(a)
            w[e] = r
    t = 0
    for z in w:
        t+=z
    print (t%10 == 0)

def replay():
    r = ""
    while not (r == "y" or r == "n"):
        r = input("Check again? Y or N?: ").lower()
    return r

while True:
    
    q = cc_input()
    cc_check(q)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
