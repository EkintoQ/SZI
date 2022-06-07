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

pygame.init()
screen = pygame.display.set_mode([RESOLUTION, RESOLUTION])

truck = Truck(screen)
surface_list = []
rubbish_list = []
refused_rubbish_list = []

# x and y are swapped on display in pygame
# matrix for display
matrix = [[0, 1, 1, 2, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 2, 1, 5, 3, 0, 5, 0, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
          [3, 3, 3, 0, 0, 0, 2, 5, 0, 5, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          ]
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
while True:
    pygame.time.delay(500)

    # drawing on screen
    for i in surface_list:
        i.draw_surface()
    for i in rubbish_list:
        i.draw_rubbish()
    for i in refused_rubbish_list:
        i.draw_rubbish()
    truck.draw_truck()

    # finding a path to rubbish
    if rubbish_list and not path:
        start = (truck.y / 60, truck.x / 60)
        direction = truck.direction
        currentRubbish = rubbish_list[0]
        endpoint = (currentRubbish.y / 60, currentRubbish.x / 60)
        # path = bfs(surface_list, endpoint).tree_search(deque(), start, direction)
        path = a_star(surface_list, endpoint).tree_search(PriorityQueue(), start, direction)

    # do an action
    if path:
        action = path.pop(0)
        if action == 'M':
            truck.move()
        else:
            truck.change_direction(action)

    # the decision that takes what to do with the garbage
    if not path and rubbish_list:
        data = rubbish_list[0].data_for_decision_tree()
        print(f'----------\n'
              f'Characteristics of the garbage we met:\n'
              f'Weight:{data[0]}\nDensity:{data[1]}\n'
              f'Fragility:{data[2]}\nMaterial:{data[3]}\n'
              f'Size:{data[4]}\nDegradability:{data[4]}\n'
              f'Renewability:{data[5]}\n'
              f'----------')
        decision = trash_selection(evaluate_values(data))
        if decision == [0]:
            print('We refused this rubbish because of bad characteristics')
            rubbish_list[0].rubbish_refused()
            refused_rubbish_list.append(rubbish_list[0])
        else:
            print('We take this rubbish because of good characteristics')
        rubbish_list.pop(0)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
