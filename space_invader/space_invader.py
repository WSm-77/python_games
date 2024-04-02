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
        self.player = Player(self.screenWidth, self.screenHeight)
        while running:
            self.screen.fill((0, 150, 0))
            for event in gf.pygame.event.get():
                match event.type:
                    case gf.pygame.QUIT:
                        running = False

            self.update_screen()

            gf.pygame.display.update()

    def update_screen(self):
        self.screen.blit(self.player.image, (self.player.x, self.player.y))

    
game = Game()
game.run()