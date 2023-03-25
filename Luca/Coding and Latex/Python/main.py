import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import plots_9 as plts

N = 6
j,h = 1,1.5
exactD = ed.exactDiag(N, j, h)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = exactD[0]

#circuit = bw.BrickWallCircuit(6,3, gatesRandomFlag=False)
#print(circuit.optimize(psiTarget,0.0001,500)[1:])
#psiTarget = (1/np.sqrt(2))*np.array([1,0,0,1]).reshape(2,2) #bell state

layers = [1,2,3]
# approxStates = [bw.BrickWallCircuit(N,M,gatesRandomFlag=True).optimize(psiTarget, 0.0001, 1000)[0] for M in layers]

# plts.plotEnergy(psiTarget, approxStates, exactE, H)
# plts.plotOvelap(psiTarget, approxStates)
# plts.plotS(psiTarget, approxStates,layers)
# plts.plotMatrixI(psiTarget, approxStates,layers)
# plts.plotJ(psiTarget, approxStates,layers)
# plts.plotJ(psiTarget, approxStates,layers,log=True)

approxStatesRand = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=True).optimize(psiTarget, 0.0001, 1000)[1:] for i in range(10)] for M in layers]
approxStatesId = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 1000)[1:] for i in range(10)] for M in layers]

plts.plotOvelap_sweeps(psiTarget, j, h, approxStatesRand, approxStatesId,layers)