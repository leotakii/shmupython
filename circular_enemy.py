import math
from enemy import Enemy
'''
class CircularEnemy(Enemy):
    def __init__(self, center_x, center_y, radius, speed, image):
        super().__init__(image, center_x + radius, center_y, speed)
        self.center = (center_x, center_y)
        self.radius = radius
        self.angle = 0
        self.image = image
'''

class CircularEnemy(Enemy):
    def __init__(self, center_x, center_y, radius, speed, image):
        super().__init__(image, center_x + radius, center_y, speed)
        self.center = (center_x, center_y)
        self.radius = radius
        self.angle = 0  # Start at angle 0
        self.speed = speed  # Speed is in radians per update
        self.image = image

    def update(self):
        self.angle += self.speed
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi
        self.rect.x = self.center[0] + self.radius * math.cos(self.angle)
        self.rect.y = self.center[1] + self.radius * math.sin(self.angle)

    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))



