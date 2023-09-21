# Michael Gee, mpgee@usc.edu
# ITP 115, Summer 2021
# Final Project
from PocketMonster import PocketMonster
import random

class Trainer(object):
    MAXPM = 6
    MAXCC = 10
    # MAXPM and MAXCC are class variables that will be referenced later.
    def __init__(self, name):
        self.name = name # set to the name inputted.
        self.caught = [] # a list containing the successfully caught Pocket Monsters.
        self.capsules = 0 # initially the user starts with 0 capsules.

    # returns the number of capsules the user has.
    def getNumCapsules(self):
        return int(self.capsules)

    # returns the number of Pocket Monsters caught.
    def getNumCaught(self):
        return int(len(self.caught))

    # allows the user to buy capsules.
    def buyCapsules(self, purchase):
        purchase = int(purchase)
        # purchase is an input from the user and it is changed to an int.
        if purchase > 0 and purchase + int(self.capsules) <= Trainer.MAXCC:
        # if these conditions are satisfied, then the user's purchase will not make them exceed 10 capsules on top of what they already have.
            self.capsules = int(self.capsules) + purchase
            print("Purchased! You now have", int(self.capsules), "capsules.\n")
        else:
        # if all of these conditions cannot be satisfied, then the user is told their purchase was invalid.
            print("Invalid.")

    # adds a Pocket Monster to the user's list of Pocket Monsters.
    def addMonster(self, PocketMonster):
        self.caught.append(PocketMonster)

    # allows the user to release a Pocket Monster.
    def releaseMonster(self, index):
        index_valid = index.isdigit()
        # the user's input is checked to see if it's a digit using .isdigit()
        if index_valid == True:
        # if the user's input is a digit, it is converted to an int.
            index = int(index)
            if index in range(0, len(self.caught)):
            # if the given index is within the indices available at the time, then that Pocket Monster is removed.
                print("Goodbye", PocketMonster.getName(self.caught[index]), "\n")
                # .pop is used to remove based on index.
                self.caught.pop(index)
            else:
            # if the given index is not avalible, then the user is told their choice was invalid.
                print("Invalid number.\n")
        else:
            # if the given input is not a digit, then the user is told their choice was invalid.
            print("Invalid choice.\n")

    # used to start an encounter with a Pocket Monster in the Grassy Field.
    def encounter(self, PocketMonster):
        print("\nYou encountered a Pocket Monster!")
        print(PocketMonster)
        choice = input("\nChoose an action: \n0: Throw a Catch Capsule  \n1: Run \nChoose (select a number 0-1): ")
        choice_valid = choice.isdigit() and choice == "1" or choice == "0"
        # choice must be 0 or 1 for choice_valid to be true.
        while choice_valid == False:
        # if the conditions for choice valid are not met, then the while loop repeats until the user inputs a valid choice.
        # this prevents a new Pocket Monster from spawning each iteration of the while loop.
            print("Invalid choice. Please select a number from 0 to 1")
            choice = input("\nChoose an action: \n0: Throw a Catch Capsule  \n1: Run \nChoose (select a number 0-1): ")
            choice_valid = choice.isdigit() and choice == "1" or choice == "0"
        # if the user's input is valid then the lines above are skipped.
        choice = int(choice)
        if choice == 0:
        # the following runs if the user decides to throw a catch capsule.
            self.capsules = int(self.capsules)
            self.capsules = self.capsules - 1
            # the number of capsules decreases by 1
            randomInt = random.randrange(0, 3901)
            # a random int from 0 to 3900 inclusive is generated using the random module and randrange.
            a = int(PocketMonster.strength) * int(PocketMonster.rarity)
            if randomInt >= a:
            # if the Pocket Monster's strength multiplied by its rarity is greater than the random int generated, then the monster was caught.
            # the addMonster method is called on to add the monster.
                self.addMonster(PocketMonster)
                print("You caught it!")
                return 1  # pm was caught
            else:
            # if the Pocket Monster's strength multiplied by its rarity is NOT greater than the random int generated, then the monster escaped the capsule.
                print("It escaped the capsule.")
                if randomInt < int(PocketMonster.strength):
                # if the random int is less than the monster's strength, then it runs away.
                    print(" It ran away!\n")
                    return -1  # pm ran away
        elif choice == 1:
        # if the user chooses to run, then 0 is returned
            return 0
        elif self.capsules == 0:
        # if the user runs out of capsules, the round also ends.
            print("You ran out of capsules!\n")
            return -2
        # for any input that is not "0" or "1", the user is told their choice was invalid.
        else:
            print("Invalid choice. Please select a number from 0 to 1\n")

    # displays the strainer's stats
    def __str__(self):
        self.capsules = str(self.capsules)
        monsterStr = "\n"
        for item in self.caught:
        # uses a for loop to print each Pocket Monster the user has.
            itemStr = str(item)
            itemStr += "\n"
            monsterStr += itemStr
        return "Name: " + self.name + "\nCapsules: " + self.capsules + "\nMonsters:" + monsterStr