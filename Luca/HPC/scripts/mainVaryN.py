import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_adam as ed
#import plots_9 as plts
import pickle
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-2
which = int(sys.argv[1])

parameters = [{'N':8},{'N':10},{'N':12}]
param = parameters[which]

N,j,h,g,M,maxIterations = param['N'],1,1,1,5,100000
psiTarget = ed.exactDiagSparse(N,j,h,g)[2].reshape(tuple([2]*N))

approxStateN = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=False)[1:]

with open(f'approxStateN{N}_Polar.pkl','wb') as f:
	pickle.dump(approxStateN,f)