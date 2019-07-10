#A simple calculator to do basic operators + - * /

def num_1():
    while True:
        try:
            num1 = int(input("First Number: "))
        except:
            print("Please input an integer!")
        else:
            return num1

def num_2():
    while True:
        try:
            num2 = int(input("Second Number: "))
        except:
            print("Please input an integer!")
        else:
            return num2
        
def opt_input():
    q = ""
    while not (q == '+' or q == '-' or q == '*' or q == '/'):
        q = input("Enter an operator - '+, -, *, /': " )
    return q

def replay():
    r = ""
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N?: ").lower()
    return r

while True:
    
    q = num_1()
    w = num_2()
    e = opt_input()
    
    if e == "+":
        print (q+w)
    elif e == "-":
        print (q-w)
    elif e == "*":
        print (q*w)
    elif e == "/":
        print (q/w)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
