from berserk import Berserk
from  paladin import Paladin

player1 = Berserk('grawlactor',  200, 20,7)
player1.show_stats()

player2 = Paladin('Nequard',500, 20,10)
player2.show_stats()

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)
print(f"\n{player1}\n{player2}\n")



a=3
b=5

print(id(a))
print(id(b))

