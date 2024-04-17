import pygame
import cfg.config as cfg

class Game:
    def __init__(self) -> None:
        # seting pygame
        Game.init()

        # setting window properties
        self.screen = pygame.display.set_mode((cfg.WINDOW_CONFIG.WIDTH, cfg.WINDOW_CONFIG.HEIGHT))
        self.background = pygame.transform.scale(
            pygame.image.load(cfg.WINDOW_CONFIG.BACKGROUND_PATH), (cfg.WINDOW_CONFIG.WIDTH, cfg.WINDOW_CONFIG.HEIGHT)
        ) 
        self.clock = pygame.time.Clock()

        
    @staticmethod
    def init():
        pygame.init()
        pygame.display.set_caption("Space Invader V2")
        pygame.display.set_icon(pygame.image.load(cfg.get_image_path("window", "icon.png")))

    def start(self):
        self.main_menu()


    def main_menu(self):
        self.new_game()        # TODO

    def update_game(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()

    def new_game(self):
        running = True

        while running:
            self.clock.tick(cfg.GAME_CONFIG.FPS)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update_game()
        #end while
        
