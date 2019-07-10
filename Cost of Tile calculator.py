#Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

def length():
    while True:
        try:
            l = int(input("Length (ft): "))
        except:
            print ("Please input an integer!")
        else:
            return l

def width():
    while True:
        try:
            w = int(input("Width (ft): "))
        except:
            print ("Please input an integer!")
        else:
            return w
        
def cost():
    while True:
        try:
            c = int(input("Cost psf: "))
        except:
            print ("Please input an integer!")
        else:
            return c
        
def replay():
    r = " "
    while not (r == "y" or r == "n"):
        r = input("Calculate again? Y or N: ").lower()
    return r

while True:
    l = length()
    w = width()
    c = cost()
    print (f"Total: ${l*w*c}")
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
