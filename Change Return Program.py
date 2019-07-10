#The user enters a cost and then the amount of money given. The program will figure out the change and the number of notes (10, 5, 2) and coins (1, 0.5, 0.2, 0.1) needed for the change.

def Cost():
    while True:
        try:
            co = round(Decimal(input("Cost: ")),2)
        except:
            print ("Please input an integer!")
        else:
            return co

def Cash():
    while True:
        try:
            ca = round(Decimal(input("Cash: ")),2)
        except:
            print ("Please input an integer!")
        else:
            return ca
        
def Change(q):
    
    if q >= 10:
        print (f"Ten Dollars: {int(q/10)}")
        q -= int(q/10) * 10
    
    if q >= 5:
        print (f"Five Dollars: {int(q/5)}")
        q -= int(q/5) * 5
        
    if q >= 2:
        print (f"Two Dollars: {int(q/2)}")
        q -= int(q/2) * 2
        
    if q >= 1:
        print (f"One Dollar: {int(q/1)}")
        q -= int(q/1) * 1
    
    if q >= round(Decimal(0.50),2):
        print (f"Fifty Cents: {int(q/round(Decimal(0.50),2))}")
        q -= int(q/round(Decimal(0.50),2)) * round(Decimal(0.50),2)
    
    if q >= round(Decimal(0.20),2):
        print (f"Twenty Cents: {int(q/round(Decimal(0.20),2))}")
        q -= int(q/round(Decimal(0.20),2)) * round(Decimal(0.20),2)
        
    if q >= round(Decimal(0.10),2):
        print (f"Ten Cents: {int(q/round(Decimal(0.10),2))}")
        q -= int(q/round(Decimal(0.10),2)) * round(Decimal(0.10),2)
        
def replay():
    r = " "
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N: ").lower()
    return r

from decimal import Decimal
while True:
    
    co = Cost()
    ca = Cash()
    ch = ca - co
    print (f"Change: {ch}")
    Change(ch)
    
    r = replay()

    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
