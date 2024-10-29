from character import Hero, Opponent, heroes_list, opponents_list
from weapon import  weapons_list

#var_weapon1 = input("Hi John choose your weapon:")
print("Choose your Hero!")
for hero in heroes_list:
    print(heroes_list.index(hero), hero.name)
hero = heroes_list[int(input())]
print(f"Choose your weapon {hero.name}!")
for weapon in weapons_list:
    print(weapons_list.index(weapon),weapon.name)
hero.equip(weapons_list[int(input())])
for opponent in opponents_list:
    print(opponents_list.index(opponent), opponent.name)
opponent = opponents_list[int(input())]
print(f"{hero.name} vs {opponent.name}")
input("Battle Start (click to continue)")


while True:
    hero.attack(opponent)
    opponent.attack(hero)

    hero.health_bar.draw()
    opponent.health_bar.draw()
    
    input()

    if hero.health <= 0:
        print(f"{opponent.name} win the game!")
        break    
    elif opponent.health <= 0:
        print(f"{hero.name} win the game")
        break

    