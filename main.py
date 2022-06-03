from collections import deque

from path_algorithms.bfs import bfs
from truck import Truck
from surface import *

RESOLUTION = 900
SIZE = 60

# matrix for display
matrix = [[1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 3, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
          [3, 3, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          ]
pygame.init()
screen = pygame.display.set_mode([RESOLUTION, RESOLUTION])
truck = Truck(screen)
surface_list = []
# x and y are swapped on display in pygame
for i in range(15):
    for j in range(15):
        if matrix[i][j] == 1:
            surface_list.append(Grass(screen, j * 60, i * 60, 1))
        if matrix[i][j] == 2:
            surface_list.append(Rock(screen, j * 60, i * 60, 2))
        if matrix[i][j] == 3:
            surface_list.append(Water(screen, j * 60, i * 60, 3))

run = 1
path = []
while True:
    pygame.time.delay(500)

    for i in surface_list:
        i.draw_surface()
    truck.draw_truck()

    if run == 1:
        start = truck.state
        direction = truck.direction
        endpoint = (0, 5)
        path = bfs(surface_list, endpoint).tree_search(deque(), start, direction)
        print(path)
        run = 0

    if path:
        action = path.pop(0)
        if action == 'M':
            truck.move()
        else:
            truck.change_direction(action)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
