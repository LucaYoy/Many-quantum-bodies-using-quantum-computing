import sys
import BrickWall_51 as bw
import ExactDiag_21 as ed


which = int(sys.argv[1])

parameters = [{'N':qb,'M':5,'j':1.5,'h':1} for qb in range(1,11)]
param = parameters[which]
p = f"N = {str(param['N'])} M = {str(param['M'])} j = {str(param['j'])} h = {str(param['h'])}"

with open("../parameters.txt",'a') as file:
	file.write(p)

print(p)
