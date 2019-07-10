'''
User enters a string and returns the number of vowels (a,e,i,o,u)
'''


def str_input():
    w = input("String: ")
    return w

def vowel_count(q):
    a,e,i,o,u = 0,0,0,0,0
    for z in q.lower():
        if z == "a":
            a+=1
        elif z == "e":
            e+=1
        elif z == "i":
            i+=1
        elif z == "o":
            o+=1
        elif z == "u":
            u+=1
    
    return(f"Vowel count: {a+e+i+o+u} \na:{a} \ne:{e} \ni:{i} \no:{o} \nu:{u}")
    
def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    
    q = str_input()
    print(vowel_count(q))
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
