'''Questions 1

Find the value of the following questions, Where x=5

● (2x+5/x^2+5x+6)
● (x^2+5x+6/2x+5)
● (2x-3)(x-9)'''

x=5

print("Answer for (2x+5/x^2+5x+6):",2*x+5/x**2+5*x+6)
print("Answer for (x^2+5x+6/2x+5)",(x**2+5*x+6/2*x+5))
print("Answer for (2x-3)(x-9)",(2*x-3)*(x-9))

'''Questions 2
Create a username and password login file using nested while loop'''

import os.path
from os import path

def useradd():
    print("Old Data")
    f1=open("details.txt","r")
    content=f1.read()
    print(content)
    f1.close()
    count=int(input("Enter count of user you want to create:"))
    while count > 0:
        username = input("Enter username:")
        if username in open("details.txt").read():
            print(username+" Username already exist,try differnt name")
            continue
          
        else:
            password = input("Enter password:")
            detail = username +":"+password
            print(detail)

            f1=open("details.txt","a")
            f1.write(str(detail)+"\n")
            f1.close()

            print("New Data")
            f1=open("details.txt","r")
            content=f1.read()
            print(content)
            f1.close()
            count-=1

test=os.path.exists("details.txt")

if test == False:
    print("File is not exist so creating new file")
    f = open("details.txt", "w")
    f.close()
    useradd()
else:
    useradd()
    
    
