import numpy as np


class map_creator():
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.map = []

    def check_map(self, map):
        valid = [(1, 1)]
        Queue = [(1, 1)]

        while len(Queue) > 0:
            (x, y) = Queue.pop(0)

            if map[x][y] != -1:
                if map[x][y - 1] != -1:
                    if (x, y - 1) not in valid:
                        valid.append((x, y - 1))
                        Queue.append((x, y - 1))

                if map[x][y + 1] != -1:
                    if (x, y + 1) not in valid:
                        valid.append((x, y + 1))
                        Queue.append((x, y + 1))

                if map[x - 1][y] != -1:
                    if (x - 1, y) not in valid:
                        valid.append((x - 1, y))
                        Queue.append((x - 1, y))

                if map[x + 1][y] != -1:
                    if (x + 1, y) not in valid:
                        valid.append((x + 1, y))
                        Queue.append((x + 1, y))

        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                if (i, j) not in valid and map[i][j] in [1, 2, 3]:
                    return False

        return True

    def create_map(self, pd=[0.1, 0.3, 0.3, 0.2, 0.1]):
        while True:
            map = [[-1] + list(np.random.choice(np.arange(-1, 4, 1),
                               self.col, p=pd)) + [-1] for i in range(self.row)]
            map.insert(0, [-1 for i in range(0, self.col + 2)])
            map.append([-1 for i in range(0, self.col + 2)])
            map[1][1] = 0

            if self.check_map(map) == True:
                self.map = map
                break

    def getobj(self):
        num = 0
        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                if self.map[i][j] in [1, 2, 3]:
                    num += 1

        return num

    def getmap(self):
        return self.map
