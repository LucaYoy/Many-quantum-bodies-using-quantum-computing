import numpy as np
import usefulGates as g
from functools import reduce

def computeSliceGate(n,*orderedGates):
	currentIndex = 0
	i = 0 
	gateToBeAdded = orderedGates[i] #gate with indices 
	startIndex = gateToBeAdded[1] #first and last qubits upon which gate acts 
	endIndex = gateToBeAdded[-1]
	i += 1 #pointer pointing at next gate to be added 
	sliceGate = []
	while currentIndex<n: #loop through qubits
		if currentIndex == startIndex: #add the current gate to the tensor product array if current qubit we are looking at is acted upon by the gate
			sliceGate.append(gateToBeAdded[0])
			currentIndex = endIndex + 1 #go to the next qubit after the ones that are acted by the gate
			if i>=len(orderedGates): #check if we finished with all the gates
				startIndex, endIndex = -1, -1
			else:
				gateToBeAdded = orderedGates[i] #look at next gate to be added 
				startIndex = gateToBeAdded[1]
				endIndex = gateToBeAdded[-1]
				i += 1 #increment pointer
		else: #if current qubit is not acted by any gate we add idenity to the tensor product list
			sliceGate.append(np.eye(2))
			currentIndex += 1

	return np.array(reduce(np.kron, sliceGate)) 

computeCircuitGate = lambda inputPsi,*sliceGates: reduce(lambda mat1,mat2: np.matmul(mat2,mat1),sliceGates,inputPsi)
