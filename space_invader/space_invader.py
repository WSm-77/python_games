# import pygame
import game_files.object as ob
from game_files.player import Player
from game_files.enemy import Enemy
from game_files.bullet import Bullet
from collections import deque

class Game:
    def __init__(self) -> None:
        # pygame initialization
        ob.pygame.init()

        # setting screen
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = ob.pygame.display.set_mode((self.screenWidth, self.screenHeight))

        # setting title, icon and background
        ob.pygame.display.set_caption("Space Invaders")
        self.icon = ob.pygame.image.load("./images/ufo.png")
        ob.pygame.display.set_icon(self.icon)
        self.backgroundImage = ob.pygame.image.load("./images/background.png")

        # setting background music
        self.backgroundMusic = ob.pygame.mixer.music.load("./sounds/background.mp3")

        # creating player
        self.player = None

        # creating enemy
        self.enemy = None

        # creating bullets queue
        self.bullets = deque()

    def run(self):
        ob.pygame.mixer.music.play(-1)
        objectsSpeed = 5

        self.player = Player(self.screenWidth, self.screenHeight)
        self.enemy = Enemy(self.screenWidth, self.screenHeight, objectsSpeed)

        # game loop
        running = True
        while running:
            for event in ob.pygame.event.get():
                match event.type:
                    case ob.pygame.QUIT:
                        running = False

                    case ob.pygame.KEYDOWN:
                        match event.key:
                            case ob.pygame.K_SPACE:
                                self.bullets.append(
                                    Bullet(self.player.x, self.player.y, objectsSpeed, self.screenWidth, self.screenHeight)
                                    )
                            case _:
                                pass

                    case _:
                        pass

            keys = ob.pygame.key.get_pressed()
            if keys[ob.pygame.K_LEFT]:
                self.player.x -= objectsSpeed*self.player.speedFactor
            if keys[ob.pygame.K_RIGHT]:
                self.player.x += objectsSpeed*self.player.speedFactor


            self.player.update()

            if self.enemy.update() and self.__check_game_over_conditions():
                running = False
            
            self.__update_bullets()

            self.__update_screen()

            ob.pygame.display.update()

    def __update_screen(self):
        self.screen.blit(self.backgroundImage, (0, 0))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        self.screen.blit(self.enemy.image, (self.enemy.x, self.enemy.y))
        for bullet in self.bullets:
            self.screen.blit(bullet.image, (bullet.x, bullet.y))

    def __check_game_over_conditions(self) -> bool:
        return self.enemy.y + self.enemy.imageHeight >= self.player.y
    
    def __update_bullets(self):
        i = 0
        while i < len(self.bullets):
            self.bullets[i].update()
            if self.bullets[i].y <= 0:
                del self.bullets[i]
            elif Game.__check_collision(self.bullets[i], self.enemy):
                del self.bullets[i]
                self.enemy.y = 0
            else:
                i += 1

    @staticmethod
    def __check_collision(bullet, enemy):
        if (enemy.y <= bullet.y <= enemy.y + enemy.imageHeight) or (bullet.y <= enemy.y <= bullet.y + bullet.imageHeight):
            if (enemy.x <= bullet.x <= enemy.x + enemy.imageWidth) or (bullet.x <= enemy.x <= bullet.x + bullet.imageWidth):
                return True

        return False

    
game = Game()
game.run()