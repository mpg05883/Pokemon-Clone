from GrassyField import GrassyField
import random

def enterGrassyField(trainer):
    # if the number of Pokemon caught = the max number of pm allowed, return 0
    if trainer.getNumCaught() == Trainer.MAXPM:
        return 0
    # else if the trainer has 0 capsules, return 1
    elif trainer.getNumCapsules() == 0:
        return 1
    # if the trainer does not have the max pm and they have more than 0 capsules...
    else:
        while trainer.getNumCaught() < Trainer.MAXPM and trainer.getNumCapsules() > 0:
            found = False
            while not found:
                rarityNum = random.randint(1,100)
                if rarityNum > 90:
                    rarity = 5
                elif rarityNum > 70:
                    rarity = 4
                elif rarityNum > 50:
                    rarity = 3
                elif rarityNum > 30:
                    rarity = 2
                else:
                    rarity = 1
                monster = GrassyField.getRandomPocketMonster(rarity)
                if monster != None:
                    found = True
            ret = trainer.encounter(monster)
            if ret == 0:
                print("\nLeaving the grassy field...")
                return -1
        if trainer.getNumCaught() == Trainer.MAXPM:
            return 0
        else:
            return 1

# Name: getMenuSelection
# Parameter: none
# Return: an int representing the user's menu choice.
# Side effects: prints the menu options, takes the user's choice, and returns it.
# Description: displays the selection menu and calls on the option that the user inputs.
def getMenuSelection():
    choice_valid = 0
    while choice_valid == 0:
    # choice_valid is used to create a while loop.
    # the while loop is used so that if an invalid input is given, the user will be told their input was invalid and the menu will appear again.
        print("Select menu option: \n\t0) Enter Grassy Field \n\t1) Release Monsters \n\t2) Buy Catch Capsules \n\t3) Print Trainer Stats \n\t4) Quit")
        choice = input("Choose: ")
        choice_digit = choice.isdigit()
        # .isdigit() is used to see if the user's input is a digit.
        if choice_digit == True:
        # if the user did input a digit, choice is converted to an int.
            choice = int(choice)
            if choice >= 0 and choice <= 4:
            # the if statement is used to see if choice is a number on the menu.
            # if choice satisfies these conditions, then it must be one of the choices on the menu.
            # therefore it is valid and choice is returned.
                return choice
            else:
            # the else statement runs if choice does not satisfy both conditions.
            # if choice does not satisfy both conditions, then it must be a number that is NOT on the menu.
            # the user is told their choice was invalid and the while loop prints the menu again
                print("Invalid choice. Please choose a number from 0 to 4.\n")
        else:
        # if the user did not input a digit, the while loop will print the menu again.
            print("Invalid choice. Please choose a number from 0 to 4.\n")

# Name: releaseMonsters
# Parameter: a Trainer object
# Return: none
# Side effects: asks for an input and uses said input to remove the desired Pocket Monster from Trainer.caught by calling Trainer.releaseMonster(index).
# Description: releases the desired Pocket Monster back into the grassy field.
from Trainer import Trainer
def releaseMonsters(Trainer):
    # prints the number of monsters the user has
    # len(Trainer.caught) is used to display the number of monsters the user has currently.
    print("You have", len(Trainer.caught), "monsters.\n")
    if len(Trainer.caught) != 0:
    # if the user does not have 0 monsters, then the following runs.
    # otherwise if the user has 0 monsters, then they are returned to the selection menu.
        for i in range(0, len(Trainer.caught)):
        # the for loop is used to print each monster the user has.
        # each monster is assigned a number i using the for loop.
        # this number i also corresponds to their index in Trainer.caught
            monster = Trainer.caught[i]
            monsterStr = str(monster)
            i = str(i)
            print(i+")", monsterStr)
            # each index number and monster is printed with the for loop.
        index = input("Which would you like to give up? ")
        Trainer.releaseMonster(index) #Trainer.releaseMonster(index) is called on to release the monster at that index.

# Name: enterShop
# Parameter: a Trainer object
# Return: none
# Side effects: asks the user how many capsules they'd like to purchase and evaluates if the purchase is valid.
# Description: if the user's purchase is greater than 0 and they do not exceed 10 capsules on top of what they already have, then the purchase goes through.
#               otherwise, the user is told their purchase was invalid.
def enterShop(Trainer):
    if Trainer.capsules == 10:
        print("You have the maximum number of capsules. \n")
    else:
        purchase_valid = 0
        while purchase_valid == 0:
        # the while loop is used to repeat enterShop if an invalid input is given.
            purchase = input("Welcome to the shop! \nHow many capsules would you like to purchase? ")
            purchase_digit = purchase.isdigit()
            if purchase_digit == True:
            # if the user's input is a digit, then the following runs.
                purchase = int(purchase)
                # purchase is converted to an int
                b = purchase + int(Trainer.capsules)
                # the sum of the user's purchase and their current number of capsules is assigned to b.
                if purchase > 0 and b <= Trainer.MAXCC:
                # if the user is purchasing more than 0 capsules and they won't exceed 10 capsules then purchase_valid is set to 1 to end the while loop.
                # Trainer.buyCapsules(purchase) is called on to add the number of capsules purchased.
                    purchase_valid = 1
                    Trainer.buyCapsules(purchase)
                else:
                # if the conditions are not satisfied then the user is told their input was invalid and enterShop starts over.
                    print("Invalid choice!\n")
            else:
                print("Invalid choice!\n")
                # if the conditions are not satisfied then the user is told their input was invalid and enterShop starts over.

# Name: main
# Parameter: none
# Return: none
# Side effects: gets input from getMenuSelection and calls on the appropriate function or method.
# Description: starts the Pocket Monster Simulator.
def main():
    trainerName = "Michael Gee"
    trainer = Trainer(trainerName)
    done = False
    while not done:
        choice = getMenuSelection()
        if choice == 0:
            ret = enterGrassyField(trainer)
            if ret == 0:
                print("You caught the maximum number of monsters!\n")
            elif ret == 1:
                print("\nYou cannot enter the Grassy Field, you don't have any capsules!\n")
            else:
                print("You ran away!\n")
        elif choice == 1:
            releaseMonsters(trainer)
        elif choice == 2:
            enterShop(trainer)
        elif choice == 3:
            print("\nTrainer Stats")
            print(trainer)
        else:
            print("\nThank you for playing!")
            done = True
main()