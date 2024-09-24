import pygame
import random

class Enemy:
    def __init__(self, image, x=0, y=0, speed=3):
        self.original_image = image
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width(), self.original_image.get_height()))
        self.x = random.randint(0, 800 - self.image.get_width())
        self.y = random.randint(-20, 20)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = min(self.width,self.height) // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        self.y += self.speed




    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
