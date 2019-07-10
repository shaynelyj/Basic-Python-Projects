#Calculate Income Tax payable based on Singapore Income Tax rates

def income_input():
    while True:
        try:
            q = int(input("Annual Income: "))
        except:
            print ("Please input an integer!")
        else:
            return q

def income_tax(q):
    
    if q <= 20000:
        print ("Income Tax: $0")
    
    if 20001 <= q <= 30000:
        print (f"Income Tax: ${(q-20000)*0.02:1.2f}")
    
    if 30001 <= q <= 40000:
        print (f"Income Tax: ${(q-30000)*0.035+200:1.2f}")
        
    if 40001 <= q <= 80000:
        print (f"Income Tax: ${(q-40000)*0.07+550:1.2f}")
        
    if 80001 <= q <= 120000:
        print (f"Income Tax: ${(q-80000)*0.115+3350:1.2f}")
    
    if 120001 <= q <= 160000:
        print (f"Income Tax: ${(q-120000)*0.15+7950:1.2f}")
    
    if 160001 <= q <= 200000:
        print (f"Income Tax: ${(q-160000)*0.18+13950:1.2f}")
        
    if 200001 <= q <= 240000:
        print (f"Income Tax: ${(q-200000)*0.19+21150:1.2f}")
    
    if 240001 <= q <= 280000:
        print (f"Income Tax: ${(q-240000)*0.195+28750:1.2f}")
    
    if 280001 <= q <= 320000:
        print (f"Income Tax: ${(q-280000)*0.2+36550:1.2f}")
        
    if 320001 <= q:
        print (f"Income Tax: ${(q-320000)*0.22+44550:1.2f}")
        
def replay():
    r = ""
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N?: ").lower()
    return r

while True:
    
    q = income_input()
    income_tax(q)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
