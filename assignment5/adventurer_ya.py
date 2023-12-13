import random
from Item import Pillar, Healing, Vision
class Adventurer:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(75, 100)
        self.hit_points = random.randint(75, 100)
        self.healing_potions = random.randint(1, 3)  # Adjust the range as needed
        self.vision_potions = random.randint(1, 3)  # Adjust the range as needed
        self.found_pillars = set()
        self.inventory = []
        self.location = [0, 0]  # Initialize the location attribute

    def move(self, direction):
        # Define the possible directions
        directions = {'north': [-1, 0], 'east': [0, 1], 'south': [1, 0], 'west': [0, -1]}

        # Check if the input direction is valid
        if direction.lower() in directions:
            # Calculate the new location based on the chosen direction
            new_location = [self.location[0] + directions[direction.lower()][0],
                            self.location[1] + directions[direction.lower()][1]]

            # Update the adventurer's location if the new location is within bounds
            if 0 <= new_location[0] < MAX_ROWS and 0 <= new_location[1] < MAX_COLS:
                self.location = new_location
                print(f"{self.name} moved {direction}. New location: {self.location}")
            else:
                print("Cannot move in that direction. Out of bounds.")
        else:
            print("Invalid direction. Please choose north, east, south, or west.")

    def use_healing_potion(self):
        if self.healing_potions > 0:
            healing_amount = random.randint(20, 30)  # Adjust the range as needed
            self.hit_points = min(100, self.hit_points + healing_amount)
            self.healing_potions -= 1
            return f"{self.name} used a Healing Potion and gained {healing_amount} hit points."
        else:
            return f"{self.name} has no Healing Potions."

    def use_vision_potion(self):
        if self.vision_potions > 0:
            self.vision_potions -= 1
            return f"{self.name} used a Vision Potion."
        else:
            return f"{self.name} has no Vision Potions."

    def find_pillar(self, pillar):
        self.found_pillars.add(pillar)
        return f"{self.name} found the Pillar of {pillar}!"

    def display_status(self):
        return f"{self.name}'s Status:\n" \
               f"Hit Points: {self.hit_points}\n" \
               f"Healing Potions: {self.healing_potions}\n" \
               f"Vision Potions: {self.vision_potions}\n" \
               f"Found Pillars: {', '.join(self.found_pillars)}"

    def has_all_pillars(self):
        return len(self.found_pillars) == 4

    def pick_up_item(self, item):
        if isinstance(item, Pillar):
            self.find_pillar(item.name)
        elif isinstance(item, Healing):
            # Adjust the healing logic based on your Healing class properties
            healing_amount = random.randint(20, 30)
            self.health = min(100, self.health + healing_amount)
            print(f"{self.name} picked up a Healing Potion and gained {healing_amount} health.")
        elif isinstance(item, Vision):
            # Adjust the vision logic based on your Vision class properties
            print(f"{self.name} picked up a Vision Potion.")
        else:
            print(f"{self.name} picked up an unknown item.")

# Example usage:

# Create an adventurer named "Hero"
hero = Adventurer("Hero")

# Display initial status
print(hero.display_status())

# # Example: Using a Healing Potion
# print(hero.use_healing_potion())
# print(hero.display_status())
#
# # Example: Using a Vision Potion
# print(hero.use_vision_potion())
# print(hero.display_status())
#
# # Example: Finding a Pillar
# print(hero.find_pillar("A"))
# print(hero.display_status())
