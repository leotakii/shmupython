import pygame

class Player:
    def __init__(self, image):
        self.image = image
        self.start_x = 800 // 3
        self.start_y = 600 - 100
        self.x = self.start_x
        self.y = self.start_y
        self.radius = 8
        self.speed = 5
        self.bullet_interval = 10
        self.update_rect()  # Initialize the rect
        self.power_up_level = 0
        self.bombs = 3
        self.lives = 10

    def update_rect(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        # Draw the player image centered around (self.x, self.y)
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))
        # Draw the circular hitbox for debugging
        #pygame.draw.circle(window, (245, 66, 141), (self.x+10, self.y+12), self.radius, 1)
        pygame.draw.circle(window, (245, 66, 141), (self.x + 10, self.y + 12), self.radius,
                           0)
        self.update_rect()

    def move(self, left, right, down, up):


        # Adjust movement limits based on the circular hitbox
        if left and self.x > 0:
            self.x -= self.speed
        if down and self.y < 600:
            self.y += self.speed
        if right and self.x < 800:
            self.x += self.speed
        if up and self.y > 0:
            self.y -= self.speed

        self.update_rect()  # Update rect after moving

    def is_colliding(self, other_rect):
        return self.rect.colliderect(other_rect)

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y
        self.update_rect()  # Update rect after resetting position

