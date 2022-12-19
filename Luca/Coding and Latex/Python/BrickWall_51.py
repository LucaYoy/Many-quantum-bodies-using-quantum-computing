import numpy as np
from functools import reduce
from scipy.stats import unitary_group as U

class BrickWallCircuit:
	def __init__(self,N,M,psiIn = None,reverseOrder = 0,gates = None):
		self.N = N
		self.M = M
		self.gates = gates
		self.reverseOrder = reverseOrder
		self.nrGates = int(np.floor(N/2)*np.ceil(M/2)+np.floor((N-1)/2)*np.floor(M/2))

		if gates is None: 
			gates = [U.rvs(4).reshape(2,2,2,2) for i in range(self.nrGates)]
		self.gates = gates

		if psiIn is None:
			psi = np.zeros(2**N)
			psi[0]  = 1
			psi = psi.reshape(tuple([2]*N))
			psiIn = psi
		self.psiIn = psiIn
		
	def gatesWithQubitsIndices(self, MOriginal = 0): #MOriginal only needed when we want to reverse order, since we need it in order to determine if we start on an odd or even layer, otherwise its value its irrelevant
		counter = 0
		gatesWithQubitsIndices = []
		layerStart = self.reverseOrder and (MOriginal+1)%2
		gates = self.gates[::(-1)**self.reverseOrder]

		for i in range(layerStart,self.M+layerStart): #decorate gates with qubit numbers on which they act
			gatesSlice = gates[counter:counter + int(np.floor((self.N-i%2)/2))]
			gatesWithQubitsIndices += [(gate,j,j+1) for gate, j in zip(gatesSlice[::(-1)**self.reverseOrder], range(i%2,self.N-1,2))]
			counter += int(np.floor((self.N-i%2)/2))
		return gatesWithQubitsIndices

	#if we rverse order then we need to contract [0,1] indices of gates
	def tensordotPsiWithTwoQubitGate(self,psi,twoQubitGateWithIndices): return np.moveaxis(np.tensordot(twoQubitGateWithIndices[0],psi,axes = ([2*(1-self.reverseOrder),2*(1-self.reverseOrder)+1],[twoQubitGateWithIndices[1],twoQubitGateWithIndices[2]])),[0,1],[twoQubitGateWithIndices[1],twoQubitGateWithIndices[2]])

	#allow for custom addition of gates with qubit indices needed for when we remove a gate, otherwise if no argument added just use the inbuild method to calculate these
	def computeUsingTensorDot(self, gatesWithQubitsIndices = None, MOriginal = 0):
		if gatesWithQubitsIndices is None: 
			gatesWithQubitsIndices = self.gatesWithQubitsIndices(MOriginal)
		return reduce(self.tensordotPsiWithTwoQubitGate,gatesWithQubitsIndices,self.psiIn)