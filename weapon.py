#---------------------------------------------------------
#----------------------- Weapon class --------------------
#---------------------------------------------------------
class Weapon :
    def __init__(self,name, damage, length, weight):
        self.name = name
        self.damage = damage
        self.length = length
        self.weight = weight
    
    # Method : Calculate stamina cost
    def stamina_cost(self):
        return (self.length * self.weight) / 1000

#---------------------------------------------------------
#----------------------- Sword class ---------------------
#---------------------------------------------------------
# Inherit from Weapon class
class Sword(Weapon):
    # Define the constructor
    def __init__(self, name, damage, length, weight):
        # Call the parent class's parameters
        super().__init__(name, damage, length, weight)
        self.type = "Sword"

#---------------------------------------------------------
#----------------------- Club class ----------------------
#---------------------------------------------------------
# Inherit from Weapon class
class Club(Weapon):
    # Define the constructor
    def __init__(self, name, damage, length, weight):
        # Call the parent class's parameters
        super().__init__(name, damage, length, weight)
        self.type = "Club"