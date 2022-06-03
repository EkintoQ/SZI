import pygame


class Surface:

    def __init__(self, screen, x, y, weight):
        self.state = (x, y)
        self.x = x
        self.y = y
        self.weight = weight
        self.screen = screen
        self.image = pygame.image.load('images/grass.png')
        self.surface_rect = self.image.get_rect()
        self.surface_rect.center = (self.x + 30, self.y + 30)

    def draw_surface(self):
        self.screen.blit(self.image, self.surface_rect)


class Grass(Surface):

    def __init__(self, screen, x, y, weight):
        super().__init__(screen, x, y, weight)
        self.image = pygame.image.load('images/grass.png')


class Rock(Surface):

    def __init__(self, screen, x, y, weight):
        super().__init__(screen, x, y, weight)
        self.image = pygame.image.load('images/rock.png')


class Water(Surface):

    def __init__(self, screen, x, y, weight):
        super().__init__(screen, x, y, weight)
        self.image = pygame.image.load('images/water.png')
