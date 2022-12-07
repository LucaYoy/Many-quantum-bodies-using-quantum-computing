import numpy as np
import usefulGates as g
from functools import reduce

tensordotPsiWithTwoQubitGate = lambda psi,twoQubitGateWithIndices: np.moveaxis(np.tensordot(twoQubitGateWithIndices[0],psi,axes = ([2,3],[twoQubitGateWithIndices[1],twoQubitGateWithIndices[2]])),[0,1],[twoQubitGateWithIndices[1],twoQubitGateWithIndices[2]])

def computeAnyCircuitUsingTensorDot(psi,*gatesWithQubitsIndices): return reduce(tensordotPsiWithTwoQubitGate,gatesWithQubitsIndices,psi).flatten()

def brickWall(N,M,psi,*gates):
	counter = 0
	gatesWithQubitsIndices = []
	for i in range(M): #decorate gate in argument list with qubit numbers on which it, acts to make it suitable for use with above function
		gatesSlice = gates[counter:counter + int(np.floor((N-i%2)/2))]
		gatesWithQubitsIndices += [(gate,j,j+1) for gate, j in zip(gatesSlice, range(i%2,N-1,2))]
		counter += int(np.floor((N-i%2)/2))
	return computeAnyCircuitUsingTensorDot(psi,*gatesWithQubitsIndices)
