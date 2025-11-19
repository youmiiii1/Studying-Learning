from random import randint

class Character:
    def __init__(self):
        self.health = 100
        self.mana = 100
        self.speed = 25
        self.power = 70

    def skill_mana_regen(self):
        self.mana += randint(20, 50)
        print(m.my_stat())

    def skill_health_regen(self):
        self.health += randint(20, 50)
        print(m.my_stat())

    def my_stat(self):
        return f"Health: {self.health} | Mana: {self.mana} | Speed: {self.speed} | Power: {self.power}"

class Mag(Character):
    def __init__(self):
        super().__init__()
        self.mana = 200
        self.power = 50

    def skill_fireball(self):
        if self.mana < 100:
            print("Not enough mana!")
            print(m.my_stat())
        else:
            self.mana -= 50
            print("Using fire-ball!")
            print(m.my_stat())

class Knight(Character):
    def __init__(self):
        super().__init__()
        self.power = 150
        self.mana = 50
        self.health = 150

    def skill_slice(self):
        if self.mana < 50:
            print("Not enough mana!")
            print(k.my_stat())
        else:
            self.mana -= 50
            self.health -= 30
            print("Sword attack!")
            print(k.my_stat())

m = Mag()
k = Knight()

m.skill_fireball()
k.skill_slice()






