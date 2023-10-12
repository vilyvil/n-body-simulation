import math
import vector2
from vector2 import Vector2
from pygame import color

class Body():
    def __init__(self, pos, radius, mass, vel=Vector2(0, 0), color=color.Color(0, 255, 0)):
        self.pos = pos
        self.radius = radius
        self.mass = mass
        self.vel = vel
        self.color = color
        self.handled = False

    # calculates next position of body according to gravitational attraction to all other bodies
    def calculate(self, bodies):
        for body in bodies:
            if body != self:
                # distance between self and body
                dist = math.pow(math.pow(self.pos.x - body.pos.x, 2) + math.pow(self.pos.y - body.pos.y, 2), 0.5)
                # ensures dist is never less than the sum of the two bodys' radiuses
                # avoids explosion of acceleration when bodies overlap
                if dist < self.radius + body.radius:
                    dist = self.radius + body.radius

                # gravity calculation
                force = (self.mass * body.mass) / (pow(dist, 2) + 0.01)
                accel = force / self.mass
                self.vel += vector2.SetMagnitude(body.pos - self.pos, accel)

        self.pos += self.vel