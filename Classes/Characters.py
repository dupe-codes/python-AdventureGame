
from Information import characterAttributes

class Player():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.skills = ['archery', 'fishing', 'bartering']

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

test = Player('Bob')
print test.name
test.addSkill('brawling')
print test.getInfo


    
        
