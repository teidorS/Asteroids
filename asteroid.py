from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius);
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt;

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        new_vec_1 = self.velocity.rotate(split_angle)
        new_vec_2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        split_asteroid_1.velocity = new_vec_1 * 1.2
        split_asteroid_2.velocity = new_vec_2 * 1.2
