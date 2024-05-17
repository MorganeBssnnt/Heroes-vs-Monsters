from weapon import Weapon
from inventory import Inventory
import random

#---------------------------------------------------------
#----------------------- Character class -----------------
#---------------------------------------------------------
class Character:
    # Set initial values for the class
    def __init__(self, name, health, inventory, stamina):
        self.name = name
        self.health = health
        self.weapon_equipped = inventory.weapons[0] if inventory.weapons else None
        self.shield_equipped = inventory.shields[0] if inventory.shields else None
        self.stamina = stamina
        self.food_inventory = inventory.foods
        self.inventory = inventory

    #---------------------------------------------------------
    #----------------------- Character Methods ---------------
    #---------------------------------------------------------
    # Method : Attack
    def attack(self, enemy):
        # Check if the character has enough stamina to attack
        if self.stamina <= 0:
            # Print "not enough stamina" message
            print(f"{self.name} does not have enough stamina to attack !")
            return
        #Randomly select a weapon from character inventory
        if self.weapon_equipped:
            weapon_to_use = self.weapon_equipped
        elif self.inventory.weapons:
            weapon_to_use = random.choice(self.inventory.weapons)
        # Print the attack action : the attacker's name, the enemy's name, and the weapon used
        print(f"{self.name} attacks {enemy.name} with {weapon_to_use.name}")    
        # Damage dealt is the weapon's damage points
        damage_dealt = weapon_to_use.damage
        enemy.get_damage(damage_dealt)
        # Reduce stamina based on weapon stamina cost
        self.stamina -= weapon_to_use.stamina_cost()
        enemy.get_damage(damage_dealt)
    
    # Method : Defend
    def defend(self, enemy):
        if self.shield_equipped:
            # Check if the character has enough stamina to attack
            if self.stamina <= 0:
                # Print "not enough stamina" message
                print(f"{self.name} does not have enough stamina to defend !")
                return
            # Calculate damage reduction using shield's damage absorption
            damage_reduction = min(enemy.weapon_equipped.damage, self.shield_equipped.damage_absorption)
            # Reduce damage
            actual_damage = max(0, enemy.weapon_equipped.damage - damage_reduction)
            self.get_damage(actual_damage)
            print(f"{self.name} defends against {enemy.name} with {self.shield_equipped.name}, reducing damage by {damage_reduction}")
            # Reduce stamina based on shield weight
            self.stamina -= self.shield_equipped.weight/1000
        else: 
            print(f"{self.name} has no shield equipped !")

    # Method: Get damage
    def get_damage(self, damage):
        # Reduce the health points by the amount of damage taken
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} is KO !")
    
    # Method : Equip shield
    def equip_shield(self, shield):
        self.shield_equipped = shield
    
    # Method : Eat food to regain stamina
    def eat(self, food=None):
        if food is None:
            print(f"{self.name} needs food !")
            return
        if self.stamina >= 100:
            print(f"{self.name} is already full !")
            return
        print(f"{self.name} eats {food.name} and recovers {food.stamina_recovery_points} stamina points.")
        # Increase stamina
        self.stamina = min(100, self.stamina + food.stamina_recovery_points)
        # Remove food from inventory
        self.food_inventory.remove(food)

#---------------------------------------------------------
#----------------------- Hero Class ----------------------
#---------------------------------------------------------
# Inherit from Character class
class Hero(Character):
    # Define the constructor
    def __init__(self, name, health, inventory, stamina):
        # Call the parent class's parameters
        super().__init__(name, health, inventory, stamina)

#---------------------------------------------------------
#----------------------- Monster Class -------------------
#---------------------------------------------------------
# Inherit from Character class
class Monster(Character):
    # Define the constructor
    def __init__(self, name, health, inventory, stamina):
        # Call the parent class's parameters
        super().__init__(name, health, inventory, stamina)