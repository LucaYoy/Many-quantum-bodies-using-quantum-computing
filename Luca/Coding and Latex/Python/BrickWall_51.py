import numpy as np
import usefulGates as g
from functools import reduce

def tensordotPsiWithTwoQubitGate(psi,twoQubitGateWithIndices): return np.moveaxis(np.tensordot(twoQubitGateWithIndices[0],psi,axes = ([2,3],[twoQubitGateWithIndices[1],twoQubitGateWithIndices[2]])),[0,1],[twoQubitGateWithIndices[1],twoQubitGateWithIndices[2]])

def computeAnyCircuitUsingTensorDot(psi, gatesWithQubitsIndices): return reduce(tensordotPsiWithTwoQubitGate,gatesWithQubitsIndices,psi)

def brickWall(N,M,psi, gates, startOddLayer = 0, reverseOrder = 0): #start loop over layers on odd layer if startOddLayer = 1, i.e starting with one gate on that layer
	counter = 0
	gatesWithQubitsIndices = []
	for i in range(startOddLayer,M+startOddLayer): #decorate gate in argument list with qubit numbers on which it, acts to make it suitable for use with above function
		gatesSlice = gates[counter:counter + int(np.floor((N-i%2)/2))]
		gatesWithQubitsIndices += [(gate,j,j+1) for gate, j in zip(gatesSlice[::(-1)**reverseOrder], range(i%2,N-1,2))]
		counter += int(np.floor((N-i%2)/2))
	#print(gatesWithQubitsIndices)
	return computeAnyCircuitUsingTensorDot(psi, gatesWithQubitsIndices)
