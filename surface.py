import pygame


class Surface:

    def __init__(self, screen, x, y):
        self.state = (x, y)
        self.x = x
        self.y = y
        self.weight = 0
        self.screen = screen
        self.image = pygame.image.load('images/grass.png')
        self.surface_rect = self.image.get_rect()
        self.surface_rect.center = (self.x + 30, self.y + 30)

    def draw_surface(self):
        self.screen.blit(self.image, self.surface_rect)


class Grass(Surface):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.weight = 1
        self.image = pygame.image.load('images/grass.png')


class Rock(Surface):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.weight = 50
        self.image = pygame.image.load('images/rock.png')


class Water(Surface):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.weight = 3
        self.image = pygame.image.load('images/water.png')
