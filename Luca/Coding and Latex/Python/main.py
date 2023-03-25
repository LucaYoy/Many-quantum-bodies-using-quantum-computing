import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import plots_9 as plts

N = 6
j,h,g = 1,1.5,0
exactD = ed.exactDiag(N, j, h,g)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = exactD[0]

#circuit = bw.BrickWallCircuit(6,3, gatesRandomFlag=False)
#print(circuit.optimize(psiTarget,0.0001,500)[1:])
#psiTarget = (1/np.sqrt(2))*np.array([1,0,0,1]).reshape(2,2) #bell state

layers = [1,2,3]
approxStates = [bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 1000)[0] for M in layers]

plts.plotEnergy(psiTarget,j,h,g,approxStates, exactE, H)
plts.plotOvelap(psiTarget,j,h,g,approxStates)
plts.plotS(psiTarget,j,h,g,approxStates,layers)
plts.plotMatrixI(psiTarget,j,h,g,approxStates,layers)
plts.plotJ(psiTarget,j,h,g,approxStates,layers)
plts.plotJ(psiTarget,j,h,g,approxStates,layers,log=True)

# approxStatesRand = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=True).optimize(psiTarget, 0.0001, 1000)[1:] for i in range(10)] for M in layers]
# approxStatesId = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 1000)[1:] for i in range(10)] for M in layers]
# plts.plotOvelap_sweeps(psiTarget, j, h, approxStatesRand, approxStatesId,layers)