import pygame


class Truck:

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.state = (self.x, self.y)
        self.direction = 'R'
        self.screen = screen
        self.image = pygame.image.load('images/truck.png')
        self.truck_rect = self.image.get_rect()
        self.truck_rect.center = (self.x + 30, self.y + 30)

    def draw_truck(self):
        self.screen.blit(self.image, self.truck_rect)

    def change_image(self):
        if self.direction == 'R':
            self.image = pygame.image.load('images/truck.png')
            self.truck_rect = self.image.get_rect()
            self.truck_rect.center = (self.x + 30, self.y + 30)
        if self.direction == 'L':
            self.image = pygame.image.load('images/truck_l.png')
            self.truck_rect = self.image.get_rect()
            self.truck_rect.center = (self.x + 30, self.y + 30)
        if self.direction == 'U':
            self.image = pygame.image.load('images/truck_u.png')
            self.truck_rect = self.image.get_rect()
            self.truck_rect.center = (self.x + 30, self.y + 30)
        if self.direction == 'D':
            self.image = pygame.image.load('images/truck_d.png')
            self.truck_rect = self.image.get_rect()
            self.truck_rect.center = (self.x + 30, self.y + 30)

    def change_direction(self, turn):
        if turn == 'L':
            if self.direction == 'R':
                self.direction = 'U'
            elif self.direction == 'U':
                self.direction = 'L'
            elif self.direction == 'L':
                self.direction = 'D'
            elif self.direction == 'D':
                self.direction = 'R'
        if turn == 'R':
            if self.direction == 'R':
                self.direction = 'D'
            elif self.direction == 'U':
                self.direction = 'R'
            elif self.direction == 'L':
                self.direction = 'U'
            elif self.direction == 'D':
                self.direction = 'L'
        self.change_image()

    def move(self):
        if self.direction == 'R':
            self.move_right()
        if self.direction == 'U':
            self.move_up()
        if self.direction == 'L':
            self.move_left()
        if self.direction == 'D':
            self.move_down()

    def move_right(self):
        self.x += 60
        self.truck_rect.center = (self.x + 30, self.y + 30)

    def move_left(self):
        self.x -= 60
        self.truck_rect.center = (self.x + 30, self.y + 30)

    def move_up(self):
        self.y -= 60
        self.truck_rect.center = (self.x + 30, self.y + 30)

    def move_down(self):
        self.y += 60
        self.truck_rect.center = (self.x + 30, self.y + 30)
