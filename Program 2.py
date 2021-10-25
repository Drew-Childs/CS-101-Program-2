#Drew Childs, 9/18/19, Program 2 "Ship Dice"

import random

def print_menu():
    mylist = [1,2,3]
    print("Welcome to Ship Dice")
    print("You have 3 chances to win! Here are the game rules:")
    print("1 - 3 chances for all dices are 6")
    print("2 - 3 chances for at least one dice equal 5")
    print("3 - 3 chances for Red dice is 6, Green dice is 5, Blue dice is 4")
    global choice
    choice = int(input("Enter your choice\n"))
    while choice not in mylist:
        print("Invalid input, please choose an option from the above menu")
        choice = int(input("Enter your choice\n"))
    option()


def option():
    for step in range(3):
        print("Trial:", step + 1)
        red = random.randint(1, 6)
        green = random.randint(1, 6)
        blue = random.randint(1, 6)
        print("red", red, "green", green, "blue", blue)
        if choice == 1:
            if red == 6 and green == 6 and blue == 6:
                print("You Won!!\n")
                break
            else:
                print("No matching!\n")
        elif choice == 2:
            if red == 5 or green == 5 or blue == 5:
                print("You Won!!\n")
                break
            else:
                print("No matching!\n")
        elif choice == 3:
            if red == 6 and green == 5 and blue == 4:
                print("You Won!!\n")
                break
            else:
                print("No matching!\n")
    again = str(input("Do you want to play again?YES/yes\n"))
    if again == "YES" or again == "yes":
        print_menu()
    else:
        print("Good Game!")

print_menu()
