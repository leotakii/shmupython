from enemy import Enemy


class ChasingEnemy(Enemy):
    def __init__(self, x, y, speed, image):
        super().__init__(image, x, y, speed)  # Pass image, x, y, speed

    def update(self, player_rect):
        # Move towards the player's position
        if self.rect.x < player_rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player_rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player_rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player_rect.y:
            self.rect.y -= self.speed

    def draw(self, window):
        # Draw the enemy at the current rect position
        window.blit(self.image, self.rect.topleft)  # Use rect.topleft for the position
