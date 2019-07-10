'''
Count the number of words in a string or txt file
'''

def user_input():
    print ("Welcome to Word counter!")
    print ("1. Count words from string")
    print ("2. Count words from file")
    while True:
        try:
            q = int(input("\nPlease enter an option: "))
        except:
            print ("Please input either 1 or 2.")
        else:
            if q not in [1,2]:
                print ("Please input either 1 or 2.")
                continue
            else:
                return q

def count_string():   
    q = input("Enter string: ")
    return f"{len(q.split())} words in string"

def count_file():
    while True:
        try:
            w = input("File name: ")
            q = open(f'{w}.txt','r')
        except:
            print ("Invalid file name. Please try again.")
        else:          
            z = 0
            for a in q:
                z+=len(a.split())
            q.close()
            return f"{z} words in {w}.txt"

def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Check again? Y or N: ").lower()
    return r == 'y'

while True:
    
    q = user_input()
    
    if q == 1:
        print (count_string())
    else:
        print (count_file())
        
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
