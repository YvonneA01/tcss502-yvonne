<<<<<<< HEAD
import math
import random


class Dungeon:

    class Room:
        def __init__(self):
            self._northern_wall=True
            self._western_wall=True

        @property
        def coordinates(self):
            return self.__str__()

        def __str__(self):
            return f'(R: {self._grid_x}, C: {self._grid_y})'

        '''def __str__(self):
            if self._northern_room==None:
                n_check="None"
            else:
                n_check="Value"
            if self._southern_room==None:
                s_check="None"
            else:
                s_check="Value"
            if self._eastern_room==None:
                e_check="None"
            else:
                e_check="Value"
            if self._western_room==None:
                w_check="None"
            else:
                w_check="Value"
            return f'(N:{n_check},S:{s_check},E:{e_check},W:{w_check})'''''


    class Interior_Room(Room):
        "The dungeon consists of these rooms.  These are the rooms the player can move around in"
        def __init__(self,grid_x,grid_y):
            super().__init__()
            self._dm_visited=False
            self._inventory_list=[]
            self._grid_x=str(grid_x) #x corresponds with the row of the dungeon
            self._grid_y=str(grid_y) #y corresponds with the column of the dungeon


    def __init__(self,num_rows,num_columns):
        self._num_rooms=0
        self._num_rows=num_rows
        self._num_columns=num_columns
        self._Dungeon_Grid=[] #the Dungeon Grid is a list of lists (two d array) that possesses all the rooms


    def Set_Base_Dungeon(self):
        "Builds the grid of rooms with the entered specifications"
        for r in range(self._num_rows):
            self._Dungeon_Grid.append([])
            for c in range(self._num_columns):
                self._Dungeon_Grid[r].append(Dungeon.Interior_Room(r,c))

    def Print_Dungeon1(self):
        "This method is just to help me make sure I was giving the rooms the right coordinates."
        for r in range(self._num_rows):
            for c in range(self._num_columns):
                print(self._Dungeon_Grid[r][c].coordinates, end=" ")
            print("")
        print("")


    def Print_Dungeon_Maze(self):
        "This method is just to help me visualize the maze.  We could show it to the player after the game is over."
        "Otherwise it has no purpose."
        "Print the Northern most boundary walls"
        for c in range(self._num_columns*2+1):
            print("X", end="")
        print("")

        "Print the first row of rooms"
        for c in range(self._num_columns):
            if self._Dungeon_Grid[0][c]._western_wall==True:
                print("XO",end="")
            else:
                print(" O",end="")
        print("X")

        "Now loop to print the middle rooms:"
        for r in range(1,self._num_rows):
            for c in range(self._num_columns):
                if self._Dungeon_Grid[r][c]._northern_wall==True:
                    print("XX",end="")
                else:
                    print("X ",end="")
            print("X")
            for c in range(self._num_columns):
                if self._Dungeon_Grid[r][c]._western_wall==True:
                    print("XO",end="")
                else:
                    print(" O",end="")
            print("X")

        "Now print the Southern most boundary walls"
        for c in range(self._num_columns * 2 + 1):
            print("X", end="")
        print("")

    def Check_Travel(self,row_location,column_location):
        "This method helps me build the maze. It helps direct the Dungeon Master as he goes around knocking down walls."
        can_travel=[False,False,False,False]
        if row_location-1>=0 and self._Dungeon_Grid[row_location-1][column_location]._dm_visited==False:
            can_travel[0]=True
        if column_location+1<=self._num_columns-1 and self._Dungeon_Grid[row_location][column_location+1]._dm_visited==False:
            can_travel[1]=True
        if row_location+1<=self._num_rows-1 and self._Dungeon_Grid[row_location+1][column_location]._dm_visited==False:
            can_travel[2]=True
        if column_location - 1 >= 0 and self._Dungeon_Grid[row_location][column_location - 1]._dm_visited == False:
            can_travel[3]=True
        return can_travel


    def Create_Maze(self, row_location, column_location):
        "This is the recursive algorithm for building the maze."
        self.Print_Dungeon_Maze()

        self._Dungeon_Grid[row_location][column_location]._dm_visited=True

        can_travel=self.Check_Travel(row_location,column_location)
        print(can_travel)


        while True in can_travel:

            direction=random.randint(0,3) #0=try to go north #1=try to go east #2=try to go south #3= try to go west

            if can_travel[0]==True and direction==0:
                self._Dungeon_Grid[row_location][column_location]._northern_wall=False
                can_travel[0]=False
                print("DM will move North!")
                print("")
                self.Create_Maze(row_location-1,column_location)
                can_travel = self.Check_Travel(row_location, column_location)
            if can_travel[1]==True and direction==1:
                self._Dungeon_Grid[row_location][column_location+1]._western_wall=False
                can_travel[1]=False
                print("DM will move East!")
                print("")
                self.Create_Maze(row_location,column_location+1)
                can_travel = self.Check_Travel(row_location, column_location)
            if can_travel[2]==True and direction==2:
                self._Dungeon_Grid[row_location+1][column_location]._northern_wall=False
                can_travel[2]=False
                print("DM will move South!")
                print("")
                self.Create_Maze(row_location+1,column_location)
                can_travel = self.Check_Travel(row_location, column_location)
            if can_travel[3]==True and direction==3:
                self._Dungeon_Grid[row_location][column_location]._western_wall=False
                can_travel[3]=False
                print("DM will move West!")
                print("")
                self.Create_Maze(row_location,column_location-1)
                can_travel = self.Check_Travel(row_location, column_location)

    
    class Adventurer:                          # Modified adventurer class added to the original Dungeon and Room codes. Some work neeeds to be done for proper integration
        def __init__(self, name):
            self.name = name
            self.inventory = {
                "Healing Potion": 0,
                "Greater Healing Potion": 0,
                "Superior Healing Potion": 0,
                "Supreme Healing Potion": 0,
            }

        def move(self, direction):
            # Assume movement logic here
            pass

        def knock_down_wall(self, dungeon, row, col):
            # Example logic to knock down walls
            room = dungeon._Dungeon_Grid[row][col]
            room._northern_wall = False
            # Update other walls accordingly based on direction
            # Example: room._western_wall = False for moving west

        def pick_up_potion(self, room):
            available_potions = ["Healing Potion", "Greater Healing Potion", "Superior Healing Potion", "Supreme Healing Potion"]
            potion = random.choice(available_potions)
            room._inventory_list.remove(potion)
            self.inventory[potion] += 1
            print(f"{self.name} picked up a {potion}.")

    
        #Other adventurer methods such as enter_room(), etc.
    ########################################################################

    # Below was the original Adventurer Class code designed 

    # class Adventurer:
    #     def __init__(self, name):
    #         self.name = name
    #         self.hit_points = random.randint(75, 100)
    #         self.total_healing_potions = 0
    #         self.total_vision_potions = 0
    #         self.pillars_found = set()

    #     def __str__(self):
    #         return (
    #             f"Name: {self.name}\n"
    #             f"Hit Points: {self.hit_points}\n"
    #             f"Total Healing Potions: {self.total_healing_potions}\n"
    #             f"Total Vision Potions: {self.total_vision_potions}\n"
    #             f"Pillars Found: {', '.join(self.pillars_found)}"
    #         )

    #     def enter_room(self, room):
    #         for item in room.items:
    #             if item == 'Healing Potion':
    #                 self.pick_up_healing_potion(room)
    #             elif item == 'Vision Potion':
    #                 self.pick_up_vision_potion(room)
    #             elif item == 'Pit':
    #                 self.fall_in_pit(room)

    #     def pick_up_healing_potion(self, room):
    #         room.items.remove('Healing Potion')
    #         self.total_healing_potions += 1
    #         print(f"{self.name} picked up a Healing Potion.")

    #     def pick_up_vision_potion(self, room):
    #         room.items.remove('Vision Potion')
    #         self.total_vision_potions += 1
    #         print(f"{self.name} picked up a Vision Potion.")

    #     def fall_in_pit(self, room):
    #         room.items.remove('Pit')
    #         damage = random.randint(1, 20)
    #         self.hit_points -= damage
    #         print(f"{self.name} fell into a pit and took {damage} damage.")






D=Dungeon(4,4)


D.Set_Base_Dungeon()
print("Number of rows= ",D._num_rows)
print("Number of columns= ",D._num_columns)
print("")

D.Print_Dungeon1()

print("")

D.Create_Maze(0,0)
=======
import math
import random
from Item import Item
from Item import Healing
from Item import Vision
from Item import Pillar
from Item import Pit
from Item import Exit
from Item import ItemIterator

class Dungeon:
    class Room:
        def __init__(self):
            "Every room only contains two walls because when you pack them together, it will share the other two walls"
            "with its neighbors."
            self._northern_wall = True
            self._western_wall = True

        @property
        def coordinates(self):
            "R is the row, C is the column."
            return self.__str__()

        def __str__(self):
            "grid_x is the row, grid_y is the column.  This is the numbering system for rooms in the maze."
            return f'(R: {self._grid_x}, C: {self._grid_y})'

    class Interior_Room(Room):
        "The dungeon consists of these rooms.  These are the rooms the player can move around in."

        def __init__(self, grid_x, grid_y):
            super().__init__()
            self._dm_visited = False
            self._inventory_list = []
            self._grid_x = str(grid_x)
            "x corresponds with the row of the dungeon"
            self._grid_y = str(grid_y)
            "y corresponds with the column of the dungeon"

        def __iter__(self):
            return ItemIterator(self._inventory_list)

    def __init__(self, num_rows, num_columns):

        "When we initialize the dungeon, we pass in how big we want it to be."
        "More rows and more columns make it a bigger dungeon."
        "4x4 or 5x5 has been in the upper limit of my ability to test, but everything works."

        self._num_rooms = 0
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._Dungeon_Grid = []
        "the Dungeon Grid is a list of lists (two d array) that possesses all the rooms."

    def Set_Base_Dungeon(self):
        "Builds the grid of rooms with the entered specifications"
        for r in range(self._num_rows):
            self._Dungeon_Grid.append([])
            for c in range(self._num_columns):
                self._Dungeon_Grid[r].append(Dungeon.Interior_Room(r, c))

    def Check_Room_Contents(self,row,column):
        "This is a helper method for Print_Dungeon_Maze."
        "It will show where the dm (dungeon master) is dropping the items when he builds the maze."
        char=""
        for item in self._Dungeon_Grid[row][column]._inventory_list:
            if isinstance(item,Healing):
                char="H"
            elif isinstance(item,Vision):
                char="V"
            elif isinstance(item,Pit):
                char="T"
            elif isinstance(item,Pillar):
                char="P"
            elif isinstance(item,Exit):
                char="F"
        if len(self._Dungeon_Grid[row][column]._inventory_list)==0:
                char="O"
        return str(char)



    def Print_Dungeon1(self):
        "This method is just to help me make sure I was giving the rooms the right coordinates."
        "It prints all the rooms with the coordinates."
        for r in range(self._num_rows):
            for c in range(self._num_columns):
                print(self._Dungeon_Grid[r][c].coordinates, end=" ")
            print("")
        print("")

    def Print_Dungeon_Maze(self):
        "This method is just to help me visualize the maze.  We could show it to the player after the game is over."
        "Otherwise it has no purpose."
        "Be advised, if a room contains an item (pillar, health, vision, or pit, or exit, it will display that room"
        "with the corresponding letter."
        "P=Pillar, H=Health Potion, T=Trap (i.e. Pit), V=Vision Potion, F=Finish (i.e. Exit)"
        "If the room contains nothing it is represented by an the letter O."
        "If the room contains more than one item, it will represent the item of bigger importance, i.e. a pillar"
        "is more important than a health potion."

        "Print the Northern most boundary walls"
        for c in range(self._num_columns * 2 + 1):
            print("X", end="")
        print("")

        "Print the first row of rooms"
        for c in range(self._num_columns):
            char=self.Check_Room_Contents(0,c)
            if self._Dungeon_Grid[0][c]._western_wall == True:
                print("X", end="")
                print(char, end="")
            else:
                print(" ", end="")
                print(char, end="")
        print("X")

        "Now loop to print the middle rooms:"
        for r in range(1, self._num_rows):
            for c in range(self._num_columns):
                if self._Dungeon_Grid[r][c]._northern_wall == True:
                    print("XX", end="")
                else:
                    print("X ", end="")
            print("X")
            for c in range(self._num_columns):
                char = self.Check_Room_Contents(r, c)
                if self._Dungeon_Grid[r][c]._western_wall == True:
                    print("X", end="")
                    print(char, end="")
                else:
                    print(" ", end="")
                    print(char, end="")
            print("X")

        "Now print the Southern most boundary walls."
        for c in range(self._num_columns * 2 + 1):
            print("X", end="")
        print("")

    def Check_Travel(self, row_location, column_location):
        "This method helps me build the maze. It helps direct the Dungeon Master as he goes around knocking down walls to"
        "build the maze."
        can_travel = [False, False, False, False]
        if row_location - 1 >= 0 and self._Dungeon_Grid[row_location - 1][column_location]._dm_visited == False:
            can_travel[0] = True
        if column_location + 1 <= self._num_columns - 1 and self._Dungeon_Grid[row_location][
            column_location + 1]._dm_visited == False:
            can_travel[1] = True
        if row_location + 1 <= self._num_rows - 1 and self._Dungeon_Grid[row_location + 1][
            column_location]._dm_visited == False:
            can_travel[2] = True
        if column_location - 1 >= 0 and self._Dungeon_Grid[row_location][column_location - 1]._dm_visited == False:
            can_travel[3] = True
        return can_travel

    def Create_Maze(self, row_location, column_location):
        "This is the recursive algorithm for building the maze."

        "After we build a grid of rooms, the dm aka Dungeon master randomly walks around breaking down walls as he goes."
        "This creates the maze. He recursively calls himself every time he enters a new room.  When he enters a room"
        "where he can no longer move, i.e. he hits the boundary of a maze, and/or he has already visited the rooms"
        "around him, he stops."

        "LISTEN THIS IS VERY IMPORTANT!!!!!!!!!!!!!!!!"
        "The next line is just for testing-self.Print_Dungeon_Maze()  When we turn it in, put a # to turn it to comment."
        "Otherwise the player will have the answer."

        self.Print_Dungeon_Maze()

        self._num_rooms += 1

        self._Dungeon_Grid[row_location][column_location]._dm_visited = True

        can_travel = self.Check_Travel(row_location, column_location)

        "LISTEN THIS IS VERY IMPORTANT!!!!!!!!!!!!!!!!"
        "The next line is just for testing-print(can_travel)  When we turn it in, put a # to turn it to comment."

        print(can_travel)

        "This next batch of code will decide what items to drop into the room."
        "We will append items to the room's inventory."
        "The dm will drop a pillar after he builds a quarter of a maze, i.e. at the 1/4 2/4 3/4 etc..."
        "There is a ten percent chance he drops a health potion in every room."
        "There is a five percent chance he drops a vision potion in every room."
        "If the dm has reached the last room in the grid, he will drop an exit."
        "If the dm hits a dead end that is NOT the end of the maze, he will install a pit."

        "Drop a health potion as necessary."
        if random.random() < .1:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Healing("Healing Potion"))

        "Drop a Vision potion as necessary."
        if random.random() < .05:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Vision("Vision Potion"))

        "Drop a Pit if appropriate."
        if not True in can_travel and self._num_rooms < self._num_rows * self._num_columns:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Pit("Pit"))

        "Drop pillar as necessary."
        quarter_num_rooms = self._num_rows * self._num_columns // 4

        if self._num_rooms == quarter_num_rooms:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Pillar("Abstraction"))
        if self._num_rooms == quarter_num_rooms * 2:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Pillar("Encapsulation"))
        if self._num_rooms == quarter_num_rooms * 3:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Pillar("Abstraction"))
        if self._num_rooms == quarter_num_rooms * 4 - 2:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Pillar("Polymorphism"))

        "Drop the Exit if appropriate."
        if self._num_rooms == self._num_rows * self._num_columns:
            self._Dungeon_Grid[row_location][column_location]._inventory_list.append(Exit("Exit"))


        while True in can_travel:

            direction = random.randint(0,
                                       3)  # 0=try to go north #1=try to go east #2=try to go south #3= try to go west

            if can_travel[0] == True and direction == 0:
                self._Dungeon_Grid[row_location][column_location]._northern_wall = False
                can_travel[0] = False
                print("DM will move North!")
                print("")
                self.Create_Maze(row_location - 1, column_location)
                can_travel = self.Check_Travel(row_location, column_location)
            if can_travel[1] == True and direction == 1:
                self._Dungeon_Grid[row_location][column_location + 1]._western_wall = False
                can_travel[1] = False
                print("DM will move East!")
                print("")
                self.Create_Maze(row_location, column_location + 1)
                can_travel = self.Check_Travel(row_location, column_location)
            if can_travel[2] == True and direction == 2:
                self._Dungeon_Grid[row_location + 1][column_location]._northern_wall = False
                can_travel[2] = False
                print("DM will move South!")
                print("")
                self.Create_Maze(row_location + 1, column_location)
                can_travel = self.Check_Travel(row_location, column_location)
            if can_travel[3] == True and direction == 3:
                self._Dungeon_Grid[row_location][column_location]._western_wall = False
                can_travel[3] = False
                print("DM will move West!")
                print("")
                self.Create_Maze(row_location, column_location - 1)
                can_travel = self.Check_Travel(row_location, column_location)


D = Dungeon(5, 5)

D.Set_Base_Dungeon()
print("Number of rows= ", D._num_rows)
print("Number of columns= ", D._num_columns)
print("")

D.Print_Dungeon1()

print("")

D.Create_Maze(0, 0)
print("")
D.Print_Dungeon_Maze()
print("")
print("Number of Rooms:", D._num_rooms)
print("")
print("----------Detailed Item Inventory for each room----------")
for r in range(D._num_rows):
    for c in range(D._num_columns):
        print("")
        print(D._Dungeon_Grid[r][c].coordinates)
        for item in D._Dungeon_Grid[r][c]._inventory_list:
            print(str(item._name))
        print("Northern Wall: ",D._Dungeon_Grid[r][c]._northern_wall)
        print("Western Wall: ", D._Dungeon_Grid[r][c]._western_wall)



>>>>>>> aa42c8ba60022a4e1a7a2c1141599194a28591d2
