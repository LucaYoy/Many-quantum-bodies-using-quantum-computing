import numpy as np
import sys
#import BrickWall_51 as bw
import ExactDiag_21 as ed
import plots_9 as plts
#import Entropy as en
#import matplotlib.pyplot as plt


which = int(sys.argv[1])

parameters = [{'N':6,'j':1,'h':1,'M':[1,2,3],'maxIterations':1000,'runs':10}, {'N':6,'j':1,'h':1.5,'M':[1,2,3],'maxIterations':1000,'runs':10}]
param = parameters[which]

N,j,h,layers,maxIterations,runs = param.values()
psiTarget = ed.exactDiag(N, j, h)[2].reshape(tuple([2]*N))
plts.plotOvelap_sweeps(psiTarget, j, h, layers, maxIterations, runs)
#p = f"N = {str(param['N'])} M = {str(param['M'])} j = {str(param['j'])} h = {str(param['h'])}"
