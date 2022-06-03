def get_path(cond):
    path = []
    while cond.parent:
        path.append(cond.action)
        cond = cond.parent
    return list(reversed(path))


class bfs:
    def __init__(self, surface_list, endpoint):
        self.surface_list = surface_list
        self.endpoint = endpoint

    def goal_achieved(self, state):
        return state == self.endpoint

    def limitation_check(self, x, y):
        for surface in self.surface_list:
            if (surface.weight == 1) and (surface.y/60 == x) and (surface.x/60 == y):
                return True
        return False

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
        queue.append(condition(start, direction))
        while queue:
            elem = queue.popleft()

            if self.goal_achieved(elem.state):
                return get_path(elem)

            for state in self.add_all_possibilities(elem):
                if state not in queue:
                    state.parent = elem
                    queue.append(state)


class condition:
    def __init__(self, state, direction):
        self.state = state
        self.parent = None
        self.action = None
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, condition):
            return (self.state == other.state and
                    self.action == other.action and
                    self.direction == other.direction)
