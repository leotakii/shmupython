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


def check_collisions(bullets, enemies):
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(player_img)
    #enemies = [Enemy(enemy_img) for _ in range(5)]
    enemies = []
    bullets = []

    cooldown = player.bullet_interval
    while run:
        clock.tick(60)
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player.move(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_DOWN], keys[pygame.K_UP])

        check_collisions(bullets, enemies)

        if keys[pygame.K_z] and len(bullets) < 40 and cooldown >= player.bullet_interval:
            bullets.append(Bullet(player.x, player.y, bullet_img))
            cooldown = 0
        if keys[pygame.K_c]:
            player.speed = 3
            player.bullet_interval = 5
        else:
            player.speed = 5
            player.bullet_interval = 10

        for bullet in bullets[:]:
            bullet.move()
            pygame.draw.rect(window, (255, 0, 0), bullet.rect, 2)  # Red for bullets
            if bullet.y < 0:
                bullets.remove(bullet)
            bullet.draw(window)

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
                    #enemies.append(CircularEnemy(spawn_x,spawn_y,radius,0.09, enemy_img,oscillation_amplitude))
                    enemies.append(CircularEnemy(spawn_x, spawn_y, radius, 0.09, enemy_img))
            elif enemy_wave_type == 1:
                enemies = [Enemy(enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 2:
                enemies = [RandomEnemy(0, 0, 3, enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 3:
                enemies = [ZigzagEnemy(0, 0, 3, 100,enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 4:
                enemies = [ChasingEnemy(0, 0, 3,enemy_img) for _ in range(number_enemies)]


            '''
            if enemy_wave_type == 0:
                enemies = [RandomEnemy(0, 0, 3, enemy_img) for _ in range(number_enemies)]
            
            elif enemy_wave_type == 1:
                enemies = [ChasingEnemy(0, 0, 3, enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 2:
                enemies = [Enemy(0, 0, 3, enemy_img) for _ in range(number_enemies)]
            elif enemy_wave_type == 3:
                enemies = [ZigzagEnemy(0, 0, 3, 100, enemy_img) for _ in range(number_enemies)]
            '''

        for enemy in enemies:
            #enemy.update(player.rect)
            if isinstance(enemy, ChasingEnemy):
                enemy.update(player.rect)
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
