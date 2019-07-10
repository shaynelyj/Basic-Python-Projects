#A simple alarm where it plays a sound after X number of minutes/seconds.

def user_input():
    while True:
        try:
            q = int(input("Hour:"))
            w = int(input("Minute:"))
            e = int(input("Second:"))
        except:
            print ("Please input an integer!")
        else:
            return q*3600 + w*60 + e

def alarm(q):
    while q:
        mins,secs = divmod(q,60)
        print (f"{mins:02d}:{secs:02d}",end = '\r')
        q-=1
        time.sleep(1)
    print ("Alarm!")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

def replay():
    r = ""
    while r not in ["y","n"]:
        r = input("\nUse again? Y or N: ").lower()
        print ("")
    return r == "y"

import time, winsound

while True:
    
    q = user_input()
    
    if q:
        alarm(q)
    
    r = replay()
    
    if r:
        continue
    else:
        print ("Thanks for using!")
        break
