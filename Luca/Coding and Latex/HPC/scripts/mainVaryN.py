import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_21 as ed
#import plots_9 as plts
import pickle
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-2
which = int(sys.argv[1])

parameters = [{'N':8,'j':1,'h':1,'g':1,'M':5,'maxIterations':20000},{'N':10,'j':1,'h':1,'g':1,'M':5,'maxIterations':20000},{'N':12,'j':1,'h':1,'g':1,'M':5,'maxIterations':20000}]
param = parameters[which]

N,j,h,M,g,maxIterations = param.values()
psiTarget = ed.exactDiag(N,j,h,g)[2].reshape(tuple([2]*N))

approxStateN = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=True)[1:]

with open(f'approxStateN{N}.pkl','wb') as f:
	pickle.dump(approxStateN,f)