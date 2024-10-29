class Weapon():
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

iron_sword = Weapon(name = "Iron Sword", weapon_type = "close range", damage = 5, value = 10)
bow = Weapon(name = "bow", weapon_type = "long range", damage = 4, value = 8)
fists = Weapon(name="Fists", weapon_type="close range", damage=2, value=0)
love = Weapon(name="Love", weapon_type="feeling", damage= -1, value= 0)

weapons_list = [iron_sword, bow, fists, love]