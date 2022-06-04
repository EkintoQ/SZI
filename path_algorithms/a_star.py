def get_path(cond):
    path = []
    while cond.parent:
        path.append(cond.action)
        cond = cond.parent
    return list(reversed(path))


class a_star:
    def __init__(self, surface_list, endpoint):
        self.surface_list = surface_list
        self.endpoint = endpoint

    def goal_achieved(self, state):
        return state == self.endpoint

    # checking borders and impassable surface
    def limitation_check(self, x, y):
        for surface in self.surface_list:
            if (surface.y / 60 == x) and (surface.x / 60 == y) and (surface.weight != -1):
                return True
        return False

    # finding surface depending on coordinates
    def current_surface(self, x, y):
        for surface in self.surface_list:
            if (x == surface.y / 60) and (y == surface.x / 60):
                return surface
        return None

    # manhattan distance
    def h(self, current):
        return abs(current[0] - self.endpoint[0]) + abs(current[1] - self.endpoint[1])

    # cost relative to surface weight
    def g(self, cond):
        if cond.action == 'L' or cond.action == 'R':
            cond.weight = cond.parent.weight + 1
        else:
            cond.weight = cond.parent.weight + self.current_surface(cond.state[0], cond.state[1]).weight
        return cond.weight

    def add_all_possibilities(self, current):
        states = []
        if current.direction == 'L':
            # when you look left and turn left
            new_condition = condition(current.state, 'D')
            new_condition.action = 'L'
            states.append(new_condition)
            # when you turn right
            new_condition = condition(current.state, 'U')
            new_condition.action = 'R'
            states.append(new_condition)
            # when you move
            if self.limitation_check(current.state[0], current.state[1] - 1):
                new_condition = condition((current.state[0], current.state[1] - 1), current.direction)
                new_condition.action = 'M'
                states.append(new_condition)

        if current.direction == 'U':
            # when you look up and turn left
            new_condition = condition(current.state, 'L')
            new_condition.action = 'L'
            states.append(new_condition)
            # when you turn right
            new_condition = condition(current.state, 'R')
            new_condition.action = 'R'
            states.append(new_condition)
            # when you move
            if self.limitation_check(current.state[0] - 1, current.state[1]):
                new_condition = condition((current.state[0] - 1, current.state[1]), current.direction)
                new_condition.action = 'M'
                states.append(new_condition)

        if current.direction == 'R':
            # when you look right and turn left
            new_condition = condition(current.state, 'U')
            new_condition.action = 'L'
            states.append(new_condition)
            # when you turn right
            new_condition = condition(current.state, 'D')
            new_condition.action = 'R'
            states.append(new_condition)
            # when you move
            if self.limitation_check(current.state[0], current.state[1] + 1):
                new_condition = condition((current.state[0], current.state[1] + 1), current.direction)
                new_condition.action = 'M'
                states.append(new_condition)

        if current.direction == 'D':
            # when you look down and turn left
            new_condition = condition(current.state, 'R')
            new_condition.action = 'L'
            states.append(new_condition)
            # when you turn right
            new_condition = condition(current.state, 'L')
            new_condition.action = 'R'
            states.append(new_condition)
            # when you move
            if self.limitation_check(current.state[0] + 1, current.state[1]):
                new_condition = condition((current.state[0] + 1, current.state[1]), current.direction)
                new_condition.action = 'M'
                states.append(new_condition)
        return states

    def tree_search(self, queue, start, direction):
        explored = []
        queue.put(condition(start, direction), 0)
        while queue:
            elem = queue.get()

            if self.goal_achieved(elem.state):
                return get_path(elem)

            explored.append(elem)

            for state in self.add_all_possibilities(elem):
                state.parent = elem
                f = self.h(state.state) + self.g(state)
                if state not in queue.queue and state not in explored:
                    queue.put(state, state.weight)
                elif state in queue.queue and state.weight > f:
                    queue.replace(state, f)


class condition:
    def __init__(self, state, direction):
        self.state = state
        self.parent = None
        self.action = None
        self.direction = direction
        self.weight = 0

    def __eq__(self, other):
        if isinstance(other, condition):
            return (self.state == other.state and
                    self.action == other.action and
                    self.direction == other.direction)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight
