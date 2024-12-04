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
from bomb import Bomb

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)

# Load images (make sure the path is correct)
player_img = pygame.image.load('sprites/reimu_sprite.png')
enemy_img = pygame.image.load('sprites/cirno_fumo.png')
bullet_img = pygame.image.load('sprites/bullet.png')
power_up_img = pygame.image.load('sprites/power_up.png')


def check_collisions(bullets, enemies, power_ups):
    for bullet in bullets[:]:  # Iterate a copy of the list
        for enemy in enemies[:]:  # Iterate a copy of the list
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemy.health -= 1
                if enemy.health <= 0:
                    enemies.remove(enemy)
                    power_ups.append(PowerUp(enemy.rect.x, enemy.rect.y, power_up_img))
                break




def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(player_img)
    enemies = []
    bullets = []
    power_ups = []
    bombs = []
    bomb_used = False
    player.power_up_level = 50

    cooldown = player.bullet_interval
    while run:
        print(player.power_up_level)
        clock.tick(60)
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()  # Get the state of all keys
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        down = keys[pygame.K_s]
        up = keys[pygame.K_w]

        player.move(left, right, down, up)  # Move player based on key states

        check_collisions(bullets, enemies, power_ups)

        if keys[pygame.K_h] and player.bombs > 0 and not bomb_used:
            bombs.append(Bomb(player.x, player.y))
            player.bombs -= 1
            bomb_used = True
        if not keys[pygame.K_h]:
            bomb_used = False

        for bomb in bombs[:]:
            bomb.update()
            if bomb.exploded:
                # Kill all enemies within the explosion radius
                enemies[:] = [enemy for enemy in enemies if not (
                    math.sqrt((enemy.rect.x - bomb.x) ** 2 + (enemy.rect.y - bomb.y) ** 2) < bomb.radius)]
                bombs.remove(bomb)

        if keys[pygame.K_g] and len(bullets) < 200 and cooldown >= player.bullet_interval:
            left_bullet_x = player.x - 10
            left_bullet_y = player.y
            right_bullet_x = player.x + 10
            right_bullet_y = player.y

            extra_left_bullet_x = player.x - 40
            extra_left_bullet_y = player.y + 30
            extra_right_bullet_x = player.x + 40
            extra_right_bullet_y = player.y + 30

            bullets.append(Bullet(left_bullet_x, left_bullet_y, bullet_img))

            if player.power_up_level < 50:
                pass  # Already added the left bullet
            elif player.power_up_level < 150:
                bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))
            elif player.power_up_level < 200:
                bullets.append(Bullet(extra_left_bullet_x, extra_left_bullet_y, bullet_img))
                bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))
            else:
                bullets.append(Bullet(extra_left_bullet_x, extra_left_bullet_y, bullet_img))
                bullets.append(Bullet(right_bullet_x, right_bullet_y, bullet_img))
                bullets.append(Bullet(extra_right_bullet_x, extra_right_bullet_y, bullet_img))

            cooldown = 0  # Reset cooldown

        # Speed control
        player.speed = 3 if keys[pygame.K_k] else 5

        for bullet in bullets[:]:
            bullet.move()
            pygame.draw.rect(window, (255, 0, 0), bullet.rect, 2)  # Red for bullets
            if bullet.rect.y < 0:
                bullets.remove(bullet)
            bullet.draw(window)

        # Update power-ups
        for power_up in power_ups[:]:
            power_up.update()
            if player.is_colliding(power_up.rect):
                player.power_up_level += 10
                power_ups.remove(power_up)
            elif power_up.rect.y > HEIGHT:
                power_ups.remove(power_up)
            power_up.draw(window)

        player.draw(window)

        if not enemies:  # Respawning enemies
            enemy_wave_type = random.randint(0, 4)
            number_enemies = random.randint(1, 3)
            center_x = WIDTH // 2
            center_y = HEIGHT // 2
            radius = WIDTH / 4

            if enemy_wave_type == 0:
                for _ in range(number_enemies):
                    angle = random.uniform(0, 2 * math.pi)
                    spawn_x = center_x + radius * math.cos(angle)
                    spawn_y = center_y + radius * math.sin(angle)
                    enemies.append(CircularEnemy(spawn_x, spawn_y, radius, 0.09, enemy_img))
            elif enemy_wave_type == 1:
                enemies.extend([Enemy(enemy_img) for _ in range(number_enemies)])
            elif enemy_wave_type == 2:
                enemies.extend([RandomEnemy(0, 0, 3, enemy_img) for _ in range(number_enemies)])
            elif enemy_wave_type == 3:
                enemies.extend([ZigzagEnemy(0, 0, 3, 100, enemy_img) for _ in range(number_enemies)])
            elif enemy_wave_type == 4:
                enemies.extend([ChasingEnemy(0, 0, 3, enemy_img) for _ in range(number_enemies)])

        for enemy in enemies[:]:
            if player.is_colliding(enemy.rect):
                player.reset_position()
                enemies.remove(enemy)
                #Remove an upgrade level
                if player.power_up_level - 25 <= 0:
                    player.power_up_level = 0
                else:
                    player.power_up_level -= 25
                player.lives -= 1
                if player.lives == 0:
                    run = False
                continue


            if isinstance(enemy, ChasingEnemy):
                enemy.update(player.x, player.y, player.radius)
            else:
                enemy.update()

            if enemy.rect.y >= HEIGHT:  # Ensure proper boundary check
                enemies.remove(enemy)
                continue
            enemy.draw(window)
            pygame.draw.rect(window, (0, 255, 0), enemy.rect, 2)  # Green for Enemies

        pygame.display.flip()
        cooldown += 1

    pygame.quit()


if __name__ == "__main__":
    main()
