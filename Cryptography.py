'''
Project 1
Do the project - Develop a cryptography app in python.
'''

import tkinter as tk
from tkinter import * 
import onetimepad

root = Tk() 


def encode(): 
    a = var.get()
    ct = onetimepad.encrypt(a,"letupgrade") 
    print("Working",ct)  
    e2.delete(0,END) 
    e2.insert(END,ct) 

def decode(): 
    a = var2.get() 
    ct = onetimepad.decrypt(a,"letupgrade") 
    print("Working",ct)  
    e4.delete(0,END) 
    e4.insert(END,ct) 


root.title("Cryptography App") 
root.minsize(600,400)

l1=Label(root,text="Enter Plain Text")
l1.grid(row=0,column=0)

l2=Label(root,text="Encrypted Text")
l2.grid(row=1,column=0)

var=StringVar()
e1=Entry(root,textvariable=var)
e1.grid(row=0,column=1)

var1=StringVar()
e2=Entry(root,textvariable=var1)
e2.grid(row=1,column=1)

l3=Label(root,text="Enter Plain Text")
l3.grid(row=0,column=4)

l4=Label(root,text="Decrypted Text")
l4.grid(row=1,column=4)


var2=StringVar()
e3=Entry(root,textvariable=var2)
e3.grid(row=0,column=5)

var3=StringVar()
e4=Entry(root,textvariable=var3)
e4.grid(row=1,column=5)


button = Button(root, text = "Encryption", command = encode)
button.grid(column= 0, row = 2)

button = Button(root, text = "Decryption", command = decode)
button.grid(column= 5, row = 2)


root.mainloop() 
