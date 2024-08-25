from circleshape import *
from constants import *

import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)

        child_astroid1_vector = self.velocity.rotate(random_angle)
        child_astroid2_vector = self.velocity.rotate(-random_angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS

        child_astroid1 = Asteroid(self.position.x,self.position.y,child_radius)
        child_astroid2 = Asteroid(self.position.x,self.position.y,child_radius)
        child_astroid1.velocity = child_astroid1_vector * 1.2
        child_astroid2.velocity = child_astroid2_vector * 1.2