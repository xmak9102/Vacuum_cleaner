import VC_Solver
from Map import Map_Creator
import os


savefig_path = os.path.realpath("Result")
filtered_files = os.listdir(savefig_path)
for file in filtered_files:
    path_to_file = os.path.join(savefig_path, file)
    os.remove(path_to_file)

m = 3
n = 5
mc = Map_Creator.map_creator(m, n)
mc.create_map(pd=[0.1, 0.3, 0.3, 0.2, 0.1])
obj = mc.getobj()
map = mc.getmap()

model = VC_Solver.VC_solver(m, n, map, obj)
model.addSolver(method=['BFS', 'As'])
model.solve()
model.plotMovement()
