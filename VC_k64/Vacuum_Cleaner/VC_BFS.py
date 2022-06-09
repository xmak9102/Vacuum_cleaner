from copy import deepcopy


class VC_BFS():
    def __init__(self, row, col, map, obj):
        self.row = row
        self.col = col
        self.map = map
        self.obj = obj
        self.path = deepcopy(self.map)

    def find_path(self, r, c, back=False):
        parent = {(r, c): None}
        Queue = [(r, c)]

        while len(Queue) > 0:
            (x, y) = Queue.pop(0)

            if self.path[x][y] in [1, 2, 3] and back == False:
                return ((x, y), parent)
            elif (x, y) == (1, 1) and back == True:
                return ((x, y), parent)
            else:
                if self.path[x][y - 1] != -1:
                    if (x, y - 1) not in parent:
                        parent[(x, y - 1)] = (x, y)
                        Queue.append((x, y - 1))

                if self.path[x][y + 1] != -1:
                    if (x, y + 1) not in parent:
                        parent[(x, y + 1)] = (x, y)
                        Queue.append((x, y + 1))

                if self.path[x - 1][y] != -1:
                    if (x - 1, y) not in parent:
                        parent[(x - 1, y)] = (x, y)
                        Queue.append((x - 1, y))

                if self.path[x + 1][y] != -1:
                    if (x + 1, y) not in parent:
                        parent[(x + 1, y)] = (x, y)
                        Queue.append((x + 1, y))

    @staticmethod
    def track(node, way):
        trpath = []
        while way[node] != None:
            trpath.append(node)
            node = way[node]
        return trpath

    def solve(self):
        sol = [(1, 1)]
        bg = (1, 1)

        while self.obj > 0:
            vtx, way = self.find_path(bg[0], bg[1])
            sol.extend(reversed(self.track(vtx, way)))
            bg = vtx
            self.obj -= 1

            if self.path[vtx[0]][vtx[1]] in [2, 3]:
                vtxb, way = self.find_path(vtx[0], vtx[1], back=True)
                sol.extend(reversed(self.track(vtxb, way)))
                bg = (1, 1)

            if self.path[vtx[0]][vtx[1]] in [1, 2]:
                self.path[vtx[0]][vtx[1]] = 0
            elif self.path[vtx[0]][vtx[1]] == 3:
                self.path[vtx[0]][vtx[1]] = 1
                self.obj += 1

        return sol
