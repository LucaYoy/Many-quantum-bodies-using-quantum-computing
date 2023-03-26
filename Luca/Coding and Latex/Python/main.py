import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import plots_9 as plts
import pickle
import tracemalloc

N = 12
jA,hA,gA = 1,1,0 #integrable not at phase transition
jB,hB,gB = 1,1.5,0 #integrable at phase transition
jC,hC,gC = 1,1,1 #general non integrable
exactD = ed.exactDiag(N, jC, hC,gC)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = exactD[0]
layers = [5]


#circuit = bw.BrickWallCircuit(N,5, gatesRandomFlag=False)
#circuit.optimize(psiTarget,0.0001,10000,GD=False)[2:]

# psiTarget = (1/np.sqrt(2))*np.array([1,0,0,1]).reshape(2,2) #bell state

# approxStates = [bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 1000)[0] for M in layers]
# plts.plotEnergy(psiTarget,j,h,g,approxStates, exactE, H)
# plts.plotOvelap(psiTarget,j,h,g,approxStates)
# plts.plotS(psiTarget,j,h,g,approxStates,layers)
# plts.plotMatrixI(psiTarget,j,h,g,approxStates,layers)
# plts.plotJ(psiTarget,j,h,g,approxStates,layers)
# plts.plotJ(psiTarget,j,h,g,approxStates,layers,log=True)

#approxStatesP = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 500,GD=False)[1:] for i in range(10)] for M in layers]
#approxStatesGD = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 500,GD=True)[1:] for i in range(10)] for M in layers]

# with open('approxStatesP.pkl','wb') as f:
# 	pickle.dump(approxStatesP, f)

# with open('approxStatesGD.pkl','wb') as f:
# 	pickle.dump(approxStatesGD, f)

# with open('approxStatesId.pkl','rb') as f:
# 	approxStatesP = pickle.load(f)

# with open('approxStatesGD.pkl','rb') as f:
# 	approxStatesGD = pickle.load(f)

# plts.plotOvelap_sweeps1(N,jC, hC,gC,layers,approxStatesP, approxStatesGD,GDvsPolar=True)




#plotting signature
#plts.plotOvelap_sweeps2([[[],[],[]],[[],[],[]],[[],[],[]]], {'type':'Models','items':['A','B','C'],'fixed':[N,5],'optimization':'Polar'})