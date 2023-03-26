import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_21 as ed
#import plots_9 as plts
import pickle
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-9
which = int(sys.argv[1])

parameters = [{'N':14,'j':1,'h':1,'g':1,'M':5,'maxIterations':20000,'run':i} for i in range(1,11)]
param = parameters[which]

N,j,h,M,g,maxIterations,run = param.values()
psiTarget = ed.exactDiag(N,j,h,g)[2].reshape(tuple([2]*N))

approxStateGD = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=True)[1:]

with open(f'approxStateGD{run}.pkl','wb') as f:
	pickle.dump(approxStateGD,f)