############################
# external library imports #
############################

import pygame

#########################
# local library imports #
#########################

from game_files.ship import Ship
from game_files.laser import Laser
import cfg.config as cfg

########
# code #
########

class Player(Ship):
    def __init__(self, game) -> None:
        shipImage = pygame.image.load(cfg.PLAYER_CONFIG.SHIP_IMAGE)
        laserImage = pygame.image.load(cfg.PLAYER_CONFIG.LASER_IMAGE)
        x = cfg.WINDOW_CONFIG.WIDTH // 2 - shipImage.get_width() // 2
        y = cfg.WINDOW_CONFIG.HEIGHT - shipImage.get_height() - 10
        super().__init__(x, y, shipImage, laserImage, game)

        self.shootCooldown = 0

    def move(self):
        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_a]:
            self.x -= cfg.PLAYER_CONFIG.VEL_PER_FRAME
        if pressedKeys[pygame.K_d]:
            self.x += cfg.PLAYER_CONFIG.VEL_PER_FRAME
        if pressedKeys[pygame.K_w]:
            self.y -= cfg.PLAYER_CONFIG.VEL_PER_FRAME
        if pressedKeys[pygame.K_s]:
            self.y += cfg.PLAYER_CONFIG.VEL_PER_FRAME

        # check if player is out of bounds
        if self.x + self.get_width() > cfg.WINDOW_CONFIG.WIDTH:
            self.x = cfg.WINDOW_CONFIG.WIDTH - self.get_width()
        elif self.x < 0:
            self.x = 0

        if self.y + self.get_height() > cfg.WINDOW_CONFIG.HEIGHT:
            self.y = cfg.WINDOW_CONFIG.HEIGHT - self.get_height()
        elif self.y < 0:
            self.y = 0

    def shoot(self):
        if self.shootCooldown == 0:
            pressedKeys = pygame.key.get_pressed()

            if pressedKeys[pygame.K_SPACE]:
                newLaser = Laser(self.x, self.y, self.get_width(), self.get_height(), self.laserImage, self.game, True)
                Player.bullets.append(newLaser)
                self.shootCooldown = cfg.PLAYER_CONFIG.SHOOT_COOLDOWN
        else:
            self.shootCooldown -= 1
