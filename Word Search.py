'''
Search for text in txt file
'''


def file_input():
    w = input("File: ")
    return w

def text_input():
    w = input("Text: ")
    return w

def search_text(file,text):
    q = open(f"{file}.txt","r")
    for z,x in enumerate(q):
        if text in x:
            print (f"Line {z}: {x}")
    q.close()
    
def replay():
    r = ""
    while r not in ['y','n']:
        r = input("Search again? Y or N: ").lower()
    return r == 'y'

while True:
    
    q = file_input()
    w = text_input()
    search_text(q,w)
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
