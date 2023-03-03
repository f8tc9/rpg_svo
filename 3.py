class Shop:
    def __init__(self):
        self.inventory = {"health potion": 20, "mana potion": 30, "sword": 50, "armor": 100}

    def display_inventory(self):
        print("Welcome to the shop!")
        print("Here's what we have for sale:")
        for item, price in self.inventory.items():
            print(f"{item}: {price} gold")

    def buy(self, player, item_name):
        if item_name not in self.inventory:
            print(f"{item_name} is not available in the shop!")
        elif player.gold < self.inventory[item_name]:
            print("You don't have enough gold!")
        else:
            player.add_item(item_name)
            player.remove_gold(self.inventory[item_name])
            print(f"You bought {item_name} for {self.inventory[item_name]} gold!")

    def sell(self, player, item_name):
        if not player.has_item(item_name):
            print("You don't have that item!")
        else:
            player.remove_item(item_name)
            player.add_gold(int(self.inventory[item_name] * 0.5))
            print(f"You sold {item_name} for {int(self.inventory[item_name] * 0.5)} gold!")
class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = [Enemy("goblin", 20, 10), Enemy("skeleton", 30, 15), Enemy("troll", 50, 20)]
        self.current_enemy = None
        self.shop = Shop()

    def start(self):
        print("Welcome to the game!")
        self.player.choose_name()
        self.player.choose_class()
        self.current_enemy = self.generate_enemy()
        while True:
            action = input("What will you do? (explore/shop/quit)")
            if action == "explore":
                self.explore()
            elif action == "shop":
                self.shop.display_inventory()
                sub_action = input("What will you do? (buy/sell/leave)")
                if sub_action == "buy":
                    item_name = input("Which item would you like to buy?")
                    self.shop.buy(self.player, item_name)
                elif sub_action == "sell":
                    item_name = input("Which item would you like to sell?")
                    self.shop
