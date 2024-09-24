class Character:
    name = ''
    health = 100
    damage = 1
    defense = 0

    def __init__ (self,name,health,damage,defense, type='human'):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.type = type

    def show_stats(self):
        print(f"-- {self.name} --\nhealth {self.health}\n "
        f"damage : {self.damage}\ndefense: {self.defense}")

    def ___str___(self):
        return(f"-- {self.name} --\nhealth {self.health}\n "
        f"damage : {self.damage}\ndefense: {self.defense}")

    def take_damage(self, damage):
       # self.health -= damage
       # if self.health < 0:
       #     self.health = 0
       self.health = max(self.health - damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)