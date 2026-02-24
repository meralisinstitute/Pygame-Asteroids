import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent constructor to initialize the sprite correctly
        super().__init__(x, y, radius)

    def draw(self, screen):
     
        pygame.draw.circle(
            screen, 
            "white", 
            (int(self.position.x), int(self.position.y)), 
            self.radius, 
            LINE_WIDTH
        )

    def update(self, dt):
       
        self.position += self.velocity * dt  # Move asteroid based on velocity

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2