
from characterAttributes import *

#classes = {'archer': Archer(), 'swordsman': Swordsman(), 'gunman': Gunman()}

class Archer():
    def __init__(self):
        self.health = 50
    
class Swordsman():
    def __init__(self):
        self.health = 125

class Gunman():
    def __init__(self):
        self.health = 75

classes = {'archer': Archer(), 'swordsman': Swordsman(), 'gunman': Gunman()}
        
class Ally:
    def __init__(self, name, char_type, opinion, morale):
        self.character = classes[char_type]
        self.name = name
        self.inventory = []

        # Rating of Character's Morale 
        self.morale = morale 

        # Rating of character's opinion of player character 
        self.playerOpinion = opinion

        # Maps story events to character's opinion of player actions
        self.memories = {}
    
    def updateHealth(self, change):
        self.character.health -= change
        return self.character.health
    
    def setHealth(self, health):
        self.character.health = health

    def updateMorale(self, change):
        self.morale += change

    def updateOpinion(self, change):
        self.playerOpinion += change

    def inInventory(self, item):
        return item in self.inventory

    def addToInventory(self, item):
        self.inventory.append(item)

    def removeFromInventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def getInfo(self):
        return self.name, self.character.health, self.inventory

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.skills = ['archery', 'fishing', 'bartering']
        self.inventory = ['bow', 'arrows']
        
        # Map of story event names to player decisions in those events.
        self.decisions = {} 
        
        # List of characters in player's party
        # Stored as their character objects 
        self.partymembers = []

    def updateHealth(self, change):
        self.health -= change
        return self.health

    def addSkill(self, skill):
        if(skill in availableSkills):
            self.skills.append(skill)
            return 'success'
        else: 
            print skill, ' is not a valid skill'
            return 'failure'
    
    def setHealth(self, health):
        self.health = health

    def inInventory(self, item):
        return item in self.inventory

    def addToInventory(self, item):
        self.inventory.append(item)

    def removeFromInventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def addToParty(self, ally):
        self.partymembers.append(ally)

    def removeFromParty(self, character):
        if character in self.partymembers:
            self.partymembers.remove(character)
            return True
        else: 
            return False

    def getInfo(self):
        return self.name, self.health, self.skills, self.inventory



    
        
