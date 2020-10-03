# creating a password validator
import re
password = input("Enter The Password :")
pw = 0
while True:
    if len(password < 7):
        pw = -1
        break
    elif not re.search("[0-9]", password):
        pw = -1
        break
    elif not re.search("[!@#$%&*]", password):
        pw = -1
        break
    else:
        pw = 0
        print("strong")
        break
if pw == -1:
    print("weak")