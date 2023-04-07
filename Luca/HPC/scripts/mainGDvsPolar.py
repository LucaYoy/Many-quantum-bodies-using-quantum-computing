import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_adam as ed
#import plots_9 as plts
import pickle
import time
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-9
which = int(sys.argv[1])

# parameters = [{'N':14,'j':1,'h':1,'g':1,'M':5,'maxIterations':20000,'run':i} for i in range(1,11)]
# param = parameters[which]

N,j,h,g,M,maxIterations,run = 8,1,1,1,5,80000,which+1
psiTarget = ed.exactDiagSparse(N,j,h,g)[2].reshape(tuple([2]*N))

time1 = time.time()
approxStatePolar = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=False)[1:]
time2 = time.time()
print(f'approxStatePolar took {time2-time1}s')
approxStateGD = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=True)[1:]
time3 = timer.time()
print(f'approxStateGD took {time3-time2}s')

with open(f'approxStateGD{run}.pkl','wb') as f:
	pickle.dump(approxStateGD,f)
with open(f'approxStatePolar{run}.pkl','wb') as f:
	pickle.dump(approxStatePolar,f)