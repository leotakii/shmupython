import random
from enemy import Enemy

class RandomEnemy(Enemy):
    def __init__(self, x, y, speed, image):
        super().__init__(image, x, y, speed)
        self.direction = random.choice([-1, 1])

    def update(self):
        if random.randint(0, 50) < 10:
            self.direction *= -1
        new_x = self.rect.x + self.direction * (self.speed ** 2)
        if new_x < 0 or new_x > 800:
            new_x = self.rect.x
        self.rect.x = new_x
        self.x = new_x
