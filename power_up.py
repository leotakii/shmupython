import pygame

class PowerUp:
    def __init__(self, x, y):
        self.image = pygame.Surface((20, 20))  # Create a simple square for the power-up
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2  # Speed at which the power-up will fall

    def update(self):
        self.rect.y += self.speed

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)
