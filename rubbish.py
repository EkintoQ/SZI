import random

import pygame


class Rubbish:

    def __init__(self, screen, x, y):
        self.state = (x, y)
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('images/garbage.png')
        self.surface_rect = self.image.get_rect()
        self.surface_rect.center = (self.x + 30, self.y + 30)
        self.weight = random.randint(0, 10)
        self.density = random.randint(0, 10)
        self.fragility = random.randint(0, 10)
        self.dirty = random.randint(0, 10)
        self.size = random.randint(0, 10)
        self.degradability = random.randint(0, 10)
        self.renewability = random.randint(0, 10)

    def draw_rubbish(self):
        self.screen.blit(self.image, self.surface_rect)


class Paper_waste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class Organic_waste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class Glass_waste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class Plastic_waste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class E_waste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class Metal_waste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
