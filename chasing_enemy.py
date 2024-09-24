from enemy import Enemy
import math
class ChasingEnemy(Enemy):
    def __init__(self, x, y, speed, image):
        super().__init__(image, x, y, speed)  # Call the parent class constructor

    def update(self, player_x, player_y, player_radius):
        # Move towards the player's position
        # Calculate the distance to the player
        distance_x = player_x - self.rect.centerx
        distance_y = player_y - self.rect.centery
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        # Normalize and move towards the player if not too close
        if distance > player_radius:  # Optional: stop chasing if within player radius
            if distance > 0:  # Avoid division by zero
                self.rect.x += (distance_x / distance) * self.speed
                self.rect.y += (distance_y / distance) * self.speed

    def draw(self, window):
        # Draw the enemy at the current rect position
        window.blit(self.image, self.rect.topleft)  # Use rect.topleft for the position
