import pygame


class Surface:

    def __init__(self, screen, x, y):
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
        self.weight = 9
        self.image = pygame.image.load('images/rock.png')


class Sand(Surface):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.weight = 3
        self.image = pygame.image.load('images/sand.png')


class Water(Surface):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.weight = -1
        self.image = pygame.image.load('images/water.png')
