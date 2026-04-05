"""
Name: Jax Jiang
PennKey: jiang13
Recitation: 201
Program Execution: N/A, this class is meant to be used by other classes
Description:
 A class that represents a Target to be hit in
 Furious Flying Fish. Can update its own position based
 on velocity and time.
"""

import penndraw as pd

class Target:
    def __init__(self, scale, x_pos, y_pos, radius, x_vel, y_vel, hit_points):
        """
        Given the scale, a position, a radius, a velocity, and a number of
        hit points, construct a Target.
        """

        # the scale used by the penndraw canvas
        self.scale = scale

        # Position and radius
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius

        # Velocity Components
        self.x_vel = x_vel
        self.y_vel = y_vel

        # When a Target's hit points reach zero,
        # it has been destroyed by the fish
        self.hit_points = hit_points

        # Track if the Target has been hit this shot
        self.hit_this_shot = False

    def draw(self):
        """
        Draw a circle centered at the Target's position
        with a radius equal to the Target's radius.
        Only draw a Target if it has more than zero
        hit points.
        """
        pd.set_pen_color(pd.RED)
        if self.hit_points > 0:
            pd.filled_circle(self.x_pos, self.y_pos, self.radius)
            pd.set_pen_color(pd.WHITE)
            pd.filled_circle(self.x_pos, self.y_pos, self.radius * 0.66)
            pd.set_pen_color(pd.RED)
            pd.filled_circle(self.x_pos, self.y_pos, self.radius * 0.33)
            pd.set_pen_color(pd.BLACK)
            pd.text(self.x_pos, self.y_pos, str(self.hit_points))

            if self.hit_points == 2:
                pd.line(
                    self.x_pos - self.radius / 2,
                    self.y_pos - self.radius / 2,
                    self.x_pos + self.radius / 2,
                    self.y_pos + self.radius / 2
                )
            elif self.hit_points == 1:
                pd.line(
                    self.x_pos - self.radius / 2,
                    self.y_pos - self.radius / 2,
                    self.x_pos + self.radius / 2,
                    self.y_pos + self.radius / 2
                )
                pd.line(
                    self.x_pos - self.radius / 2,
                    self.y_pos + self.radius / 2,
                    self.x_pos + self.radius / 2,
                    self.y_pos - self.radius / 2
                )

    def update(self, time_step):
        """
        Given the change in time, update the Target's
        position based on its x and y velocity. When
        a Target is completely offscreen horizontally,
        its position should wrap back around to the opposite
        horizontal side. For example, if the Target moves off the
        right side of the screen, its x_pos should be set to the
        left side of the screen minus the Target's radius.
        The same logic should apply to the Target's vertical
        position with respect to the vertical screen boundaries.
        """
        self.x_pos += self.x_vel * time_step
        self.y_pos += self.y_vel * time_step

        # is x off screen?
        if self.x_pos - self.radius > self.scale:
            self.x_pos = -self.radius
        elif self.x_pos + self.radius < 0:
            self.x_pos = self.scale + self.radius

        # is y off screen?
        if self.y_pos - self.radius > self.scale:
            self.y_pos = -self.radius
        elif self.y_pos + self.radius < 0:
            self.y_pos = self.scale + self.radius

    def decrease_hp(self):
        """Decrement the Target's hit points by 1."""
        self.hit_points -= 1
