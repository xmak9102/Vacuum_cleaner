from copy import deepcopy


class sQueue():
    def __init__(self, priority):
        self.queue = []
        self.queue_length = 0
        self.priority = priority

    def bin_search(self, e, l, r):
        if l <= r:
            mid = (l + r)//2
            if self.priority(self.queue[mid]) < self.priority(e):
                return self.bin_search(e, l, mid - 1)
            elif self.priority(self.queue[mid]) >= self.priority(e):
                return self.bin_search(e, mid + 1, r)
        else:
            return l

    def insertElement(self, element):
        self.queue.insert(self.bin_search(
            element, 0, self.queue_length - 1), element)
        self.queue_length += 1

    def deleteElement(self):
        self.queue_length -= 1
        return self.queue.pop()

    def sortQueue(self):
        self.queue.sort(reverse=True, key=self.priority)

    def getlength(self):
        return self.queue_length

    def getQueue(self):
        return self.queue

    def __str__(self):
        return str(self.queue)


class VC_As():
    def __init__(self, row, col, map, obj):
        self.row = row
        self.col = col
        self.map = map
        self.obj = obj
        self.path = deepcopy(map)

    @staticmethod
    def shortest_path(path_tmp, r, c):
        def md(n1, n2): return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
        ptr = (r, c)
        tmp = {(r, c): 0}
        Queue = sQueue(priority=lambda x: tmp[x])
        Queue.insertElement((r, c))
        way = 0

        while Queue.getlength() > 0:
            (x, y) = Queue.deleteElement()
            if path_tmp[x][y] in [1, 2, 3]:
                if path_tmp[x][y] == 1:
                    way += md(ptr, (x, y))
                    ptr = (x, y)
                    path_tmp[x][y] = 0
                elif path_tmp[x][y] == 2:
                    way += md(ptr, (x, y))
                    ptr = (1, 1)
                    path_tmp[x][y] = 0
                elif path_tmp[x][y] == 3:
                    way += md(ptr, (x, y))
                    ptr = (1, 1)
                    path_tmp[x][y] = 1
                    Queue.insertElement((x, y))

                for i in Queue.getQueue():
                    tmp[i] = md(ptr, i)
                Queue.sortQueue()

            if path_tmp[x][y - 1] != -1:
                if (x, y - 1) not in tmp:
                    tmp[(x, y - 1)] = md(ptr, (x, y - 1))
                    Queue.insertElement((x, y - 1))
            if path_tmp[x][y + 1] != -1:
                if (x, y + 1) not in tmp:
                    tmp[(x, y + 1)] = md(ptr, (x, y + 1))
                    Queue.insertElement((x, y + 1))
            if path_tmp[x - 1][y] != -1:
                if (x - 1, y) not in tmp:
                    tmp[(x - 1, y)] = md(ptr, (x - 1, y))
                    Queue.insertElement((x - 1, y))
            if path_tmp[x + 1][y] != -1:
                if (x + 1, y) not in tmp:
                    tmp[(x + 1, y)] = md(ptr, (x + 1, y))
                    Queue.insertElement((x + 1, y))

        return way

    def search(self, r, c, nb=5):
        temp = {(r, c): (0, None)}
        Queue = [(r, c)]
        neighbor = []

        while nb > 0 and len(Queue) > 0:
            (x, y) = Queue.pop(0)

            if self.path[x][y] in [1, 2, 3]:
                neighbor.append((x, y))
                nb -= 1
            else:
                if self.path[x][y - 1] != -1:
                    if (x, y - 1) not in temp:
                        temp[(x, y - 1)] = (temp[(x, y)][0] + 1, (x, y))
                        Queue.append((x, y - 1))

                if self.path[x][y + 1] != -1:
                    if (x, y + 1) not in temp:
                        temp[(x, y + 1)] = (temp[(x, y)][0] + 1, (x, y))
                        Queue.append((x, y + 1))

                if self.path[x - 1][y] != -1:
                    if (x - 1, y) not in temp:
                        temp[(x - 1, y)] = (temp[(x, y)][0] + 1, (x, y))
                        Queue.append((x - 1, y))

                if self.path[x + 1][y] != -1:
                    if (x + 1, y) not in temp:
                        temp[(x + 1, y)] = (temp[(x, y)][0] + 1, (x, y))
                        Queue.append((x + 1, y))

        sp = self.row*self.row*self.col*self.col
        for i, j in neighbor:
            if self.path[i][j] == 1:
                path_tmp = deepcopy(self.path)
                path_tmp[i][j] = 0
                p = self.shortest_path(path_tmp, i, j)
                if sp > temp[(i, j)][0] + p:
                    sp = temp[(i, j)][0] + p
                    goal = (i, j)
            elif self.path[i][j] == 2:
                path_tmp = deepcopy(self.path)
                path_tmp[i][j] = 0
                p = self.shortest_path(path_tmp, 1, 1)
                if sp > temp[(i, j)][0] + p:
                    sp = temp[(i, j)][0] + p
                    goal = (i, j)
            elif self.path[i][j] == 3:
                path_tmp = deepcopy(self.path)
                path_tmp[i][j] = 1
                p = self.shortest_path(path_tmp, 1, 1)
                if sp > temp[(i, j)][0] + p:
                    sp = temp[(i, j)][0] + p
                    goal = (i, j)

        return (goal, temp)

    def goto11(self, r, c):
        temp = {(r, c): (r + c - 2, 0, None)}
        stack = sQueue(priority=lambda x: temp[x][0])
        stack.insertElement((r, c))
        best_path = self.row*self.col

        while stack.getlength() > 0:
            (x, y) = stack.deleteElement()
            z = temp[(x, y)][1]

            if (x, y) == (1, 1):
                if best_path > temp[(x, y)][0] + z:
                    goal = (x, y)
                    best_path = temp[(x, y)][0] + z
            else:
                lt = x + y - 1 - \
                    2 if self.path[x][y - 1] != -1 else self.row*self.col
                rt = x + y + 1 - \
                    2 if self.path[x][y + 1] != -1 else self.row*self.col
                up = x - 1 + y - \
                    2 if self.path[x - 1][y] != -1 else self.row*self.col
                dn = x + 1 + y - \
                    2 if self.path[x + 1][y] != -1 else self.row*self.col

                if lt + z + 1 <= best_path:
                    if (x, y - 1) not in temp:
                        temp[(x, y - 1)] = (lt, z + 1, (x, y))
                        stack.insertElement((x, y - 1))
                    else:
                        if z + 1 < temp[(x, y - 1)][1]:
                            temp[(x, y - 1)] = (lt, z + 1, (x, y))
                            stack.insertElement((x, y - 1))

                if rt + z + 1 <= best_path:
                    if (x, y + 1) not in temp:
                        temp[(x, y + 1)] = (rt, z + 1, (x, y))
                        stack.insertElement((x, y + 1))
                    else:
                        if z + 1 < temp[(x, y + 1)][1]:
                            temp[(x, y + 1)] = (rt, z + 1, (x, y))
                            stack.insertElement((x, y + 1))

                if up + z + 1 <= best_path:
                    if (x - 1, y) not in temp:
                        temp[(x - 1, y)] = (up, z + 1, (x, y))
                        stack.insertElement((x - 1, y))
                    else:
                        if z + 1 < temp[(x - 1, y)][1]:
                            temp[(x - 1, y)] = (up, z + 1, (x, y))
                            stack.insertElement((x - 1, y))

                if dn + z + 1 <= best_path:
                    if (x + 1, y) not in temp:
                        temp[(x + 1, y)] = (dn, z + 1, (x, y))
                        stack.insertElement((x + 1, y))
                    else:
                        if z + 1 < temp[(x + 1, y)][1]:
                            temp[(x + 1, y)] = (dn, z + 1, (x, y))
                            stack.insertElement((x + 1, y))

        return temp

    def solve(self):
        sol = [(1, 1)]
        bg = (1, 1)

        while self.obj > 0:
            pos, way = self.search(bg[0], bg[1])
            traced_path = []
            loc = pos
            while way[loc][-1] != None:
                traced_path.append(loc)
                loc = way[loc][-1]

            sol.extend(reversed(traced_path))
            self.obj -= 1
            bg = pos
            if self.path[pos[0]][pos[1]] in [2, 3]:
                wayto11 = self.goto11(pos[0], pos[1])

                traced_path = []
                loc = (1, 1)
                while wayto11[loc][-1] != None:
                    traced_path.append(loc)
                    loc = wayto11[loc][-1]

                sol.extend(reversed(traced_path))
                bg = (1, 1)

            if self.path[pos[0]][pos[1]] == 3:
                self.path[pos[0]][pos[1]] = 1
                self.obj += 1
            else:
                self.path[pos[0]][pos[1]] = 0

        return sol
