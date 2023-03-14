import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
            print(f"{self.name} attacks {enemy.name} and deals {damage} damage!")
        else:
            print(f"{self.name}'s attack is too weak to damage {enemy.name}!")

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.experience = 0
        self.level = 1

    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} gains {experience} experience points!")
        if self.experience >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 5
        self.attack += 2
        self.defense += 2
        self.experience = 0
        print(f"{self.name} levels up to level {self.level}!")

class Enemy(Character):
    def __init__(self, name, health, attack, defense, experience):
        super().__init__(name, health, attack, defense)
        self.experience = experience

    def drop_loot(self):
        loot_table = {
            "gold": random.randint(0, 10),
            "potion": random.randint(0, 1),
            "sword": random.randint(0, 1)
        }
        print(f"{self.name} drops:")
        for item, quantity in loot_table.items():
            if quantity > 0:
                print(f"{quantity} {item}")
        return loot_table

def fight(player, enemy):
    print(f"{player.name} (Level {player.level}, Health {player.health}) vs {enemy.name} (Experience {enemy.experience}, Health {enemy.health})")
    while player.is_alive() and enemy.is_alive():
        player.attack_enemy(enemy)
        if enemy.is_alive():
            enemy.attack_enemy(player)
    if player.is_alive():
        player.gain_experience(enemy.experience)
        loot_table = enemy.drop_loot()
        return loot_table
    else:
        print(f"{player.name} has been defeated!")
        return None

# Example usage
player = Player("Bob", 20, 5, 5)
goblin = Enemy("Goblin", 10, 3, 1, 5)

loot = fight(player, goblin)
if loot:
    print("Loot obtained:")
    for item, quantity in loot.items():
        print(f"{quantity} {item}")