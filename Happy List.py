'''
Print out list of happy numbers
E.g:
No. of happy numbers to print: 8
[1, 7, 10, 13, 19, 23, 28, 31]
'''

def happy_input():
    while True:
        try:
            q = int(input("No. of happy numbers: "))
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

def happy_list(q):
    w = 1
    s = []
    while len(s) < q:
        if happy_check(w):
            s.append(w)
        w+=1
    print (s)

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N?: ").lower()
    return r

while True:
    
    q = happy_input()
    
    happy_list(q)
        
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
