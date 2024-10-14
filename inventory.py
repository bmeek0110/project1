class Inventory:
    def __init__(self):
        self.items = {
            "Potion": 5,
            "Super Potion": 2,
            "Poké Ball": 10,
        }

    def use_item(self, item_name, target_pokemon):
        if item_name in self.items and self.items[item_name] > 0:
            if item_name == "Potion":
                target_pokemon.heal(10)
            elif item_name == "Super Potion":
                target_pokemon.heal(20)

            self.items[item_name] -= 1
            print(f"Used {item_name} on {target_pokemon.name}.")
