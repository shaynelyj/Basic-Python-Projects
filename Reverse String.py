'''
Enter a string and the program will reverse it and print it out.
"Hello World" = "dlroW olleH"
'''

def str_input():
    w = input("String: ")
    return w

def rev_string(q):
    print (q[::-1])

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    
    q = str_input()
    rev_string(q)
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
