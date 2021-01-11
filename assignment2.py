'''
Question 1
Write a Python program to remove duplicates from a list
'''

list_test=[1,2,4,89,5,2]
print("Orginal List",list_test)

temp=set(list_test)
print("Removed Duplicate ",temp)

'''
Question 2
Write a Python program to get the difference between the two lists
'''

list1=[12,324,42,21,2,6]
list2=[12,324,42,21,2,1,5]
print(list1)
print(list2)

list3=[]
for num in list1:
    if num not in list2:
        list3.append(num)

print("Difference b/w List1 and List2 ",list3)

'''
Question 3
Write a Python program to get the frequency of the elements in a list
'''

a=[1,1,5,3,2,5,2]

print(a)

num=int(input("Enter the value to get frequency of the elements in a list: "))
b=a.count(num)
print("frequency of the elements",num," in a list is",b)

'''
Question 4
Write a Python program to compute the similarity between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output: Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
'''

data1=["red", "orange", "green", "blue", "white"]
data2=["black", "yellow", "green", "blue"]

data3=[]
data4=[]

for num in data1:
    if num not in data2:
        data3.append(num)
print("Color1-Color2",data3)

for num in data2:
    if num not in data1:
        data4.append(num)
print("Color2-Color1",data4)

'''
Question 5
Write a Python function that takes a list of words and returns the length of the longest one
'''

long=[]
i=int(input("Enter number of strings to insert in list:"))
while(i>0):
    data=input("Enter the string:")
    long.append(data)
    i-=1
print("List of strings:",long)

count=[]
for num in long:
    a=int(len(num))
    count.append(a)

print("List of string length",count)

max=0
i=0
for num in count:
    if num > max:
        save=i
        max=num
        i+=1

print("Longest word",long[save])
print("Length of the word",count[save])


'''
Question 6
Write a Python program to count the occurrences of each word in a given sentence
'''


txt = input("Enter the sentence:")

x = txt.split()

print(x)

for num in x:
    b=x.count(num)
    print("frequency of the elements",num," in a list is",b)


'''
Question 7
Write a Python program to count and display the vowels of a given text
'''


txt = input("Enter the text:")
a=list(txt)
print(a)

vowels=("aeiouAEIOU")
b=list(vowels)
text_vowels=[]
for num in a:
    if num in b:
        text_vowels.append(num)

count=int(len(text_vowels))
print(count,"Vowels are present in the text, these all are the vowels",text_vowels)



'''
Question 8
Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x)
'''

n=int(input("Enter the number to generate:"))

d=dict()

i=1
while n > 0:
    d[i]=i*i
    i+=1
    n-=1
print("Output",d)

'''
Question 9
Write a Python program to combine two dictionary adding values for common keys
● d1 = {'a': 100, 'b': 200, 'c':300}
● d2 = {'a': 300, 'b': 200, 'd':400}
● Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print("First Dict",d1)
print("Second Dict",d2)

d3 ={}

d3=Counter(d1)+Counter(d2)

print("Result",d3)

'''
Question 10
Write a Python program to print all unique values in a dictionary
● Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
● Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''

d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

print("Original Text",d1)
d2=set()

for num in d1:
    for i in num.values():
        d2.add(i)

print("Unique Value",d2)






















