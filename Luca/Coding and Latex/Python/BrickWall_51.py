import numpy as np
from functools import reduce
from scipy.stats import unitary_group as U
from scipy.linalg import expm

class BrickWallCircuit:
	def __init__(self,N,M,psiIn = None,reverseOrder = 0,gates = None,gatesRandomFlag = False):
		self.N = N
		self.M = M
		self.reverseOrder = reverseOrder
		self.nrGates = int(np.floor(N/2)*np.ceil(M/2)+np.floor((N-1)/2)*np.floor(M/2))

		if gates is None:
			if gatesRandomFlag: 
				gates = [U.rvs(4).reshape(2,2,2,2) for i in range(self.nrGates)]
			else: #make random matrix closer to identity
				epsilon = 0.01
				gates = []
				for i in range(self.nrGates):
					R = np.random.rand(4,4) #U.rvs(4)
					M = np.eye(4)+epsilon*R
					H = (M+np.conjugate(np.transpose(M)))/2
					gates.append(expm(-(1j)*H).reshape(2,2,2,2))
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

	def removeGate(self ,psiTarget,indexLayer,indexRelativeToLayer):
		nrGatesTillSplit = int(np.floor(self.N/2)*np.ceil(indexLayer/2)+np.floor((self.N-1)/2)*np.floor(indexLayer/2))
		nrGatesOnLayer = int(np.floor((self.N-indexLayer%2)/2))
		indexOfGate = nrGatesTillSplit + indexRelativeToLayer
		gatesWithQubits = self.gatesWithQubitsIndices()
		#print(gatesWithQubits)
		qubitsOfGate = gatesWithQubits[indexOfGate][1], gatesWithQubits[indexOfGate][2]
		qubitsToContract = [qubit for qubit in range(self.N) if qubit not in qubitsOfGate ]
		#print(qubitsToContract)
		firstHalfGatesWithQubits =  gatesWithQubits[:nrGatesTillSplit+nrGatesOnLayer][:indexOfGate] + gatesWithQubits[:nrGatesTillSplit+nrGatesOnLayer][indexOfGate+1:]
		#print(firstHalfGatesWithQubits)

		firstHalfCircuit = BrickWallCircuit(self.N, indexLayer+1,gates = firstHalfGatesWithQubits) #This is not quite a brick wall since one gate is missing, however all we need is to use computeUsingTensorDot method
		secondHalfCircuit = BrickWallCircuit(self.N, self.M - indexLayer-1,psiIn = np.conjugate(psiTarget),reverseOrder=1, gates=self.gates[nrGatesTillSplit+nrGatesOnLayer:])
		#print(secondHalfCircuit.gatesWithQubitsIndices(self.M))

		#Care in how we take tensor dot between the two halves to get indices in correct places to make life easier when we add gates back 
		E = np.tensordot(secondHalfCircuit.computeUsingTensorDot(MOriginal = self.M),firstHalfCircuit.computeUsingTensorDot(gatesWithQubitsIndices = firstHalfCircuit.gates),axes = (qubitsToContract,qubitsToContract)) #4 legs
		return E, self.gates[indexOfGate] #return gate removed only for checking purposes

	def optimize(self,psiTarget,minPerChange, maxCycles):
		cycles = 0
		breakFlag = False
		overlapArray = []
		stoppingCriteria1Hit = False
		stoppingCriteria2Hit = False
		while True: #keep going through cycles until desired accuracy is reached, this simulates a do-while loop
			oldOverlap = np.abs(np.tensordot(self.computeUsingTensorDot(),np.conjugate(psiTarget),self.N))
			oldError = 1-oldOverlap
			for indexLayer in range(self.M): #iterate through layers
				nrGatesOnLayer = int(np.floor((self.N-indexLayer%2)/2))
				for gateIndex in range(nrGatesOnLayer): #iterate through gates on that layer
					E, gateRm = self.removeGate(psiTarget,indexLayer,gateIndex)
					#E_new = gateRm + 0.5*E
					W, sigma, Vdagger = np.linalg.svd(np.conjugate(E.reshape(4,4)))
					newGate = np.matmul(W,Vdagger).reshape(2,2,2,2) #get the new gate that will maximize the fidelity

					oldGateOverlap = np.abs(np.tensordot(E,gateRm,4)) #overap with old gate
					newGateOverlap = np.abs(np.tensordot(E,newGate,4)) #overlap with new gate
					#print(oldGateOverlap,newGateOverlap)

					if newGateOverlap < oldGateOverlap and np.abs(newGateOverlap-oldGateOverlap)>10**(-6):
						raise Exception(f'overlap decreased, something went wrong at cycle {cycles+1}')
			
					self.gates = [newGate if (gate == gateRm).all() else gate for gate in self.gates] #updates gates with the new gate added instead of old one
					if np.abs(newGateOverlap-1) < 10**(-8):
						breakFlag = True
						print("numerical precision reached!")
						break
				if breakFlag: 
					break

			overlapArray.append(newGateOverlap)
			changeInOverlap = newGateOverlap - oldOverlap #changeInOverlap at end of cycle
			percentageChange = changeInOverlap/oldError #percentage change in error = 1-overlap
			newError = 1-newGateOverlap
			cycles += 1

			if percentageChange < minPerChange and not(stoppingCriteria1Hit): #note when percentage change criteria was hit
				criteria1 = (cycles,newGateOverlap)
				stoppingCriteria1Hit = True
			if breakFlag and not(stoppingCriteria2Hit): #note if numerical accuracy reached 
				criteria2 = (cycles,newGateOverlap)
				stoppingCriteria2Hit = True

			if cycles>=maxCycles:
				break
			# if (percentageChange < minPerChange and newError<0.1) or cycles > maxCycles or breakFlag:
			# 	break
		#print(cycles, percentageChange,stoppingCriteria1Hit,stoppingCriteria2Hit)
		return self.computeUsingTensorDot(), np.array(overlapArray), criteria1 if 'criteria1' in locals() else None, criteria2 if 'criteria2' in locals() else None



