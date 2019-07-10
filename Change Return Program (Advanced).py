'''
User can input supply for notes and coins
Display remaining supply after each transaction
Breaks and dislay outstanding balance for insufficient change
'''

class Change:
    
    def __init__(self, TenD, FiveD, TwoD, OneD, FiftyC, TwentyC, TenC):
        self.TenD = TenD
        self.FiveD = FiveD
        self.TwoD = TwoD
        self.OneD = OneD
        self.FiftyC = FiftyC
        self.TwentyC = TwentyC
        self.TenC = TenC
        
    def notes(self,ch):
        TenD, FiveD, TwoD, OneD, FiftyC, TwentyC, TenC = 0,0,0,0,0,0,0
        
        if ch >= 10 and self.TenD:
            while ch >= 10 and self.TenD:    
                ch -= 10
                self.TenD -= 1
                TenD += 1
            print (f"Ten Dollars: {TenD}")
        
        if ch >= 5 and self.FiveD:
            while ch >= 5 and self.FiveD:    
                ch -= 5
                self.FiveD -= 1
                FiveD += 1
            print (f"Five Dollars: {FiveD}")
    
        if ch >= 2 and self.TwoD:
            while ch >= 2 and self.TwoD: 
                ch -= 2
                self.TwoD -= 1
                TwoD += 1
            print (f"Two Dollars: {TwoD}")
        
        if ch >= 1 and self.OneD: 
            while ch >= 1 and self.OneD: 
                ch -= 1
                self.OneD -= 1
                OneD += 1
            print (f"One Dollar: {OneD}")
            
        if ch >= round(Decimal(0.50),2) and self.FiftyC: 
            while ch >= round(Decimal(0.50),2) and self.FiftyC: 
                ch -= round(Decimal(0.50),2)
                self.FiftyC -= 1
                FiftyC += 1
            print (f"Fifty Cents: {FiftyC}")
        
        if ch >= round(Decimal(0.20),2) and self.TwentyC: 
            while ch >= round(Decimal(0.20),2) and self.TwentyC: 
                ch -= round(Decimal(0.20),2)
                self.TwentyC -= 1
                TwentyC += 1
            print (f"Twenty Cents: {TwentyC}")
        
        if ch >= round(Decimal(0.10),2) and self.TenC: 
            while ch >= round(Decimal(0.10),2) and self.TenC: 
                ch -= round(Decimal(0.10),2)
                self.TenC -= 1
                TenC += 1
            print (f"Ten Cents: {TenC}")
        
        if ch:
            print (f"Insufficient change! Require {ch} more!")
            return False
            
    def stock(self):
        
        print ("\nCurrent stock:")
        print (f"Ten Dollars: {self.TenD}")
        print (f"Five Dollars: {self.FiveD}")
        print (f"Two Dollars: {self.TwoD}")
        print (f"One Dollar: {self.OneD}")
        print (f"Fifty Cents: {self.FiftyC}")
        print (f"Twenty Cents: {self.TwentyC}")
        print (f"Ten Cents: {self.TenC}\n")

def Cost():
    while True:
        try:
            co = round(Decimal(input("\nCost: ")),2)
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
        
def replay():
    r = " "
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N: ").lower()
    return r

from decimal import Decimal
q = Change(9,9,9,9,9,9,9)

while True:
    
    co = Cost()
    ca = Cash()
    ch = ca - co
    print (f"Change: {ch}")
    w = q.notes(ch)
    
    if w == 0:
        q.stock()
        break
    
    q.stock()

    r = replay()

    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
