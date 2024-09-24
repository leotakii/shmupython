import pygame
import math

class Player:
    def __init__(self, image):
        self.image = image
        self.x = 800 // 3
        self.y = 600 - 100
        self.radius = 8
        self.speed = 5
        self.bullet_interval = 10

    def draw(self, window):
        # Draw the player image centered around (self.x, self.y)
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))
        # Draw the circular hitbox for debugging
        #pygame.draw.circle(window, (245, 66, 141), (self.x+10, self.y+12), self.radius, 1)
        pygame.draw.circle(window, (245, 66, 141), (self.x + 10, self.y + 12), self.radius,
                           0)  # Inner circle (filled with black)

    def move(self, left, right, down, up):
        # Adjust movement limits based on the circular hitbox
        if left and self.x - self.radius > 0:
            self.x -= self.speed
        if right and self.x + self.radius < 800:
            self.x += self.speed
        if down and self.y + self.radius < 600:
            self.y += self.speed
        if up and self.y - self.radius > 0:
            self.y -= self.speed

    def is_colliding(self, other_x, other_y, other_radius):
        # Calculate distance for collision detection
        distance = math.sqrt((self.x - other_x) ** 2 + (self.y - other_y) ** 2)
        return distance < (self.radius + other_radius)  # Use + for proper collision detection
