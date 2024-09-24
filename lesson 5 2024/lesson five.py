from character import Character
from  import Paladin
player1 = Character('grawlactor', 500, 20,10)
player1.show_stats()

player2 = Paladin('Nequard', 200, 20,7)
player2.show_stats()

player1.attack(player2)

print(f"\n{player1}\n{player2}\n")

a=3
b=5

print(id(a))
print(id(b))

class Paladin(Character):
    def __init__(self, name, health, damage,defense ,type = 'human'):
        Character.__init__(self, name ,health, damage,defense ,type )
    def take_damage (self,damage):
        damage-=

    def take_damage(self, damage):
        damage -=self.defense
        Character.take_damage(self, damage)