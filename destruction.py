"""
Python script that creates and destroys objects for fun
"""

class Building:
    def __init__(self, name):
        self.name = name

class House(Building):
    def __init__(self, name, num_rooms):
        super().__init__(name)
        self.num_rooms = num_rooms

class Apartment(House):
    def __init__(self, name, num_rooms, num_floors):
        super().__init__(name, num_rooms)
        self.num_floors = num_floors

# Create objects
my_building = Building("My Building")
my_house = House("My House", 3)
my_apartment = Apartment("My Apartment", 2, 5)

# Destroy objects
del my_building
del my_house
del my_apartment