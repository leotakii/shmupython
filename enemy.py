import pygame
import random

class Enemy:
    def __init__(self, image, x=0, y=0, speed=3):
        self.scale_factor = 0.5
        self.original_image = image
        new_width = int(self.original_image.get_width() * self.scale_factor)
        new_height = int(self.original_image.get_height() * self.scale_factor)
        self.image = pygame.transform.scale(self.original_image, (new_width,new_height))
        self.x = random.randint(0, 800 - self.image.get_width())
        self.y = random.randint(-20, 20)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = min(self.width,self.height) // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = speed
        self.cooldown = 0
        self.shoot_interval = 60
        self.health = 3

    def update(self):
        self.rect.y += self.speed
        self.y += self.speed
        self.cooldown -= 1



    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
