import pygame

class PowerUp:
    def __init__(self, x, y, image):
        self.original_image = image
        self.image = pygame.transform.scale(self.original_image,
                                            (self.original_image.get_width(), self.original_image.get_height()))
        self.speed = 2  # Speed for both upward and downward movement
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_moving_up = True  # State to determine movement direction
        self.upward_distance = 50  # Distance to move upwards
        self.moved_up = 0  # Tracks how far it has moved upward
        self.auto_loot_height = 400  # Height at which the power-up will be auto-looted
        self.is_collected = False  # Flag to check if the power-up is collected

    def update(self):
        if not self.is_collected:
            if self.is_moving_up:
                self.rect.y -= self.speed
                self.moved_up += self.speed
                if self.moved_up >= self.upward_distance:
                    self.is_moving_up = False  # Start moving down after reaching the limit
            else:
                self.rect.y += self.speed

            # Check for auto-loot condition
            #if player_height > 400:
             #   self.collect()

    def collect(self):
        self.is_collected = True
        # Implement your loot collection logic here
        print("Power-up collected!")

    def draw(self, window):
        if not self.is_collected:
            window.blit(self.image, self.rect.topleft)
