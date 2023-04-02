import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_adam as ed
#import plots_9 as plts
import pickle
import time
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-2
which = int(sys.argv[1])

parameters = [{'h':1,'g':0},{'h':1.5,'g':0},{'h':1,'g':1,}]
param = parameters[which]

N,j,h,g,M,maxIterations = 14,1,param['h'],param['g'],5,100000

psiTarget = ed.exactDiagSparse(N,j,h,g)[2].reshape(tuple([2]*N))
t1 = time.time()
approxStateModel = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=False)[1:]
t2 = time.time()
print(f'model {j}{h}{g} opt took {t2-t1}s')
with open(f'approxStateModel{j}{h}{g}_Polar.pkl','wb') as f:
	pickle.dump(approxStateModel,f)