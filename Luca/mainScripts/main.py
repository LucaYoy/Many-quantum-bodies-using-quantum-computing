import numpy as np
import BrickWall_51 as bw
import ExactDiag_adam as ed
import plots_9 as plts
import pickle

N = 12
jA,hA,gA = 1,1,0 #integrable not at phase transition
jB,hB,gB = 1,1.5,0 #integrable at phase transition
jC,hC,gC = 1,1,1 #general non integrable
exactD = ed.exactDiagSparse(N, jC, hC,gC)
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

approxStatesRand = []
approxStatesId = []
approxStatesGD = []
approxStatesModel = []
approxStatesM = []
approxStatesN = []

for i in range(1,11):
	with open(f'approxStateRand{i}.pkl','rb') as f:
		approxStatesRand.append(pickle.load(f))
	with open(f'approxStateId{i}.pkl','rb') as f:
		approxStatesId.append(pickle.load(f))
	with open(f'approxStateGD{i}.pkl','rb') as f:
		approxStatesGD.append(pickle.load(f))
	
	if i in [3,4,6,7]:
		with open(f'approxStateM{i}.pkl','rb') as f:
			approxStatesM.append(pickle.load(f))

approxStatesRand = [approxStatesRand]
approxStatesId = [approxStatesId]
approxStatesGD = [approxStatesGD]
approxStatesP = approxStatesId
approxStatesM.insert(2,approxStatesGD[0][0])

with open(f'approxStateModel110.pkl','rb') as f:
		approxStatesModel.append(pickle.load(f))
with open(f'approxStateModel11.50.pkl','rb') as f:
		approxStatesModel.append(pickle.load(f))
with open(f'approxStateModel111.pkl','rb') as f:
		approxStatesModel.append(pickle.load(f))

with open(f'approxStateN8.pkl','rb') as f:
		approxStatesN.append(pickle.load(f))
with open(f'approxStateN10.pkl','rb') as f:
		approxStatesN.append(pickle.load(f))
with open(f'approxStateN12.pkl','rb') as f:
		approxStatesN.append(pickle.load(f))
approxStatesN.append(approxStatesGD[0][0])

compareModelSig = {'type':'Models','items':['A','B','C'],'fixed':[14,5],'optimization':'GD'}
compareNSig = {'type':'N','items':[8,10,12,14],'fixed':[111,5],'optimization':'GD'}
compareMSig = {'type':'M','items':[3,4,5,6,7],'fixed':[111,14],'optimization':'GD'}



plts.plotOvelap_sweeps1(14,1,1,1,[5],approxStatesRand, approxStatesId,GDvsPolar=False)
plts.plotOvelap_sweeps1(14, 1, 1, 1, [5], approxStatesP, approxStatesGD,GDvsPolar=True)
plts.plotOvelap_sweeps2(approxStatesModel, compareModelSig)
plts.plotOvelap_sweeps2(approxStatesN, compareNSig)
plts.plotOvelap_sweeps2(approxStatesM, compareMSig)

















