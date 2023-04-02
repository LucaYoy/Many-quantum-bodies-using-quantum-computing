import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_adam as ed
#import plots_9 as plts
import pickle
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-3
which = int(sys.argv[1])

parameters = [{'M':3,},{'M':4},{'M':6},{'M':7}]
param = parameters[which]

N,j,h,g,M,maxIterations = 14,1,1,1,param['M'],100000
psiTarget = ed.exactDiagSparse(N,j,h,g)[2].reshape(tuple([2]*N))

approxStateM = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=False)[1:]

with open(f'approxStateM{M}_Polar.pkl','wb') as f:
	pickle.dump(approxStateM,f)