import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_adam as ed
#import plots_9 as plts
import pickle
#import Entropy as en
#import matplotlib.pyplot as plt

import psutil
process = psutil.Process() # get current process to check memory usage

#sh file array 0-9
which = int(sys.argv[1])

# parameters = [{'N':14,'j':1,'h':1,'g':1,'M':5,'maxIterations':200,'run':i} for i in range(1,11)]
# param = parameters[which]

N,j,h,g,M,maxIterations,run = 14,1,1,1,5,20000,which+1

psiTarget = ed.exactDiagSparse(N,j,h,g)[2].reshape(tuple([2]*N))

print("psiTarget created")
print(f"Memory used: {process.memory_info().rss/(1024)**3:.3f} GB") # print memory used to 3 significant figures

approxStateRand = bw.BrickWallCircuit(N,M,gatesRandomFlag=True).optimize(psiTarget, 0.0001, maxIterations,GD=False)[1:]

print("optimisation random done")
print(f"Memory used: {process.memory_info().rss/(1024)**3:.3f} GB") # print memory used to 3 significant figures

approxStateId = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=False)[1:]

print("optimisation id done")
print(f"Memory used: {process.memory_info().rss/(1024)**3:.3f} GB") # print memory used to 3 significant figures

with open(f'approxStateRand{run}.pkl','wb') as f:
	pickle.dump(approxStateRand,f)
with open(f'approxStateId{run}.pkl','wb') as f:
	pickle.dump(approxStateId,f)