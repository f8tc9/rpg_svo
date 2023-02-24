import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            print(f"{self.name} hits {enemy.name} for {damage} damage!")
            enemy.take_damage(damage)
        else:
            print(f"{self.name}'s attack bounces off {enemy.name}'s defenses!")

class Player(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.items = {"Potion": 2}
        self.gold = 0

    def move(self, direction):
        if direction == "north":
            print(f"{self.name} moves north.")
        elif direction == "south":
            print(f"{self.name} moves south.")
        elif direction == "east":
            print(f"{self.name} moves east.")
        elif direction == "west":
            print(f"{self.name} moves west.")

    def use_item(self, item_name):
        if item_name in self.items:
            if item_name == "Potion":
                self.heal(50)
                self.items[item_name] -= 1
                if self.items[item_name] == 0:
                    del self.items[item_name]
                print(f"{self.name} drinks a potion and restores 50 health.")
            else:
                print("Invalid item.")
        else:
            print("Item not found.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} gains {amount} gold.")

class Enemy(Character):
    def __init__(self, name, hp, attack, defense, xp, gold):
        super().__init__(name, hp, attack, defense)
        self.xp = xp
        self.gold = gold

    def defeated(self):
        print(f"{self.name} has been defeated!")
        return self.xp, self.gold

class Game:
    def __init__(self):
        self.player = Player("Player", 100, 10, 5)
        self.enemies = [
            Enemy("Goblin", 50, 5, 2, 10, 5),
            Enemy("Skeleton", 75, 8, 4, 20, 10),
            Enemy("Orc", 100, 12, 6, 30, 15)
        ]
        self.current_enemy = None

    def start(self):
        print("Welcome to the game!")
        self.player.move("north")
        self.current_enemy = self.generate_enemy()
        self.battle()

    def generate_enemy(self):
        return random.choice(self.enemies)

    def battle(self):
        print(f"You encounter a {self.current_enemy.name}!")
        while self.current_enemy.hp > 0 and self.player.hp > 0:
            action = input("What will you do? (attack/use item/run)")
            if action == "attack":
                self.player.attack_enemy(selfdef battle(self):
    print(f"You encounter a {self.current_enemy.name}!")
    while self.current_enemy.hp > 0 and self.player.hp > 0:
        action = input("What will you do? (attack/use item/run)")
        if action == "attack":
            self.player.attack_enemy(self.current_enemy)
            if self.current_enemy.hp > 0:
                self.current_enemy.attack_enemy(self.player)
        elif action == "use item":
            item_name = input("Which item would you like to use?")
            self.player.use_item(item_name)
            if self.current_enemy.hp > 0:
                self.current_enemy.attack_enemy(self.player)
        elif action == "run":
            print(f"{self.player.name} runs away from the {self.current_enemy.name}.")
            self.current_enemy = self.generate_enemy()
            return
        else:
            print("Invalid action.")
        if self.current_enemy.hp == 0:
            xp, gold = self.current_enemy.defeated()
            self.player.add_gold(gold)
            self.player.heal(10)
            self.player.add_xp(xp)
            print(f"{self.player.name} gains {xp} experience and {gold} gold!")
            self.current_enemy = self.generate_enemy()
    if self.player.hp == 0:
        print(f"{self.player.name} has been defeated! Game over.")
    else:
        print(f"{self.player.name} has successfully defeated all the enemies and won the game!")

