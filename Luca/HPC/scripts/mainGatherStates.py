import numpy as np
import sys
import BrickWall_51 as bw
import ExactDiag_adam as ed
#import plots_9 as plts
import pickle
import time
#import Entropy as en
#import matplotlib.pyplot as plt

#sh file array 0-59
which = int(sys.argv[1])
parameters = []
#vary N,M,Model
for h,g in zip([1,1,1.5],[1,0,0]):
	for N in [8,10,12,14]:
		for M in [3,4,5,6,7]:
			parameters.append({'j':1,'h':h,'g':g,'N':N,'M':M})

#print(len(parameters))
param = parameters[which]

N,j,h,g,M,maxIterations = param['N'],param['j'],param['h'],param['g'],param['M'],100000

psiTarget = ed.exactDiagSparse(N,j,h,g)[2].reshape(tuple([2]*N))
t1 = time.time()
approxOptimizedCircuit = bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, maxIterations,GD=False)[0]
t2 = time.time()
print(f' {j}{h}{g}_{N}_{M} opt took {t2-t1}s')

with open(f'approxOptimizedCircuit{j}{h}{g}_{N}_{M}_.pkl','wb') as f:
	pickle.dump(approxOptimizedCircuit,f)