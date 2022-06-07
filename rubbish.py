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
        self.weight = random.choice([10, 15, 20, 30, 40])
        self.density = random.choice([True, False])
        self.fragility = random.randint(1, 10)
        self.material = random.choice(["plastic", "wood", "metal", "glass", "paper"])
        self.size = random.choice(["little", "medium", "huge", "large"])
        self.degradability = random.randint(1, 10)
        self.renewability = random.randint(1, 10)

    def draw_rubbish(self):
        self.screen.blit(self.image, self.surface_rect)

    def data_for_decision_tree(self):
        return [self.weight, self.density, self.fragility, self.material, self.size, self.degradability, self.renewability]


class PaperWaste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class OrganicWaste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class GlassWaste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class PlasticWaste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class EWaste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)


class MetalWaste(Rubbish):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
