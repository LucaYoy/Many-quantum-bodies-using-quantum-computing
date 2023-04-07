import numpy as np
import BrickWall_51 as bw
import ExactDiag_adam as ed
import plots_9 as plts
import pickle
import sys

N = 14
exactD = ed.exactDiagSparse(N, 1, 1,0)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = np.array(exactD[0].todense())
layers = [3,4,5,6,7]

#For N=14
approxStates110 = []
for layer in layers:
	with open(f'pklFiles/DB/approxOptimizedCircuit110_{N}_{layer}_.pkl','rb') as f:
		approxStates110.append(pickle.load(f).computeUsingTensorDot())
plts.plotS(psiTarget, 1, 1, 0, approxStates110, layers)
