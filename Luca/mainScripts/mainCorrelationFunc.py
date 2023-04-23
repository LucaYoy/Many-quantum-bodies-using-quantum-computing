import numpy as np
import BrickWall_51 as bw
import ExactDiag_adam as ed
import plots_9 as plts
import pickle
import sys
import Entropy as en

N = 8
exactD = ed.exactDiagSparse(N, 1, 1,1)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = np.array(exactD[0].todense())
exactD = None
layers = [3,4,5,6,7]
bond = range(N+1)

#For N=14
entropies111 = []
EList = []
for layer in layers:
	with open(f'pklFiles/DB/approxOptimizedCircuit111_{N}_{layer}_.pkl','rb') as f:
		approxState = pickle.load(f).computeUsingTensorDot()
		enList=[]

		# for i in bond:
		# 	enList.append(en.S(range(1,i+1), approxState))

		approxState = approxState.flatten()
		energy = np.vdot(approxState,np.matmul(H,approxState))

		EList.append(energy)
		entropies111.append(enList)

#plts.plotS(psiTarget, 1, 1, 1, entropies111, layers)
plts.plotEnergy(psiTarget, 1, 1, 1, exactE, EList,layers, H)
