'''
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or number 10801.
'''


def str_input():
    w = input("Palindrome check: ")
    return w.lower()

def palindrome_check(q):
    return q == q[::-1]

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    
    q = str_input()
    w = palindrome_check(q)
    
    if w:
        print (f"{q} is a palindrome")
    else:
        print (f"{q} is not a palindrome")
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
