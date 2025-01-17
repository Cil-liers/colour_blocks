# This is a class that represents one of my falling blocks as sprites.
# Benjamin Cilliers
# 2025/01/13

import pygame
import random

class Block(pygame.sprite.Sprite):
    
    def __init__(self, position):

        pygame.sprite.Sprite.__init__(self)
        # self.colour = (128,128,128)
        self.colour = self.new_color()
        self.size = (20,20)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.time = 0
        self.moving = True
        # self.blocks_above = []
        self.blocks_below = []


    def update(self):
        self.travel()
        if self.time == 600:
            # if self.block_above is not None:
            #     self.block_above.block_below = None
            self.kill()
        else:
            self.time += 1


    def travel(self):
        (x_val,y_val) = self.rect.center
        if y_val < 590 and self.moving:
            self.rect.center = (x_val,y_val+3)
        elif self.moving:
            self.rect.center = (x_val,590)
            self.moving = False


    def new_color(self):
        num_1 = random.randint(0,255)
        num_2 = random.randint(0,255)
        num_3 = random.randint(0,255)
        return (num_1, num_2, num_3)
