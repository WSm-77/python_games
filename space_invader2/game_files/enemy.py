############################
# external library imports #
############################

#########################
# local library imports #
#########################

from random import randint
from game_files.laser import Laser
from game_files.ship import Ship
import cfg.config as cfg

########
# code #
########

class Enemy(Ship):
    bullets = []
    def __init__(self, x, y, shipImage, laserImage, game) -> None:
        super().__init__(x, y, shipImage, laserImage, game)

    def move(self):
        self.y += cfg.ENEMY_CONFIG.VEL_PER_FRAME

    def shoot(self):
        if randint(1, cfg.ENEMY_CONFIG.SHOOTING_CHANCE) == 1:
            newLaser = Laser(self.x, self.y, self.get_width(), self.get_height(), self.laserImage, self.game, False)
            Enemy.bullets.append(newLaser)
