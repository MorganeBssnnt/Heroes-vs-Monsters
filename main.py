from character import Hero, Monster
from weapon import Sword, Club
from shield import Shield
from food import Food
from inventory import Inventory
import random

#---------------------------------------------------------
#----------------------- Objects -------------------------
#---------------------------------------------------------
# List of weapons
sword1 = Sword("Excalibur", 10, 90, 1500)
sword2 = Sword("Royal sword", 9, 100, 1600)
club1 = Club("Slaughter", 8, 70, 2000)
club2 = Club("Death", 5, 30, 1200)

# List of shields
shield1 = Shield("Durnval", 5, 1200)
shield2 = Shield("Shield2", 7, 1500)

# List of food
apple = Food("Apple",10, 100)
grapes = Food("Grapes", 8, 80)

#---------------------------------------------------------
#----------------------- Inventories ---------------------
#---------------------------------------------------------
# Arthur inventory
arthur_inventory = Inventory()
# Weapons
arthur_inventory.add_weapon(sword1)
arthur_inventory.add_weapon(sword2)
# Food
arthur_inventory.add_food(apple, quantity=7)

# Knight1 inventory
knight1_inventory = Inventory()
# Weapons
knight1_inventory.add_weapon(sword2)
knight1_inventory.add_weapon(club1)
# Shields
knight1_inventory.add_shield(shield1)
# Food
knight1_inventory.add_food(grapes, quantity=2)

# Monster inventory
monster_inventory = Inventory()
# Weapons
monster_inventory.add_weapon(club2)
monster_inventory.add_weapon(club1)
# Shields
monster_inventory.add_shield(shield2)
# Food
monster_inventory.add_food(grapes, quantity=1)

#---------------------------------------------------------
#----------------------- Heroes --------------------------
#---------------------------------------------------------
arthur = Hero("Arthur", 30, arthur_inventory, 100)
knight1 = Hero("Knight1", 20, knight1_inventory, 70)

#---------------------------------------------------------
#----------------------- Monsters ------------------------
#---------------------------------------------------------
grum1 = Monster("Grum1", 25, monster_inventory, 42)

#---------------------------------------------------------
#----------------------- Create teams --------------------
#---------------------------------------------------------
def create_team(team_type):
    team = []
    if team_type == "heroes":
        # List of heroes
        team.extend([arthur, knight1])
    elif team_type == "monsters":
        # List of monsters
        team.append(grum1)
    return team

#---------------------------------------------------------
#----------------------- Main function -------------------
#---------------------------------------------------------
def main(): 

    # Create teams
    heroes = create_team("heroes")
    monsters = create_team("monsters")

    # Randomly choose which team attacks first
    if random.choice([True, False]):
        attacking_team = heroes
        defending_team = monsters
        print("Heroes attack first !")
    else: 
        attacking_team = monsters
        defending_team = heroes
        print("Monsters attack first !")

    # Loop : until one team is defeated
    while heroes and monsters : 
        # Each character attacks once
        for attacker in attacking_team:
            # Randomly select a defender
            defender = random.choice(defending_team)
            # Randomly choose action for the character
            action = random.choice(["attack", "defend","eat"])
            if action == "attack":
                attacker.attack(defender)
            elif action == "defend":
                attacker.defend(defender)
            elif action == "eat":
                # Ensure the character has food to eat
                if attacker.food_inventory:
                    # Randomly select food item to eat
                    food_item = random.choice(attacker.food_inventory)
                    # Call the eat method with the selected food item
                    attacker.eat(food_item)
                else:
                    print(f"{attacker.name} has no food to eat!")
                    # Skip the turn if no food is available
                    continue  

            # If the defender is still alive, it couterattacks
            if defender.health > 0:
                defender.attack(attacker)
        
        # Update teams after each turn
        heroes = [hero for hero in heroes if hero.health > 0]
        monsters = [monster for monster in monsters if monster.health > 0]

    # Display results
    if heroes: 
        print("Heroes win !")
    else: 
        print("Monsters win !")        