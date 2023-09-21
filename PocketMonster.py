# Michael Gee, mpgee@usc.edu
# ITP 115, Summer 2021
# Final Project

# a class was used to create each Pocket Monster
class PocketMonster(object):
    def __init__(self, name, type, strength, rarity):
        # def__init__ used to define instance attributes
        self.name = name # Pocket Monster's name, str
        self.type = type # Pocket Monster's type, str
        self.strength = strength # Pocket Monster's strength, int
        self.rarity = rarity # Pocket Monster's rarity, int

# the following are get methods that return the desired instance attribute for an instance of a Pocket Monster.
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getStrength(self):
        return int(self.strength)

    def getRarity(self):
        return int(self.rarity)

# def __str__ used to return a string containing all the instance attributes.
    def __str__(self):
        return self.name + " (" + self.type + ")" "\n\tStrength:" + str(self.strength) + "\n\tRarity:" + str(self.rarity)

