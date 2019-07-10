'''
Convert number to words (99 = ninety nine, -99 = negative ninety nine)
Only support six digits from -999999 to 999999
'''

one = {'0':'','1': "one", '2': "two", '3': "three", '4': "four", '5':"five", '6':"six", '7':"seven", '8':"eight", '9':"nine"}
teen = {'0':'ten','1': "eleven", '2': "twelve", '3': "thirteen", '4':'fourteen','5':"fifteen",'6':"sixteen", '7':"seventeen", '8':"eighteen", '9':"nineteen"}
ty = {'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':"sixty", '7':"seventy", '8':"eighty", '9':"ninety"}

def len_one(q):
    return (one[q])

def len_two(q,w):
    if q == '0':
        return len_one(w)
    if q == '1':
        return teen[w]
    else:
        return ty[q] + " " + one[w]

def len_three(q,w,e):
    if q == '0':
        return len_two(w,e)
    else:
        return one[q] + " hundred " + len_two(w,e)

def len_four(q,w,e,r):
    if q == '0':
        return len_three(w,e,r)
    else:
        return one[q] + " thousand " + len_three(w,e,r)

def len_five(q,w,e,r,t):
    if q == '0':
        return len_four(w,e,r,t)
    else:
        return len_two(q,w) + " thousand " + len_three(e,r,t)

def len_six(q,w,e,r,t,y):
    if q == '0':
        return len_five(w,e,r,t,y)
    else:
        return len_three(q,w,e) + " thousand " + len_three(r,t,y)

def int_input():
    while True:
        try:
            q = int(input("Num to convert to words: "))
        except:
            print ("Please input an integer!")
        else:
            return q

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N?: ").lower()
    return r

while True:
    
    z = int_input()
    x = [c for c in str(z)]
    v = ""
    
    if x[0] == '-':
        x.pop(0)
        v+='negative '
        
    if z == 0:
        print ("Zero")
    elif len(x) == 6:
        v += (len_six(x[0], x[1], x[2], x[3], x[4], x[5]))
    elif len (x) == 5:
        v += (len_five(x[0], x[1], x[2], x[3], x[4]))
    elif len (x) == 4:
        v += (len_four(x[0], x[1], x[2], x[3]))
    elif len (x) == 3:
        v += (len_three(x[0], x[1], x[2]))
    elif len (x) == 2:
        v += (len_two(x[0], x[1]))
    elif len (x) == 1:
        v += (len_one(x[0]))
        
    print (v)
    
    r = replay()
    
    if r == "y":
        continue
    else:
        print ("Thanks for using!")
        break
