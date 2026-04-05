"""
Name: Jax Jiang
PennKey: jiang13
Recitation: 201
Program Execution: N/A, this class is meant to be used by other classes
Description:
 A class that represents the fish projectile in
 Furious Flying Fish. Can update its own position based
 on velocity and time, and can compute whether
 it overlaps a given Target.
"""

import penndraw as pd

class Fish:
    def __init__(self, x_pos, y_pos, radius, num_throws):
        """
        Initialize the fish's member variables
        with the same names as the inputs to those values.
        Initializes the fish's velocity components to 0.
        """

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = 0
        self.y_vel = 0
        self.radius = radius
        self.num_throws = num_throws

    def draw(self):
        """
        Draws a Circle centered at the fish's position
        with a radius equal to the fish's radius.
        Additionally, draws a triangular fin and a
        circular eye somewhere on the circle to make
        the fish look more like a fish. Additional details
        are up to your discretion.
        Also draws the fish's remaining throws 0.1 units
        above its circular body.
        """
        # set pen color
        pd.set_pen_color(173, 216, 230)

        # draw body
        pd.filled_circle(self.x_pos, self.y_pos, self.radius)

        # draw tail
        pd.filled_polygon(
            self.x_pos - self.radius, self.y_pos,
            self.x_pos - 2 * self.radius, self.y_pos + self.radius,
            self.x_pos - 2 * self.radius, self.y_pos - self.radius
        )

        # draw eye
        pd.set_pen_color(pd.BLACK)
        pd.filled_circle(
            self.x_pos + self.radius / 3,
            self.y_pos + self.radius / 3,
            self.radius / 6
        )

        # show remaining throws
        pd.text(
            self.x_pos,
            self.y_pos + self.radius + 0.1,
            str(self.num_throws)
        )

    def draw_velocity(self):
        """
        Draw the line representing the fish's initial velocity
        when the player is clicking and dragging the mouse.
        """
        pd.line(
            self.x_pos,
            self.y_pos,
            self.x_pos + self.x_vel,
            self.y_pos + self.y_vel
        )

    def reset(self):
        """
        Set x_pos and y_pos to 1.0,
        set x_vel and y_vel to 0.0.
        """
        self.x_pos = 1.0
        self.y_pos = 1.0
        self.x_vel = 0.0
        self.y_vel = 0.0

    def set_velocity_from_mouse_pos(self):
        """
        Compute the fish's initial velocity as the
        vector from the mouse's current position to
        the fish's current position. This will be used
        in mouse listening mode to update the launch
        velocity.
        """
        self.x_vel = self.x_pos - pd.mouse_x()
        self.y_vel = self.y_pos - pd.mouse_y()

    def update(self, time_step):
        """
        Given the change in time, compute the fish's
        new position and new velocity.
        """
        # update x and y coordinates
        self.x_pos += self.x_vel * time_step
        self.y_pos += self.y_vel * time_step

        # update y_vel
        self.y_vel -= 0.25 * time_step

    def distance(self, x1, y1, x2, y2):
        """
        A helper function used to find the distance
        between two 2D points. Remember to use the
        Pythagorean Theorem.
        """
        return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

    def test_and_handle_collision(self, target):
        """
        Given a target, determine if the fish should
        test for collision against it. If the fish
        *should* see if it collides with the target,
        then perform that test. If the fish collides,
        then decrease the target's HP by 1 set its
        hit_this_shot field to be true.
        """
        if target.hit_points > 0 and not target.hit_this_shot:
            dx = self.x_pos - target.x_pos
            dy = self.y_pos - target.y_pos
            dist = self.distance(
                self.x_pos, self.y_pos,
                target.x_pos, target.y_pos
            )

            if dist < self.radius + target.radius:
                target.hit_this_shot = True

                if abs(dx) > abs(dy):
                    self.x_vel *= -1
                else:
                    self.y_vel *= -1

    def decrement_throws(self):
        """
        reduce the num_throws for this fish by 1.
        """
        self.num_throws -= 1
