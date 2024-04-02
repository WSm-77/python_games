# import pygame
import game_files.object as gf
from game_files.player import Player

class Game:
    def __init__(self) -> None:
        # pygame initialization
        gf.pygame.init()

        # setting screen
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = gf.pygame.display.set_mode((self.screenWidth, self.screenHeight))

        # setting title and icon
        gf.pygame.display.set_caption("Space Invaders")
        self.icon = gf.pygame.image.load("./images/ufo.png")
        gf.pygame.display.set_icon(self.icon)

        # creating player
        self.player = None

        # creating enemy
        self.enemy = None


    def run(self):
        # game loop
        running = True
        objectsSpeed = 1
        self.player = Player(self.screenWidth, self.screenHeight)
        while running:

            self.screen.fill((0, 150, 0))
            # self.player.xSpeed = objectsSpeed

            for event in gf.pygame.event.get():
                match event.type:
                    case gf.pygame.QUIT:
                        running = False

                    case gf.pygame.KEYDOWN:
                        match event.key:
                            case gf.pygame.K_LEFT:
                                self.player.xSpeed = -objectsSpeed
                            case gf.pygame.K_RIGHT:
                                self.player.xSpeed = objectsSpeed
                            case _:
                                pass
                    case gf.pygame.KEYUP:
                        if event.key == gf.pygame.K_LEFT or event.key == gf.pygame.K_RIGHT:
                            self.player.xSpeed = 0

                    case _:
                        pass

            self.player.update()
            self.update_screen()

            gf.pygame.display.update()

    def update_screen(self):
        self.screen.blit(self.player.image, (self.player.x, self.player.y))

    
game = Game()
game.run()