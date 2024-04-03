import game_files.object as ob

class Player(ob.Object):    
    def __init__(self, screenWidth, screenHeight) -> None:
        image = ob.pygame.image.load("./images/player-ship.png")
        imageWidth = 64
        imageHeight = 64
        image.get_rect()
        super().__init__((screenWidth // 2) - (imageWidth // 2), screenHeight - imageHeight - 10, 0, 0, image, imageWidth, imageHeight,
                         screenWidth, screenHeight)
        
        self.speedFactor = 1.2

    def update(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.screenWidth - self.imageWidth:
            self.x = self.screenWidth - self.imageWidth
        
        if self.y <= 0:
            self.y = 0
        elif self.y >= self.screenHeight - self.imageHeight:
            self.y = self.screenHeight - self.imageHeight