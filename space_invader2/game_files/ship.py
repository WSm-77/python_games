############################
# external library imports #
############################

#########################
# local library imports #
#########################

from game_files.activeObject import ActiveObject
from game_files.healthBar import HealthBar

########
# code #
########

class Ship(ActiveObject):
    def __init__(self, x, y, shipImage, laserImage, game, hp, showHealthBar) -> None:
        super().__init__(x, y, shipImage, game)
        self.laserImage = laserImage
        self.healthBar = HealthBar(hp, self, game, showHealthBar)

    def hp(self):
        return self.healthBar.currentHp

    def is_destroyed(self):
        return self.hp() <= 0

    def hit(self, damage):
        self.healthBar.loose_hp(damage)

    def move(self):
        pass

    def shoot(self):
        pass

    def draw(self):
        super().draw()
        self.healthBar.draw()

    def actions(self):
        self.move()
        self.healthBar.update()
        self.shoot()
        super().actions()
