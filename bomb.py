import pygame

class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.exploded = False
        self.radius = 900
        self.explosion_timer = 9


    def update(self):
        if self.explosion_timer > 0:
            self.explosion_timer -= 1
        else:
            self.exploded = True

    #def draw(self):
     #   if self.exploded:
      #      pygame.draw.circle()


