import numpy as np
import BrickWall_51 as bw
import ExactDiag_adam as ed
import plots_9 as plts
import pickle
import sys

N = 6
jA,hA,gA = 1,1,0 #integrable not at phase transition
jB,hB,gB = 1,1.5,0 #integrable at phase transition
jC,hC,gC = 1,1,1 #general non integrable
exactD = ed.exactDiagSparse(N, jC, hC,gC)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = np.array(exactD[0].todense())
layers = [1,2,3]

#Testing
# circuit = bw.BrickWallCircuit(N,3, gatesRandomFlag=False)
# circuitOpt = circuit.optimize(psiTarget,0.0001,5000,GD=False)[0]
# print(sys.getsizeof(circuit))
# print(sys.getsizeof(circuitOpt.computeUsingTensorDot()))
# print(sys.getsizeof(circuitOpt))
#plts.plotOvelap_sweeps3(approxState,'0.5_8_5_5000_GD_Nich')

# plotting correlation functions
#approxStates = [bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 5000,GD=False)[0].computeUsingTensorDot() for M in layers]
# plts.plotEnergy(psiTarget,jB,hB,gB,approxStates, exactE, H)
# plts.plotOvelap(psiTarget,jB,hB,gB,approxStates)
#plts.plotS(psiTarget,jC,hC,gC,approxStates,layers)
# plts.plotMatrixI(psiTarget,jB,hB,gB,approxStates,layers)
# plts.plotJ(psiTarget,jB,hB,gB,approxStates,layers)
#plts.plotJ(psiTarget,jB,hB,gB,approxStates,layers,log=True)

#approxStatesP = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 500,GD=False)[1:] for i in range(10)] for M in layers]
#approxStatesGD = [[bw.BrickWallCircuit(N,M,gatesRandomFlag=False).optimize(psiTarget, 0.0001, 500,GD=True)[1:] for i in range(10)] for M in layers]
# plts.plotOvelap_sweeps1(N,jC, hC,gC,layers,approxStatesP, approxStatesGD,GDvsPolar=True)




#plotting signature
#plts.plotOvelap_sweeps2([[[],[],[]],[[],[],[]],[[],[],[]]], {'type':'Models','items':['A','B','C'],'fixed':[N,5],'optimization':'Polar'})

#Final Plotting
approxStatesRand = []
approxStatesId = []
approxStatesGD,approxStatesGD8, approxStatesGD14 = [], [], []
approxStatesP, approxStatesP8, approxStatesP14 = [], [], []
approxStatesModel = []
approxStatesM = []
approxStatesN = []

for i in range(1,11):
	with open(f'pklFiles/testingOpt/approxStateRand14{i}.pkl','rb') as f:
		approxStatesRand.append(pickle.load(f))
	with open(f'pklFiles/testingOpt/approxStateId14{i}.pkl','rb') as f:
		approxStatesId.append(pickle.load(f))
	with open(f'pklFiles/testingOpt/approxStatePolar14{i}.pkl','rb') as f:
		approxStatesP14.append(pickle.load(f))
	with open(f'pklFiles/testingOpt/approxStateGD14_eta_linear_decrease{i}.pkl','rb') as f:
		approxStatesGD14.append(pickle.load(f))
	with open(f'pklFiles/testingOpt/approxStatePolar8{i}.pkl','rb') as f:
		approxStatesP8.append(pickle.load(f))
	with open(f'pklFiles/testingOpt/approxStateGD8_eta_Nich{i}.pkl','rb') as f:
		approxStatesGD8.append(pickle.load(f))
	
approxStatesRand = [approxStatesRand]
approxStatesId = [approxStatesId]
approxStatesGD = [approxStatesGD8]
approxStatesP = [approxStatesP8]

with open(f'pklFiles/Comparing/approxStateModel110_Polar.pkl','rb') as f:
		approxStatesModel.append(pickle.load(f))
with open(f'pklFiles/Comparing/approxStateModel11.50_Polar.pkl','rb') as f:
		approxStatesModel.append(pickle.load(f))
with open(f'pklFiles/Comparing/approxStateModel111_Polar.pkl','rb') as f:
		approxStatesModel.append(pickle.load(f))
	
for i in [3,4,6,7]:
	with open(f'pklFiles/Comparing/approxStateM{i}_Polar.pkl','rb') as f:
		approxStatesM.append(pickle.load(f))
approxStatesM.insert(2,approxStatesModel[2])

with open(f'pklFiles/Comparing/approxStateN8_Polar.pkl','rb') as f:
		approxStatesN.append(pickle.load(f))
with open(f'pklFiles/Comparing/approxStateN10_Polar.pkl','rb') as f:
		approxStatesN.append(pickle.load(f))
with open(f'pklFiles/Comparing/approxStateN12_Polar.pkl','rb') as f:
		approxStatesN.append(pickle.load(f))
approxStatesN.append(approxStatesModel[2])

compareModelSig = {'type':'Model','items':['1,1,0','1,1.5,0','1,1,1'],'fixed':[14,5],'optimization':'Polar'}
compareNSig = {'type':'N','items':[8,10,12,14],'fixed':[111,5],'optimization':'Polar'}
compareMSig1 = {'type':'M','items':[3,5,7],'fixed':[111,14],'optimization':'Polar'}



#plts.plotOvelap_sweeps1(14,1,1,1,[5],approxStatesRand, approxStatesId,GDvsPolar=False)
#plts.plotOvelap_sweeps1('8', 1, 1, 1, [5], approxStatesP, approxStatesGD,GDvsPolar=True)
#plts.plotOvelap_sweeps3(approxStatesGD[0][1],'GDOptimization_111_14_5_eta_linear_decrease')
plts.plotOvelap_sweeps2(approxStatesModel, compareModelSig)
#plts.plotOvelap_sweeps2(approxStatesN, compareNSig)
#plts.plotOvelap_sweeps2(approxStatesM[::2], compareMSig1,i='_110')


















