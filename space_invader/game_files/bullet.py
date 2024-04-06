import game_files.object as ob

class Bullet(ob.Object):

    def __init__(self, spaceshipXpos, spaceShipYpos, objectSpeed, screenWidth, screenHeight) -> None:
        image = ob.pygame.image.load("./images/bullet.png")
        imageWidth = 10
        imageHeight = 32
        self.speedFactor = -3
        super().__init__(spaceshipXpos + 32 - (imageWidth // 2), spaceShipYpos + (imageHeight // 2), 0, objectSpeed*self.speedFactor, 
                         image, imageWidth, imageHeight, screenWidth, screenHeight)
    
    def update(self):
        self.y += self.ySpeed