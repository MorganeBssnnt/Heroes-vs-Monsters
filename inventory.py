#---------------------------------------------------------
#----------------------- Inventory class -----------------
#---------------------------------------------------------
class Inventory:
    def __init__(self):
        # Set empty lists to store : weapons, shields, an food
        self.weapons = []
        self.shields = []
        self.foods = []
    
    # Method : Add a weapon to the inventory
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    # Method : Add a shield to the inventory
    def add_shield(self, shield):
        self.shields.append(shield)
    # Method : Add food to the inventory
    def add_food(self, food, quantity=1):
        for _ in range(quantity):
            self.foods.append(food)