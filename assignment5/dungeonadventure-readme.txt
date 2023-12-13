How the game is played

1. Start the Game:

    - Run the script to initialize the DungeonAdventure class.
    - Enter the name of your adventurer when prompted.

2. Explore the Dungeon:

    - The initial dungeon state is displayed.
    - You start in the room at coordinates (0, 0), as indicated by "Current Room: (R: 0, C: 0)."

3. Review Options:

    Options are presented:
       1. Move
       2. Use Healing Potion
       3. Use Vision Potion
       4. Show Dungeon (hidden option)

4. Choose an Option:

   - Enter the number corresponding to your choice (1-4).

5. If Choosing to Move:

    - Enter the direction to move ("north", "east", "south", "west").
    - The game will check if the move is valid and execute it if possible.
    - The updated room coordinates will be displayed.

6. If Choosing to Use Potions:

    - The game will use healing or vision potions if available, and your status will be displayed.

7. If Choosing to Show Dungeon:

    - The hidden option to print the dungeon will display the entire dungeon state.

8. Continue Exploring:

    - Repeat steps 3-7 to navigate through the dungeon, pick up items, and overcome challenges.
    - The game will provide feedback on your progress, such as finding pillars or reaching an exit.

9. Game Over or Victory:

    - The game will end if your adventurer's health reaches zero, resulting in a "Game Over" message.
    - If you collect all four pillars and reach an exit, you win the game.

10. Final Dungeon State:

    - The script will display the entire dungeon at the conclusion of the game.


Current limitation:

1. the move doesn't work properly, I am checking for updates per the check_travel method to see if I missed anything

The other options(2-4) on step 3 work correctly.