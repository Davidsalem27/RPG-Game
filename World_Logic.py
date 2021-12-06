

class World_L:

    def __init__(self):
        pass




class Character:

    def __init__(self,health,armor,strength):
        self.health = health
        self.armor = armor
        self.strength = strength

        self.weapons=[]
    def set_health(self, addition):
        self.health = self.health + addition
    def set_armor(self,new):
        self.armor = new
    def get_armor(self):
        return self.armor
    def get_strength(self):
        return self.strength + self.weapons[0]



class Hero(Character):
    def __init__(self,health,armor,strength,money,level):
        Character.__init__(self,health,armor,strength)
        self.money=money
        self.level=level
        self.bag = []

    def set_money(self,addition):
        self.money = self.money + addition
    def level_up(self):
        self.level += 1
        self.armor += 1
        self.health += 1
        self.strength += 1
    def get_items_bag(self):
        return self.bag

class Barbarian(Character):
    def __init__(self, health, armor, strength):
        Character.__init__(self, health, armor, strength)









