# Michael Gee, mpgee@usc.edu
# ITP 115, Summer 2021
# Final Project
from PocketMonster import PocketMonster
# PocketMonster class imported and used here.

class PMIndex(object):
    TYPES = ["Bug", "Dragon", "Electric", "Fighting", "Fire", "Fairy", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Water"]
    # TYPES is a class variable where each item is a Pocket Monster type.
    def __init__(self, file_name):
    # def __init__ used to define instance attributes.
    # each instance attribute is a list containing a certain type of Pocket Monster
        self.bug = []
        self.dragon = []
        self.electric = []
        self.fighting = []
        self.fire = []
        self.fairy = []
        self.ghost = []
        self.grass = []
        self.ground = []
        self.ice = []
        self.normal = []
        self.poison = []
        self.psychic = []
        self.rock = []
        self.water = []
        self.file_name = file_name
        file_name = "pm.csv"
        file_obj = open(file_name, "r")
        # the csv file containing all the Pocket Monsters is opened using open(file_name, "r").
        for line in file_obj:
        # the for loop is used to run through each Pocket Monster in the csv file.
            line = line.strip() # strip gets rid of white space
            pm_lst = line.split(",") # .split(",") used to turn each line into a list and for the commas to delineate each item.
            name = pm_lst[0] # each index of pm_lst is assigned to the corresponding variable
            type = pm_lst[1]
            strength = pm_lst[2]
            rarity = pm_lst[3]
            # each index from pm_lst is used to create an instance of a Pocket Monster
            pm = PocketMonster(name, type, strength, rarity)
            # each Pocket Monster is added to the appropriate list using the if and elif statements and .append(pm)
            if type == "Bug":
                self.bug.append(pm)
            elif type == "Dragon":
                self.dragon.append(pm)
            elif type == "Electric":
                self.electric.append(pm)
            elif type == "Fighting":
                self.fighting.append(pm)
            elif type == "Fire":
                self.fire.append(pm)
            elif type == "Fairy":
                self.fairy.append(pm)
            elif type == "Ghost":
                self.ghost.append(pm)
            elif type == "Grass":
                self.grass.append(pm)
            elif type == "Ground":
                self.ground.append(pm)
            elif type == "Ice":
                self.ice.append(pm)
            elif type == "Normal":
                self.normal.append(pm)
            elif type == "Poison":
                self.poison.append(pm)
            elif type == "Psychic":
                self.psychic.append(pm)
            elif type == "Rock":
                self.rock.append(pm)
            else:
                self.water.append(pm)
        file_obj.close()
        # the file is closed using .close()

    # returns a pocket monster from a type and a index
    def getMonster(self, type, index):
        self.type = type
        self.index = index
        type = input("Enter a type: ")
        index = input("Enter an index: ")
        # the user is prompted to input a type and an index.
        index = int(index)
        # the index is converted to an int so that it can be found in the appropriate list.
        # the appropriate Pocket Monster is found and returned using the if and elif statements and .append(pm)
        if type == "Bug":
            return self.bug[index]
        elif type == "Dragon":
            return self.dragon[index]
        elif type == "Electric":
            return self.electric[index]
        elif type == "Fighting":
            return self.fighting[index]
        elif type == "Fire":
            return self.fire[index]
        elif type == "Fairy":
            return self.fairy[index]
        elif type == "Ghost":
            return self.ghost[index]
        elif type == "Grass":
            return self.grass[index]
        elif type == "Ground":
            return self.ground[index]
        elif type == "Ice":
            return self.ice[index]
        elif type == "Normal":
            return self.normal[index]
        elif type == "Poison":
            return self.poison[index]
        elif type == "Psychic":
            return self.psychic[index]
        elif type == "Rock":
            return self.rock[index]
        elif type == "Water":
            return self.water[index]
        else:
            print("Invalid.")

    # returns a list of pocket monsters in the appropriate type.
    # this functions the same as getMonster except it returns an entire list of a certain type.
    def getMonsterType(self, type):
        if type == "Bug":
            return self.bug
        elif type == "Dragon":
            return self.dragon
        elif type == "Electric":
            return self.electric
        elif type == "Fighting":
            return self.fighting
        elif type == "Fire":
            return self.fire
        elif type == "Fairy":
            return self.fairy
        elif type == "Ghost":
            return self.ghost
        elif type == "Grass":
            return self.grass
        elif type == "Ground":
            return self.ground
        elif type == "Ice":
            return self.ice
        elif type == "Normal":
            return self.normal
        elif type == "Poison":
            return self.poison
        elif type == "Psychic":
            return self.psychic
        elif type == "Rock":
            return self.rock
        elif type == "Water":
            return self.water
        else:
            print("Invalid.")

    # prints a list of Pocket Monsters given by the type input.
    # this functions the same as getMonsterType except it takes an input from the user.
    def printMonsterType(self, type):
        type = input("Enter a type: ")
        if type == "Bug":
            return self.bug
        elif type == "Dragon":
            return self.dragon
        elif type == "Electric":
            return self.electric
        elif type == "Fighting":
            return self.fighting
        elif type == "Fire":
            return self.fire
        elif type == "Fairy":
            return self.fairy
        elif type == "Ghost":
            return self.ghost
        elif type == "Grass":
            return self.grass
        elif type == "Ground":
            return self.ground
        elif type == "Ice":
            return self.ice
        elif type == "Normal":
            return self.normal
        elif type == "Poison":
            return self.poison
        elif type == "Psychic":
            return self.psychic
        elif type == "Rock":
            return self.rock
        elif type == "Water":
            return self.water
        else:
            print("Invalid.")

    # returns the number of pm in the list
    def getNumMonsterType(self, type):
        if type == "Bug":
            return len(self.bug)
        elif type == "Dragon":
            return len(self.dragon)
        elif type == "Electric":
            return len(self.electric)
        elif type == "Fighting":
            return len(self.fighting)
        elif type == "Fire":
            return len(self.fire)
        elif type == "Fairy":
            return len(self.fairy)
        elif type == "Ghost":
            return len(self.ghost)
        elif type == "Grass":
            return len(self.grass)
        elif type == "Ground":
            return len(self.ground)
        elif type == "Ice":
            return len(self.ice)
        elif type == "Normal":
            return len(self.normal)
        elif type == "Poison":
            return len(self.poison)
        elif type == "Psychic":
            return len(self.psychic)
        elif type == "Rock":
            return len(self.rock)
        elif type == "Water":
            return len(self.water)
        else:
            print("Invalid.")

