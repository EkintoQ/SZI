# from collections import deque
from queue import PriorityQueue

from path_algorithms.a_star import a_star
# from path_algorithms.bfs import bfs
from rubbish import *
from tree import evaluate_values, trash_selection
from truck import Truck
from surface import *

RESOLUTION = 900
SIZE = 60

# matrix for display
matrix = [[0, 1, 1, 2, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 2, 1, 5, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
          [3, 3, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          ]
pygame.init()
screen = pygame.display.set_mode([RESOLUTION, RESOLUTION])

truck = Truck(screen)
surface_list = []
rubbish_list = []
# x and y are swapped on display in pygame
for i in range(15):
    for j in range(15):
        if matrix[i][j] == 0:
            surface_list.append(Grass(screen, j * 60, i * 60))
        if matrix[i][j] == 1:
            surface_list.append(Sand(screen, j * 60, i * 60))
        if matrix[i][j] == 2:
            surface_list.append(Rock(screen, j * 60, i * 60))
        if matrix[i][j] == 3:
            surface_list.append(Water(screen, j * 60, i * 60))
        if matrix[i][j] == 5:
            surface_list.append(Grass(screen, j * 60, i * 60))
            rubbish_list.append(Rubbish(screen, j * 60, i * 60))

path = []
run = 1
while True:
    pygame.time.delay(500)

    for i in surface_list:
        i.draw_surface()
    for i in rubbish_list:
        i.draw_rubbish()
    truck.draw_truck()

    if run == 1:
        # func(rubbish_list[0])
        data = rubbish_list[0].data_for_decision_tree()
        test = trash_selection(evaluate_values(data))
        print(test)
        run = 0

    if rubbish_list and not path:
        start = (truck.y / 60, truck.x / 60)
        direction = truck.direction
        currentRubbish = rubbish_list[0]
        endpoint = (currentRubbish.y / 60, currentRubbish.x / 60)
        # path = bfs(surface_list, endpoint).tree_search(deque(), start, direction)
        path = a_star(surface_list, endpoint).tree_search(PriorityQueue(), start, direction)

    if path:
        action = path.pop(0)
        if action == 'M':
            truck.move()
        else:
            truck.change_direction(action)
    if not path:
        if rubbish_list:
            print(rubbish_list.pop(0).x)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
