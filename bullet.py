import pygame

class Bullet:
    def __init__(self, x, y, image):
        self.original_image = image
        self.x = x
        self.y = y-30
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() / 2, self.original_image.get_height() / 2))
        self.speed = 7
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.speed
        self.rect.y -= self.speed
