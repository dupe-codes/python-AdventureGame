
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
    def __init__(self, name, char_type):
        self.character = classes[char_type]
        self.name = name

        # Rating of Character's Morale 
        self.morale = 0 

        # Rating of character's opinion of player character 
        self.playerOpinion = 0

        # Maps story events to character's opinion of player actions
        self.memories = {}
    
    def updateHealth(self, change):
        self.character.health -= change
        return self.character.health
    
    def setHealth(self, health):
        self.character.health = health

    def getInfo(self):
        return self.name, self.character.health

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.skills = ['archery', 'fishing', 'bartering']
        
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

    def getInfo(self):
        return self.name, self.health, self.skills



    
        
