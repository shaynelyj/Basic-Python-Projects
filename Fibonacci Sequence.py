#Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def Fibo(w):
    a,b = 1,1
    for q in range(w):
        yield a
        a,b = b,b+a
        
def fibo_input():
    while True:
        try:
            q = int(input("Number of Fibonacci Sequence: "))
        except:
            print ("Please input an integer")
        else:
            return q
        
def replay():
    r = " "
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N: ").lower()
    return r

while True:
    
    print("Welcome to Fibonacci Sequence nth")
    
    q = fibo_input()
    for e in Fibo(q):
        print (e)
        
    r = replay()
        
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
