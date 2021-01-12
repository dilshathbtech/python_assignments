'''
Project 4
Do the project - Sending mail using Python
'''

import smtplib

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()

s.login("xxx@gmail.com","pcjkyvoxmbfvhpqv")

msg="Hi Dilshath"

s.sendmail("xxxx@gmail.com","xxxx@gmail.com",msg)

s.quit()
