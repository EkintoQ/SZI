# from collections import deque
from queue import PriorityQueue

import matplotlib.pyplot as plt

from neural import *
from path_algorithms.a_star import a_star
# from path_algorithms.bfs import bfs
from rubbish import *
from tree import evaluate_values, trash_selection
from truck import Truck
from surface import *
from PIL import Image
from genetic import genetic

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
X,y = create_training_data()
model = learn_neural_network(X,y)

gen = [(truck.y / 60, truck.x / 60)]
fl = 0
length = []
finalLength = []
order = []
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

    # finding order to collect rubbish
    if fl == 0:
        for item in rubbish_list:
            print(item.y / 60, item.x / 60, end='\n')
            gen.append((item.y / 60, item.x / 60))
        for item1 in range(len(gen)):
            for item2 in range(len(gen)):
                if item1 < item2:
                    length.append(len(a_star(surface_list, gen[item2]).tree_search(PriorityQueue(), gen[item1], 'R')))
                else:
                    length.append(0)
            finalLength.append(length)
            length = []
        fl = 1
        for i in range(len(finalLength)):
            for j in range(len(finalLength)):
                if i > j:
                    finalLength[i][j] = finalLength[j][i]
        for i in range(len(finalLength)):
            for j in range(len(finalLength)):
                print(finalLength[i][j], end=',')
            print('')
        print(finalLength)
        order = genetic(finalLength).search()
        order = list(map(int, order))
        order.pop(0)
        for j in range(len(order)):
            order[j] -= 1

    # finding a path to rubbish
    if order and not path:
        start = (truck.y / 60, truck.x / 60)
        direction = truck.direction
        currentRubbish = rubbish_list[order[0]]
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
    if not path and order:

        number = np.random.randint(2077)
        path_img = "images/bbb"
        img = Image.open(path_img+'/'+str(number)+'.jpg')
        img.show()
        prediction = predict(model,path_img+'/'+str(number)+'.jpg')
        result(prediction)
        data = rubbish_list[order[0]].data_for_decision_tree()
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
            rubbish_list[order[0]].rubbish_refused()
            refused_rubbish_list.append(rubbish_list[order[0]])
        else:
            print('We take this rubbish because of good characteristics')
        order.pop(0)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
