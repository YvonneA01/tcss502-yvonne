import random

class Room:
    def __init__(self, items):
        self.items = items

# Define the Adventurer class
class Adventurer:
    def __init__(self, name):
        self.name = name
        self.hit_points = random.randint(75, 100)
        self.total_healing_potions = 0
        self.total_vision_potions = 0
        self.pillars_found = set()

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Hit Points: {self.hit_points}\n"
            f"Total Healing Potions: {self.total_healing_potions}\n"
            f"Total Vision Potions: {self.total_vision_potions}\n"
            f"Pillars Found: {', '.join(self.pillars_found)}"
        )

    def enter_room(self, room):
        for item in room.items:
            if item == 'Healing Potion':
                self.pick_up_healing_potion(room)
            elif item == 'Vision Potion':
                self.pick_up_vision_potion(room)
            elif item == 'Pit':
                self.fall_in_pit(room)

    def pick_up_healing_potion(self, room):
        room.items.remove('Healing Potion')
        self.total_healing_potions += 1
        print(f"{self.name} picked up a Healing Potion.")

    def pick_up_vision_potion(self, room):
        room.items.remove('Vision Potion')
        self.total_vision_potions += 1
        print(f"{self.name} picked up a Vision Potion.")

    def fall_in_pit(self, room):
        room.items.remove('Pit')
        damage = random.randint(1, 20)
        self.hit_points -= damage
        print(f"{self.name} fell into a pit and took {damage} damage.")

# Example usage:

# Create an instance of the Adventurer class
adventurer = Adventurer("Hero")

# Create a room with items
room_items = ['Healing Potion', 'Vision Potion', 'Pit']
room = Room(room_items)

# Adventurer enters the room
adventurer.enter_room(room)

# Display the adventurer's status
print(adventurer)