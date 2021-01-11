#Assignment 3:

'''
Question 1
Write a Python function to find the Max of three numbers.
'''

def max(num):
    num.sort(reverse = True)
    return(num[0])

num=[3,7,5]
print("Max Number",max(num))

'''
Question 2
Write a Python function that checks whether a passed string is palindrome or not
'''
def palindrome(str,reverse_str):
    if str == reverse_str:
        return("Palindrome True")
    else:
        return("Palindrome False")

str=input("Enter the text :")
reverse_str=str[::-1]

print("Orginal text",str)
print("Reverse text",reverse_str)

print(palindrome(str,reverse_str))

'''
Question 3
Write a Python function that accepts a string and calculate the number of uppercase letters and
lowercase letters

'''

def letter(str):
    upper=0
    lower=0
    for word in str:
        if word.isupper()==True:
            upper+=1
        elif word.islower()==True:
            lower+=1
        else:
            pass
    return("Upper case",upper,"Lower case",lower)



str=input("Enter the text :")

print(letter(str))

'''
Question 4
Write a Python function to sum all the numbers in a list
'''

from math import fsum

def sum(list1):
    print(fsum(list1))

list1=[3,4,5,2]
sum(list1)

'''
Question 5
Write a Python function to multiply all the numbers in a list

'''

import math
def multi(list1):
    print("Muliply of List Value",math.prod(list1))

list1=[3,5]
print("Orginal List Value",list1)
multi(list1)

'''
Question 6
Write a Python function that takes a list and returns a new list with unique elements of the first list

'''
def unique(list1):
    s=set(list1)
    print("Unique Value:",s)


long=[]
i=int(input("Enter count of number to insert in list:"))
while(i>0):
    data=input("Enter the number:")
    long.append(data)
    i-=1
print("List of numbers:",long)
unique(long)




