import pygame as pg
from Const import *


class Entity(object):    
   # Classe dos Mob

    def __init__(self):

        self.state = 0
        self.x_vel = 0
        self.y_vel = 0

        self.move_direction = True
        self.on_ground = False
        self.collision = True

        self.image = None
        self.rect = None

    def update_x_pos(self, blocks):
        self.rect.x += self.x_vel

        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):
                    if self.x_vel > 0:
                        self.rect.right = block.rect.left
                        self.x_vel = -self.x_vel
                    elif self.x_vel < 0:
                        self.rect.left = block.rect.right
                        self.x_vel = -self.x_vel

    def update_y_pos(self, blocks):
        self.rect.y += self.y_vel * FALL_MULTIPLIER

        self.on_ground = False
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):
                    if self.y_vel > 0:
                        self.on_ground = True
                        self.rect.bottom = block.rect.top
                        self.y_vel = 0

    def check_map_borders(self, core):
        if self.rect.y >= 448:
            self.die(core, True, False)
        if self.rect.x <= 1 and self.x_vel < 0:
            self.x_vel = - self.x_vel

    def die(self, core, instantly, crushed): #copiado
        if not instantly:
            core.get_map().get_player().add_score(core.get_map().score_for_killing_mob)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y)

            if crushed:
                self.crushed = True
                self.image_tick = 0
                self.current_image = 2
                self.state = -1
                core.get_sound().play('kill_mob', 0, 0.5)
                self.collision = False

            else:
                self.y_vel = -4
                self.current_image = 3
                core.get_sound().play('shot', 0, 0.5)
                self.state = -1
                self.collision = False

        else:
            core.get_map().get_mobs().remove(self)


    def render(self, core): #copiado
        core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))
