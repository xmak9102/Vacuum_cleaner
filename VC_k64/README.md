@README

# VACUUM CLEANER

&nbsp;

##### Component

- Folder Vacuum_Cleaner contains all source codes of the project
- Folder Map contains map generator tool randomly with probability distribution
- File VC_solver.py integrate the source codes of solving and help ploting
- Folder Result contains picture of the output in the .png format
- main.py is the main program to which all other codes are imported

##### Instruction

###### In main.py, there are 2 parameter to be passed, m and n, number of rows and number of column respectively. Then the map generate randomly with probability distribution (pd) which is [0.1, 0.3, 0.3, 0.2, 0.1] (can be changed in main.py).

&nbsp;

> Probability distribution have 5 parameter included in a list. The 1st one is the probability to assign a square to be block. The 2nd one is the probability to assign a square to be vacant. The 3rd one is the probability to assign a square to contain dirt only. The 4st one is the probability to assign a square to contain jewel only. The last one is the probability to assign a square to contain both dirt and jewel.

&nbsp;

###### The syntax to call VC_Solver is model = VC_Solver.VC_solver(m, n, map, obj) where map and obj is generate by Map_Creator. To solve the problem in different ways, call model.addSolver(<method>). <method> is a list of method for solver such as 'BFS', 'A*'. To use 'BFS', add 'BFS' to <method>.  To use 'A*', add 'As' to <method>. 

&nbsp;

###### After running main.py, figures plotted by matplotlib.plt are saved in folder Result in .png format. Folder Result is emptied automatically before new map is generated.