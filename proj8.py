class Player:
    def __init__(self,name,lvl,health):
        self.name=name
        self.lvl=lvl
        self.health=health

    def attack(self):
        print(f"{self.name} is attacking!!")
    def heal(self):
        print(f"{self.name} is healing")
        self.health+=10
        print(f"{self.name} is healed now.His health is {self.health}")
    def lvlup(self):
        self.lvl+=1
        print(f"{self.name} leveled up.He reached level:{self.lvl}")

player_1=Player("Sohan",10,200)

player_1.attack()
player_1.heal()
player_1.lvlup()
player_1.heal()