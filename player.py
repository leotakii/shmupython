import pygame

class Player:
    def __init__(self, image):
        self.image = image
        self.x = 800 // 3
        self.y = 600 - 100
        self.width = 64
        self.height = 64
        self.speed = 5
        self.bullet_interval = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, left, right, down, up):
        if left and self.x > 0:
            self.x -= self.speed
            self.rect.x -= self.speed
        if right and self.x < 800 - 35:
            self.x += self.speed
            self.rect.x += self.speed
        if down and self.y < 600 - self.height + 15:
            self.y += self.speed
            self.rect.y += self.speed
        if up and self.y < 600 + self.height and self.y > 0:
            self.y -= self.speed
            self.rect.y -= self.speed
