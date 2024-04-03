import game_files.object as ob
from random import randint

class Enemy(ob.Object):
    def __init__(self, screenWidth, screenHeight, objectSpeed) -> None:
        image = ob.pygame.image.load("./images/alien.png")
        imageWidth = 64
        imageHeight = 64
        super().__init__(randint(0, screenWidth - (imageWidth // 2)), 0, objectSpeed * self.speedFactor, 0, image, imageWidth,
                         imageHeight, screenWidth, screenHeight)
        
    # def update(self) -> bool:
    def update(self):
        self.x += self.xSpeed * self.speedFactor
        self.y += self.ySpeed * self.speedFactor
        # result = False
        if self.x <= 0:
            self.x = 0
            self.xSpeed *= -1
            self.y += 40
            # result = True
        elif self.x >= self.screenWidth - self.imageWidth:
            self.x = self.screenWidth - self.imageWidth
            self.xSpeed *= -1
            self.y += 40
            # result = True
        
        # return result
    
    def reset(self):
        self.y = 0
        self.x = randint(0, self.screenWidth - (self.imageWidth // 2))
        self.speedFactor += 0.1
