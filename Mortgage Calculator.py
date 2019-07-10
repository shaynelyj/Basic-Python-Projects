#Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.

def loan_amount():
    while True:
        try:
            P = int(input("Loan amount: "))
        except:
            print ("Please input an integer!")
        else:
            return P
        
def interest_rate():
    while True:
        try:
            R = float(input("Interest Rate (%): "))
        except:
            print ("Please input an integer!")
        else:
            R = R/12/100
            return R
        
def repayment_period():
    while True:
        try:
            M = int(input("Repayment Period (Years): "))
        except:
            print ("Please input an integer!")
        else:
            M = M*12
            return M
        
def mortgage_formula(p,r,m):
    i = (p*(r*(1+r)**m)) / ((1+r)**m-1)
    return i

def replay():
    r = " "
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N: ").lower()
    return r

while True:
    p = loan_amount()
    r = interest_rate()
    m = repayment_period()
    c = mortgage_formula(p,r,m)
    print (f"Monthly mortgage: ${c:1.2f}")
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
