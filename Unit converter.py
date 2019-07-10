def con_input():
    print("1. Celsius to Fahrenheit converter (°C to °F)")
    print("2. Fahrenheit to Celsius converter (°F to °C)")
    print("3. Decimal to Binary converter (50 to 110010)")
    print("4. Binary to Decimal converter (110010 to 50)")
    q = 0
    while q not in [1,2,3,4]:
        q = int(input("\nPlease enter a converter: "))
    return q

def unit_input():
    while True:
        try:
            q = int(input("\nUnit: "))
        except:
            print ("Please input an integer!")
        else:
            return q
        
def cel_fah(q):
    print (f"{q*9/5+32}°F")
    
def fah_cel(q):
    print (f"{5/9*(q-32)}°C")
    
def dec_bin(dec):
    binpos = []
    while dec:
        a = 0
        while 2**a < dec:
            a += 1
        
        if 2**a == dec:
            binpos.append(a)
            dec -= 2**a
        else:
            binpos.append(a-1)
            dec -= 2**(a-1)
            
    binlist = [0]*(binpos[0]+1)  
    for x in binpos:
        binlist[binpos[0]- x] = 1
    
    binstr = "".join(str(c) for c in binlist)
    print (f"Binary: {binstr}")
    
def bin_dec(bin):
    w = [int(x) for x in str(bin)]
    q = 0
    while len(w):
        if w[0] == 1:
            q += 2**(len(w)-1)
        w.pop(0)
    print (f"Decimal: {q}")

def replay():
    r = ""
    while r not in ["y","n"]:
        r = input("\nCalculate again? Y or N: ").lower()
        print ("")
    return r == "y"
    
while True:
    q = con_input()
    w = unit_input()
    
    if q == 1:
        cel_fah(w)
    elif q == 2:
        fah_cel(w)
    elif q == 3:
        dec_bin(w)
    elif q == 4:
        bin_dec(w)
        
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
