"""
Name: Jax Jiang
PennKey: jiang13
Recitation: 201
Program Execution: python furious_fish.py [filename]
Description:
 Represents the Furious Flying Fish game. Takes a level
 description text file and initializes a game arena
 with that data, then runs the game until the player
 wins or loses.
"""

# for sys.argv
import sys
import penndraw
import arena

def main():
    # set width and height of the canvas
    penndraw.set_canvas_size(500, 500)

    # Instantiate an arena provided with the
    # name of a level description file, e.g.
    # target_file_1.txt
    the_arena = arena.Arena(sys.argv[1])

    # Our change in time between frames will be
    # set to 0.2 seconds.
    TIME_STEP = 0.2

    # While the player has neither won nor lost,
    # keep running the game.
    while (not the_arena.game_over()):
        # Update the arena and all of its components,
        # such as moving each target based on its
        # velocity and processing the player's mouse
        # input if appropriate.
        the_arena.update(TIME_STEP)

        # Draw the updated arena and its components.
        the_arena.draw()

    # When the while loop has finished, the game is
    # over. The arena will draw either a victory screen
    # or a defeat screen.
    the_arena.draw_game_complete_screen()
    penndraw.run()


if __name__ == "__main__":
    main()
