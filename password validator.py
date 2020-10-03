# making a password validator
import re
password = input("Enter Your Password")
pw = 0
while True:
    if 5 > len(password) > 10:
        pw = -1
        break
    elif not re.search("[a-z]", password):
        pw = -1
        break
    elif not re.search("[A-Z]", password):
        pw = -1
        break
    elif not re.search("[!@#$%^&*+]", password):
        pw = -1
        break
    elif not re.search("[0-9]", password):
        pw = -1
        break
    elif re.search("[ ]", password):
        pw = -1
        break
    else:
        pw = 0
        print("password is valid")
        break
if pw == -1:
    print("Entered password is invalid")
