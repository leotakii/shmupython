import pygame
import random
import math
from player import Player
from enemy import Enemy
from bullet import Bullet
from circular_enemy import CircularEnemy
from zigzag_enemy import ZigzagEnemy
from random_enemy import RandomEnemy
from chasing_enemy import ChasingEnemy
from power_up import PowerUp

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)

# Load images (make sure the path is correct)
player_img = pygame.image.load('C:/Users/Lenovo/PycharmProjects/navinha/Lib/sprites/reimu_sprite.png')
enemy_img = pygame.image.load('C:/Users/Lenovo/PycharmProjects/navinha/Lib/sprites/cirno_fumo.png')
bullet_img = pygame.image.load('C:/Users/Lenovo/PycharmProjects/navinha/Lib/sprites/bullet.png')


def check_collisions(bullets, enemies,power_ups):
    for bullet in bullets:
        for enemy in enemies:

            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                power_ups.append(PowerUp(enemy.rect.x,enemy.rect.y))
                break

def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(player_img)
    enemies = []
    bullets = []
    power_ups = []

    cooldown = player.bullet_interval
    while run:
        clock.tick(60)
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player.move(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_DOWN], keys[pygame.K_UP])
        check_collisions(bullets, enemies,power_ups)

        if keys[pygame.K_z] and len(bullets) < 200 and cooldown >= player.bullet_interval:
            # Calculate bullet positions
            left_bullet_x = player.x - 10
            left_bullet_y = player.y
            right_bullet_x = player.x + 10
            right_bullet_y = player.y

            # Initialize extra bullet positions
            extra_left_bullet_x = player.x - 40
            extra_left_bullet_y = player.y + 30
            extra_right_bullet_x = player.x + 40
            extra_right_bullet_y = player.y + 30

            # Always add the left bullet
            bullets.append(Bullet(left_bullet_x, left_bullet_y, bullet_img))

            if player.power_up_level < 50:
                # If power up level is less than 50, shoot only the left bullet
                pass  # Already added the left bullet
            elif player.power_up_level < 150:
                # If power up level is between 50 and 150, add the right bullet
                bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))
            elif player.power_up_level < 200:
                # If power up level is between 150 and 200, add an extra bullet on the left
                bullets.append(Bullet(extra_left_bullet_x, extra_left_bullet_y, bullet_img))
                bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))  # Add right bullet
            else:
                # If power up level is 200 or more, add an extra bullet on the right
                bullets.append(Bullet(extra_left_bullet_x, extra_left_bullet_y, bullet_img))  # Extra left bullet
                bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))  # Regular right bullet
                bullets.append(Bullet(extra_right_bullet_x, extra_right_bullet_y, bullet_img))  # Extra right bullet

            cooldown = 5  # Reset cooldown

            cooldown = 5  # Reset cooldown

            # Create bullets
            #bullets.append(Bullet(left_bullet_x, left_bullet_y, bullet_img))
            #bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))

            cooldown = 5

        if keys[pygame.K_c]:
            player.speed = 3
            player.bullet_interval = 10
        else:
            player.speed = 5
            player.bullet_interval = 10

        for bullet in bullets[:]:
            bullet.move()
            pygame.draw.rect(window, (255, 0, 0), bullet.rect, 2)  # Red for bullets
            if bullet.y < 0:
                bullets.remove(bullet)
            bullet.draw(window)
        # Update power-ups
        for power_up in power_ups[:]:
            power_up.update()
            if player.is_colliding(power_up.rect):
                player.power_up_level += 10  # Increase the power-up level
                power_ups.remove(power_up)  # Remove the power-up once collected
                if player.power_up_level == 150:
                    player.power_up_level = 150
            elif power_up.rect.y > HEIGHT:  # Remove if it falls off screen
                power_ups.remove(power_up)
            power_up.draw(window)



        player.draw(window)

        if len(enemies) == 0:#Respawning enemies
            enemy_wave_type = random.randint(0, 4)
            number_enemies = random.randint(1,3)
            center_x = WIDTH // 2
            center_y = HEIGHT // 2
            radius = WIDTH / 4

            enemies = []
            #oscillation_amplitude = 20
            if enemy_wave_type == 0:
                enemies = []
                for _ in range(number_enemies):
                    # Random angle
                    angle = random.uniform(0, 2 * math.pi)
                    # Calculate random x and y based on the angle and radius
                    spawn_x = center_x + radius * math.cos(angle)
                    spawn_y = center_y + radius * math.sin(angle)
                    enemies.append(CircularEnemy(spawn_x, spawn_y, radius, 0.09, enemy_img))
            elif enemy_wave_type == 1:
                enemies = [Enemy(enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 2:
                enemies = [RandomEnemy(0, 0, 3, enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 3:
                enemies = [ZigzagEnemy(0, 0, 3, 100,enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 4:
                enemies = [ChasingEnemy(0, 0, 3,enemy_img) for _ in range(number_enemies)]
        for enemy in enemies:
            if player.is_colliding(enemy.rect):
                player.reset_position()
                enemies.remove(enemy)
                break

            if isinstance(enemy, ChasingEnemy):
                enemy.update(player.x,player.y,player.radius)
            else:
                enemy.update()
            if enemy.y >= 800:
                enemies.remove(enemy)
                continue
            enemy.draw(window)
            pygame.draw.rect(window, (0, 255, 0), enemy.rect, 2)  # Green for Enemies

        pygame.display.flip()
        cooldown += 1

    pygame.quit()

if __name__ == "__main__":
    main()
