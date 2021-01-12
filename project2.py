import random
import psycopg2

##Postgresql Database 
con = psycopg2.connect(database="postgres", user="postgres", password="postgresql", host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()

cur.execute('''CREATE TABLE MOVIE
      (NAME           TEXT    NOT NULL);''')
print("Table created successfully")


cur.execute('''select * from movie''')
rows=cur.fetchall()

word=random.choice(rows)
s=[word]
print(s[0])

player = input("Write your Name: ") 
print("Guess the character: ") 
print("You have 10 chance to get the movie name: ") 
print("Best of luck!",player) 
count = 2
guess= "" 

while count>0: 
    fail = 0 
    for char in word: 
        if char in guess: 
            print(char) 
        else: 
            print("_") 
            fail+=1            
    if fail==0: 
        print("Congratulation you won!!!") 
        print("Movie Name was:",word) 
        break       
    g = input("Enter your character: ") 
    guess = guess+g  
    if g not in word: 
        count = count-1 
        print("Wrong Answer:(") 
        print("You have ",count,"more guesses") 


con.commit()
con.close()