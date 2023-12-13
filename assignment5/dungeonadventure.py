from Rooms_and_Dungeons2 import Dungeon, Exit  # Assuming Dungeon class is in a separate module
from adventurer import Adventurer  # Assuming Adventurer class is in a separate module

class DungeonAdventure:
    def __init__(self, name):
        self.name = name
        self.hit_points = 100  # Assuming an initial value for hit points
        self.inventory = []
        self.location = [0, 0]  # Initialize the location attribute
        print("Welcome to Dungeon Adventure!")
        print("In this game, you are an adventurer exploring a mysterious dungeon.")
        print("Your goal is to find the treasure, collect all four pillars, and make it out alive!")
        print("Be careful of traps and monsters along the way. Use potions wisely to heal and see in the dark.")

        # Create a Dungeon object with dimensions 5x5
        self.dungeon = Dungeon(5, 5)
        self.dungeon.Set_Base_Dungeon()
        self.dungeon.Create_Maze(0, 0)

        # Display initial dungeon state
        print("\nInitial Dungeon State:")
        self.dungeon.Print_Dungeon_Maze()

        # Get the name of the adventurer from the user
        adventurer_name = input("\nEnter the name of your adventurer: ")
        self.adventurer = Adventurer(adventurer_name)

    def print_menu(self):
        print("\nOptions:")
        print("1. Move")
        print("2. Use Healing Potion")
        print("3. Use Vision Potion")
        print("4. Show Dungeon (hidden option)")

    def play_game(self):
        print("\nLet the adventure begin!")

        while True:
            print("\n" + "-" * 30)

            # Access the current room's information directly from the Dungeon object
            current_room = self.dungeon._Dungeon_Grid[self.adventurer.location[0]][self.adventurer.location[1]]
            print(f'Current Room: {current_room.coordinates}')

            # Check if there are items in the room
            if current_room._inventory_list:
                print("Items in the room:")
                for item in current_room._inventory_list:
                    print(f"- {item}")

                    # Allow the adventurer to pick up items
                    pick_up = input("Do you want to pick up any items? (y/n): ")
                    if pick_up.lower() == 'y':
                        # Assume adventurer can pick up all items in the room
                        for item in current_room._inventory_list:
                            self.adventurer.pick_up_item(item)
                            if isinstance(item, self.dungeon.Pillar):
                                # Check if the adventurer has all four pillars
                                if self.adventurer.has_all_pillars():
                                    print(f"Congratulations, {self.adventurer.name}! You collected all four pillars and the exit.")
                                    print("You won the game!")
                                    return  # Exit the game

                        current_room._inventory_list = []  # Remove picked up items from the room

            # Check if the adventurer has all four pillars after picking up items
            if self.adventurer.has_all_pillars():
                print(f"Congratulations, {self.adventurer.name}! You collected all four pillars and the exit.")
                print("You won the game!")
                break

            options = self.dungeon.Check_Travel(*self.adventurer.location)
            print("Options:", ", ".join(direction for direction, can_travel in zip(["North", "East", "South", "West"], options) if can_travel))

            self.print_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                direction = input("Enter the direction to move: ").lower()

                # Debug print
                print("Direction:", direction)
                print("Options:", options)

                # Access the current room's information directly from the Dungeon object
                current_room = self.dungeon._Dungeon_Grid[self.adventurer.location[0]][self.adventurer.location[1]]
                print(f'Current Room: {current_room.coordinates}, Type: {type(current_room).__name__}')

                # Update the current position after moving
                if direction == 'north' and options[0]:
                    self.adventurer.move('North')
                elif direction == 'east' and options[1]:
                    self.adventurer.move('East')
                elif direction == 'south' and options[2]:
                    self.adventurer.move('South')
                elif direction == 'west' and options[3]:
                    self.adventurer.move('West')
                else:
                    print("Invalid move. Try again.")
                    continue
            elif choice == '2':
                if self.adventurer.use_healing_potion():
                    print(f"{self.adventurer.name} used a healing potion and gained health!")
                    print(self.adventurer.display_status())
            elif choice == '3':
                if self.adventurer.use_vision_potion():
                    print(f"{self.adventurer.name} used a vision potion.")
                    print(self.adventurer.display_status())
            elif choice == '4':
                # Show the hidden option to print the dungeon
                self.dungeon.Print_Dungeon_Maze()
            else:
                print("Invalid choice. Please choose again.")

            # Check if the adventurer has won or died
            if isinstance(current_room, Exit):  # Use Exit class here
                print(f"Congratulations, {self.adventurer.name}! You found the treasure and won the game!")
                break
            elif self.adventurer.hit_points <= 0:
                print(f"Game Over, {self.adventurer.name}! You ran out of health and died.")
                break

        # Display the entire dungeon at the conclusion of the game
        print("\nFinal Dungeon State:")
        self.dungeon.Print_Dungeon_Maze()



# Create an instance of DungeonAdventure
game = DungeonAdventure("hero")

# Start the game
game.play_game()