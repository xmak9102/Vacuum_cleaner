from Vacuum_Cleaner import VC_BFS, VC_As
import matplotlib.pyplot as plt
from copy import deepcopy
import os


class VC_solver():
    def __init__(self, row, col, map, obj):
        self.row = row
        self.col = col
        self.map = map
        self.obj = obj
        self.solver = []
        self.id = []
        self.solution = []

    NS = -1

    def addSolver(self, method=['BFS']):
        for i in method:
            self.NS += 1

            if i == 'BFS':
                self.solver.append(VC_BFS.VC_BFS(
                    self.row, self.col, self.map, self.obj))
                self.id.append('BFS')
            elif i == 'As':
                self.solver.append(VC_As.VC_As(
                    self.row, self.col, self.map, self.obj))
                self.id.append('As')

    def solve(self):
        for i in self.solver:
            self.solution.append(i.solve())

    def getSolution(self):
        return self.solution

    def plotMovement(self):
        fig, ax = plt.subplots(1, self.NS + 1)
        for i in range(self.NS + 1):
            ax[i].tick_params(left=False, bottom=False,
                              labelleft=False, labelbottom=False)

        node_list = deepcopy(self.solution)
        map = []
        for i in range(self.NS + 1):
            map.append(deepcopy(self.map))
        go_back = (self.NS + 1)*[False]
        step = -1
        while node_list != (self.NS + 1)*[None]:
            step += 1

            for i in range(self.NS + 1):
                if node_list[i] != None:
                    vertex = node_list[i].pop(0)
                    if go_back[i] == False:
                        if map[i][vertex[0]][vertex[1]] in [1, 2]:
                            if map[i][vertex[0]][vertex[1]] == 2:
                                go_back[i] = True
                            map[i][vertex[0]][vertex[1]] = 0
                        elif map[i][vertex[0]][vertex[1]] == 3:
                            go_back[i] = True
                            map[i][vertex[0]][vertex[1]] = 1
                    else:
                        if vertex == (1, 1):
                            go_back[i] = False

                    if len(node_list[i]) == 0:
                        node_list[i] = None

                    ax[i].cla()
                    ax[i].imshow(map[i])
                    ax[i].set_title(self.id[i])
                    ax[i].set_xlabel('Step {}'.format(step))
                    ax[i].plot(vertex[1], vertex[0], 'rx')

                    plt.pause(0.05)

            fig.savefig(os.path.realpath("Result") + "/Step {}".format(step))
