class Ship:
    def __init__(self, x, y, shipImage, laserImage, game) -> None:
        self.x = x
        self.y = y
        self.shipImage = shipImage
        self.laserImage = laserImage
        self.game = game

    def update(self):
        pass

    def draw(self):
        self.game.screen.blit(self.shipImage, (self.x, self.y))
