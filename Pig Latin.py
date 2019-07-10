'''
For words beginning with a vowel (a,e,i,o,u), add "ay" to the end. E.g: eat = eatay
Else, all letters before the initial vowel are placed at the end of the word sequence before adding "ay". E.g: Smile = ilesmay
'''

def str_input():
    w = input("String: ")
    return w

def pig_latin(q):
    if q[0] in ["a","e","i","o","u"]:
        return (q+"ay")
    else:
        for z in q:
            if z in ["a","e","i","o","u"]:
                return (q[q.index(z):] + q[:q.index(z)] + 'ay')
            
def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    
    q = str_input()
    print(pig_latin(q))
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
