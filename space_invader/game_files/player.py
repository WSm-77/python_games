import game_files.object as ob

class Player(ob.Object):
    def __init__(self, screenWidth, screenHeight) -> None:
        image = ob.pygame.image.load("./images/player-ship.png")
        imageWidth = 64
        imageHeight = 64
        super().__init__((screenWidth // 2) - (imageWidth // 2), screenHeight - imageHeight - 10, 0, 0, image, imageWidth, imageHeight)