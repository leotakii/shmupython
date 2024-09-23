from enemy import Enemy

class ZigzagEnemy(Enemy):
    def __init__(self, x, y, speed, amplitude,image):
        super().__init__(image,x, y, speed)
        self.amplitude = amplitude
        self.direction = 10  # 1 for right, -1 for left
        self.offset = 0



    def update(self):
        self.rect.y += self.speed
        self.y += self.speed
        self.offset += self.direction
        self.rect.x += self.direction  # Move horizontally
        self.x += self.direction
        # Change direction when reaching the amplitude limit
        if abs(self.offset) >= self.amplitude:
            self.direction *= -1