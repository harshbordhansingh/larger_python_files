import random
game_running = True
result = 10
print("*"*32)
print("      Welcome To My Game")
print("*"*32)
print("Do you want to play the game or want to quit?")
print("*"*32)
print("If you want to continue press 0 \nAnd if u want to quit press 1")
print("*"*32)
print("If you want to take the first option press 5\nelse press 6 to take the second one")
print("*"*32)
print("The Game will end when you go below 0\nor above 21 and the game will start from 10.\nNow enjoy the game.")
print("*"*32)
choice = input("Enter Your Choice:")
while game_running:
    if choice == "1":
        game_running = False
    comp_choice1 = random.randint(-10, 10)
    comp_choice2 = random.randint(-10, 10)
    if choice == "0":
        print("1.")
        print(comp_choice1)
        print("\r")
        print("2.")
        print(comp_choice2)
    choice2 = input("Enter Your Choice(2nd):")
    if choice2 == "5":
        result += comp_choice1
        print("Your Number is:")
        print(result)
    elif choice2 == "6":
        result += comp_choice2
        print("Your Number is:")
        print(result)
    if result > 21 or result < 0:
        print("You Lose The Game\nBetter Luck Next Time.")
        game_running = False
