import numpy as np
import usefulGates as g
from functools import reduce

def computeLayerGate(n,*orderedGates):
	currentIndex = 0
	i = 0 
	gateToBeAdded = orderedGates[i] #gate with indices 
	startIndex = gateToBeAdded[1] #first and last qubits upon which gate acts 
	endIndex = gateToBeAdded[-1]
	i += 1 #pointer pointing at next gate to be added 
	layeredGate = []
	while currentIndex<n: #loop through qubits
		if currentIndex == startIndex: #add the current gate to the tensor product array if current qubit we are looking at is acted upon by the gate
			layeredGate.append(gateToBeAdded[0])
			currentIndex = endIndex + 1 #go to the next qubit after the ones that are acted by the gate
			if i>=len(orderedGates): #check if we finished with all the gates
				startIndex, endIndex = -1, -1
			else:
				gateToBeAdded = orderedGates[i] #look at next gate to be added 
				startIndex = gateToBeAdded[1]
				endIndex = gateToBeAdded[-1]
				i += 1 #increment pointer
		else: #if current qubit is not acted by any gate we add idenity to the tensor product list
			layeredGate.append(np.eye(2))
			currentIndex += 1

	return np.array(reduce(np.kron, layeredGate)) 

gate = computeLayerGate(4,(g.H,0),(g.H,1),(g.RXX,2,3))
print(gate)

computeCircuitGate = lambda *layeredGates: reduce(lambda mat1,mat2: np.matmult(mat1,mat2),layeredGates.reverse())  
