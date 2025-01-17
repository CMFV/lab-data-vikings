
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage



class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health,strength)
        self.name = name

    def receiveDamage(self, damage):
        super(Viking, self).receiveDamage(damage)
        if self.health> 0: 
            return  "{} has received {} points of damage".format(self.name, self.damage)
        elif self.health <= 0:
            return  "{} has died in act of combat".format(self.name)
    def battleCry (self):
        return "Odin Owns You All!"  
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)
    
    def receiveDamage(self, damage):
        super(Saxon, self).receiveDamage(damage) 
        if self.health> 0: 
            return  "A Saxon has received {} points of damage".format(self.damage)
        elif self.health <= 0:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,Viking1):
        self.vikingArmy.append(Viking1)
    def addSaxon (self,Saxon1):
        self.saxonArmy.append(Saxon1)
    def vikingAttack (self):
        srandom = random.choice(self.saxonArmy)
        vrandom = random.choice(self.vikingArmy)
        Viking_attack = srandom.receiveDamage(vrandom.strength)
        if srandom.health <= 0: 
            self.saxonArmy.remove(srandom)
        return Viking_attack
    def saxonAttack(self):
        srandom=random.choice(self.saxonArmy)
        vrandom=random.choice(self.vikingArmy)
        Saxon_attack = vrandom.receiveDamage(srandom.strength) 
        if vrandom.health <= 0:
            self.vikingArmy.remove(vrandom)
        return Saxon_attack
    def showStatus(self):
        if len(self.saxonArmy) < 1:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) < 1:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >=1 and len(self.vikingArmy)>=1:
            return "Vikings and Saxons are still in the thick of battle."


