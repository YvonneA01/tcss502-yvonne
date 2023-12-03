import random

class Room:
    def __init__(self, room_id):
        self.room_id = room_id
        self.items = []
        self.exits = {'N': None, 'S': None, 'E': None, 'W': None}
        self.is_entrance = False
        self.is_exit = False
        self.pillar_of_oo = False

        # Generate items with 10% probability
        self.generate_items()

        # Distribute pillars among rooms
        if room_id == 1:
            self.pillar_of_oo = True

    def generate_items(self):
        # Healing potion, vision potion, and pit with 10% probability each
        if random.random() < 0.1:
            self.generate_healing_potion()
        if random.random() < 0.1:
            self.generate_vision_potion()
        if random.random() < 0.1:
            self.generate_pit()

    def generate_healing_potion(self):
        # Healing potion heals 5-15 hit points
        healing_amount = random.randint(5, 15)
        self.items.append(('Healing Potion', healing_amount))

    def generate_vision_potion(self):
        # Vision potion allows the user to see surrounding rooms
        vision_info = self.get_surrounding_rooms_info()
        self.items.append(('Vision Potion', vision_info))

    def generate_pit(self):
        # Pit damage is from 1-20 hit points
        pit_damage = random.randint(1, 20)
        self.items.append(('Pit', pit_damage))

    def get_surrounding_rooms_info(self):
        surrounding_rooms = {}
        for direction, room in self.exits.items():
            if room:
                surrounding_rooms[direction] = {
                    'room_id': room.room_id,
                    'items': room.items,
                    'is_entrance': room.is_entrance,
                    'is_exit': room.is_exit,
                    'pillar_of_oo': room.pillar_of_oo
                }
        return surrounding_rooms

    def set_entrance(self):
        # Mark the room as the entrance, and it contains NOTHING else
        self.is_entrance = True
        self.items = []

    def set_exit(self):
        # Mark the room as the exit, and it contains NOTHING else
        self.is_exit = True
        self.items = []

    def connect(self, direction, other_room):
        # Connect this room to another room in the specified direction
        self.exits[direction] = other_room

    def display_info(self):
        print(f"Room {self.room_id} - Exits: {', '.join([key for key, value in self.exits.items() if value is not None])}")
        if self.items:
            for item in self.items:
                item_name, item_value = item
                if item_name == 'Vision Potion':
                    print(f"{item_name}: {item_value}")
                else:
                    print(f"{item_name}: {item_value} hit points")
        if self.is_entrance:
            print("Entrance")
        if self.is_exit:
            print("Exit")
        if self.pillar_of_oo:
            print("Pillar of OO")
        print("\n")

    def __str__(self):
        # Represent doors, boundaries, and contents
        boundary = "***"
        doors = "*-*"
        east_door = "|" if self.exits['E'] else boundary
        west_door = "|" if self.exits['W'] else boundary
        north_door = doors if self.exits['N'] else boundary
        south_door = doors if self.exits['S'] else boundary

        center_content = ' '  # Default is an empty room

        if self.is_entrance:
            center_content = 'E'
        elif self.is_exit:
            center_content = 'O'
        elif self.pillar_of_oo:
            center_content = random.choice(['A', 'E', 'I', 'P'])
        elif any(item[0] == 'Vision Potion' for item in self.items):
            center_content = 'V'
        elif any(item[0] == 'Healing Potion' for item in self.items):
            center_content = 'H'
        elif any(item[0] == 'Pit' for item in self.items):
            center_content = 'X'
        elif self.items:
            center_content = 'M'

        return f"{north_door}\n|{center_content}|\n{south_door}"

    def move(self, direction, adventurer):
        next_room = self.exits.get(direction)
        if next_room:
            # Implement logic for hit points change based on room contents
            for item in next_room.items:
                item_name, item_value = item
                if item_name == 'Healing Potion':
                    adventurer.hit_points = min(100, adventurer.hit_points + item_value)
                    return f"{adventurer.name} moved {direction} and found a Healing Potion. " \
                           f"{adventurer.name}'s hit points increased to {adventurer.hit_points}."
                elif item_name == 'Pit':
                    adventurer.hit_points = max(0, adventurer.hit_points - item_value)
                    return f"{adventurer.name} moved {direction} and fell into a Pit. " \
                           f"{adventurer.name}'s hit points decreased to {adventurer.hit_points}."
            # If no special items in the room, just move to the next room
            return next_room
        else:
            return None

# Example usage:

# Create rooms
room1 = Room(1)
room2 = Room(2)
room3 = Room(3)
room4 = Room(4)

# Connect rooms
room1.connect('N', room2)
room2.connect('S', room1)
room2.connect('E', room3)
room3.connect('W', room2)
room3.connect('N', room4)
room4.connect('S', room3)

# Mark entrance and exit
room1.set_entrance()
room4.set_exit()

# Display information about each room
room1.display_info()
room2.display_info()
room3.display_info()
room4.display_info()

# Print the graphical representation
print(room1)
print(room2)
