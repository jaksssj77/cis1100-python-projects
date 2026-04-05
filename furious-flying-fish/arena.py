"""
Name: Jax Jiang
PennKey: jiang13
Recitation: 201
Program Execution: N/A, this class is meant to be used by other classes
Description:
 A class representing the Arena in which the Furious Flying Fish
 game takes place. Keeps track of the game's Fish and
 Targets and receives the player's input to control the Fish.
"""

import penndraw as pd
from fish import Fish
from target import Target

class Arena:
    def __init__(self, filename):
        """
        Given a file that describes the contents of the
        Arena, parse the file and initialize all member
        variables of the Arena.

        Remember to set mouse_listening_mode to true to start.
        """
        input_file = open(filename, "r")
        first_line = input_file.readline().split()
        num_targets = int(first_line[0])

        # The scale we will use for the screen.
        # So instead of all coordinates being in the range of [0, 1] for
        # both x and y, instead they will be in the range of [0, scale]
        self.scale = float(first_line[1])
        # set scale used by penndraw
        pd.set_scale(0, self.scale)

        # list of Targets in the Arena
        self.targets = []

        num_throws = int(input_file.readline().strip())
        # The one and only Fish in this game
        self.nemo = Fish(1, 1, 0.25, num_throws)

        for _ in range(num_targets):
            line = input_file.readline().split()

            x_pos = float(line[0])
            y_pos = float(line[1])
            radius = float(line[2])
            x_vel = float(line[3])
            y_vel = float(line[4])
            hit_points = int(line[5])

            self.targets.append(
                Target(
                    self.scale, x_pos, y_pos, radius, x_vel, y_vel, hit_points
                )
            )

        input_file.close()

        # Whether the game is currently listening for
        # the player's mouse input, or letting the Fish
        # fly. Begins as true.
        self.mouse_listening_mode = True
        self.mouse_was_pressed_last_update = False

    def draw(self):
        """
        1. Clear the screen
        2. Draw each Target
        3. Draw the Fish
        4. If in mouse listening mode and
        the mouse was pressed last update,
        draw the Fish's velocity as a line.
        5. Advance penndraw.
        """
        pd.clear()

        for t in self.targets:
            t.draw()

        self.nemo.draw()

        if self.mouse_listening_mode and self.mouse_was_pressed_last_update:
            self.nemo.draw_velocity()

        pd.advance()

    def did_player_win(self):
        """
        Returns true when all Targets' hit points are 0.
        Returns false in any other scenario.
        """
        return len(self.targets) == 0

    def did_player_lose(self):
        """
        Returns true when the Fish's remaining throw count is 0
        when the game is in mouse-listening mode.
        Returns false in any other scenario.
        """
        return self.mouse_listening_mode and self.nemo.num_throws == 0

    def game_over(self):
        """
        Returns true when either the win or lose
        condition is fulfilled.
        Win: All Targets' hit points are 0.
        Lose: The Fish's remaining throw count reaches 0.
        Additionally, the game must be in mouse listening
        mode for the player to have lost so that the Fish
        can finish its final flight and potentially hit
        the last Target(s).
        """
        return self.did_player_win() or self.did_player_lose()

    def update(self, time_step):
        """
        Update each of the entities within the Arena.
        1. Call each Target's update function
        2. Check the game state (mouse listening or Fish moving)
        and invoke the appropriate functions for the Fish.
        """
        for t in self.targets:
            t.update(time_step)

        if (self.mouse_listening_mode):

            # If the mouse is currently pressed, then
            # set mouse_was_pressed_last_update to true, and
            # call nemo.set_velocity_from_mouse_pos().
            if pd.mouse_pressed():
                self.mouse_was_pressed_last_update = True
                self.nemo.set_velocity_from_mouse_pos()
            elif self.mouse_was_pressed_last_update:
                self.mouse_was_pressed_last_update = False
                self.mouse_listening_mode = False
                self.nemo.decrement_throws()

        else:
            self.nemo.update(time_step)

            for t in self.targets:
                self.nemo.test_and_handle_collision(t)

            if self.fish_is_off_screen():
                for t in self.targets:
                    if t.hit_this_shot:
                        t.decrease_hp()
                        t.hit_this_shot = False

                self.targets = [t for t in self.targets if t.hit_points > 0]

                self.nemo.reset()
                self.mouse_listening_mode = True

    def fish_is_off_screen(self):
        """
        A helper function for the Arena class that lets
        it know when to reset the Fish's position and velocity
        along with the game state.
        Returns true when the Fish is offscreen to the left, right,
        or bottom. However, the Fish is allowed to go above the top
        of the screen without resetting.
        """
        # is fish below the screen bottom?
        below_screen = self.nemo.y_pos + self.nemo.radius < 0

        # is fish beyond the left side of the screen?
        beyond_left = self.nemo.x_pos + self.nemo.radius < 0

        # is fish beyond the right side of the screen?
        beyond_right = self.nemo.x_pos - self.nemo.radius > self.scale

        return below_screen or beyond_right or beyond_left

    def draw_game_complete_screen(self):
        """
        Draws either the victory or loss screen.
        If all Targets have 0 hit points, the player has won.
        Otherwise they have lost.
        """
        pd.clear()

        if self.did_player_win():
            pd.text(self.scale / 2, self.scale / 2, "You Win!")
        elif self.did_player_lose():
            pd.text(self.scale / 2, self.scale / 2, "You have lost...")

        pd.advance()
