############################
# external library imports #
############################

#########################
# local library imports #
#########################

from game_files.activeObject import ActiveObject

########
# code #
########

class Ship(ActiveObject):
    def __init__(self, x, y, shipImage, laserImage, game, hp) -> None:
        super().__init__(x, y, shipImage, game)
        self.laserImage = laserImage
        self.hp = hp

    def is_destroyed(self):
        return self.hp <= 0

    def hit(self, damage):
        self.hp -= damage

    def move(self):
        pass

    def shoot(self):
        pass

    def actions(self):
        self.move()
        self.shoot()
        super().actions()
