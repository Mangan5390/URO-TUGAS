from weapon import fists, love, bow
from health_bar import HealthBar


class Character():
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()

        print(f"{self.name} dealth {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name = name, health = health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")
        

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        self.weapon = self.default_weapon

class Opponent(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name = name, health = health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="red")

    def drop(self) -> None:
        self.weapon = self.default_weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")


character1 = Hero(name = "RobotJohn", health=100)
character2 = Hero(name = " RobotJean", health= 100)
character3 = Hero(name = "RobotAurel", health= 100)

character4 = Opponent(name = "Kunti", health= 75)
character5 = Opponent(name = "Poci", health= 70)
character6 = Opponent(name = "Kerek", health= 66)

heroes_list = [character1, character2, character3]
opponents_list = [character4, character5, character6]