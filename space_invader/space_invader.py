# import pygame
import game_files.object as gf
from game_files.player import Player
from game_files.enemy import Enemy

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
        self.background = gf.pygame.image.load("./images/background.png")

    def run(self):
        # game loop
        running = True
        objectsSpeed = 5
        self.player = Player(self.screenWidth, self.screenHeight)
        self.enemy = Enemy(self.screenWidth, self.screenHeight, objectsSpeed)
        while running:
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
                        # match event.key:
                        #     case gf.pygame.K_LEFT:
                        #         self.player.xSpeed = 0
                        #     case gf.pygame.K_RIGHT:
                        #         self.player.xSpeed = 0

                    case _:
                        pass

            self.player.update()

            if self.enemy.update() and self.__check_game_over_conditions():
                running = False

            self.__update_screen()

            gf.pygame.display.update()

    def __update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        self.screen.blit(self.enemy.image, (self.enemy.x, self.enemy.y))

    def __check_game_over_conditions(self) -> bool:
        return self.enemy.y + self.enemy.imageHeight >= self.player.y

    
game = Game()
game.run()