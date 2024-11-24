from abc import ABC, abstractmethod
import time
from ipycanvas import hold_canvas

class Particle:
    def __init__(self, x, y, vx, vy, radius=5, mass=1, color="#9e823f"):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass
        self.color = color

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, canvas):
        canvas.fill_style = self.color
        canvas.fill_circle(self.x, self.y, self.radius)


class NParticlesSystem(ABC):
    def __init__(self, particles, background_color="#f0f0f0"):
        self.particles = particles
        self.background_color = background_color

    @abstractmethod
    def evolve(self, dt):
        pass

    def draw(self, canvas):
        with hold_canvas(canvas):
            canvas.clear()

            canvas.fill_style = self.background_color
            canvas.fill_rect(0, 0, canvas.width, canvas.height)

            for particle in self.particles:
                particle.draw(canvas)

    def update(self, dt, canvas):
        self.evolve(dt)
        self.draw(canvas)
        time.sleep(1/60)
