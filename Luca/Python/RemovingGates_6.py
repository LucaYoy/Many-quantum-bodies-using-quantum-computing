import BrickWall_51 as bw
import numpy as np

circuit = bw.BrickWallCircuit(3,5)
psiTarget = np.array([1 for i in range(2**circuit.N)]).reshape(tuple([2]*circuit.N))
psiCheck = circuit.computeUsingTensorDot()

#only for checking purposes
def splitCircuit(splitLayer):
	nrGatesTillSplit = int(np.floor(circuit.N/2)*np.ceil(splitLayer/2)+np.floor((circuit.N-1)/2)*np.floor(splitLayer/2))

	firstHalfCircuit = bw.BrickWallCircuit(circuit.N, splitLayer,gates = circuit.gates[0:nrGatesTillSplit])
	secondHalfCircuit = bw.BrickWallCircuit(circuit.N, circuit.M - splitLayer,psiIn = np.conjugate(psiTarget),reverseOrder=1, gates=circuit.gates[nrGatesTillSplit:])

	return firstHalfCircuit, secondHalfCircuit

#checks
overlap1 = np.tensordot(circuit.computeUsingTensorDot(),np.conjugate(psiTarget),circuit.N)
print(overlap1)

firstHalfCircuit, secondHalfCircuit = splitCircuit(4)
overlap2 = np.tensordot(firstHalfCircuit.computeUsingTensorDot(),secondHalfCircuit.computeUsingTensorDot(MOriginal = circuit.M),circuit.N)
print(overlap2)

#putting gate back should give same as overlap1 and overlap2
E, gate = circuit.removeGate(psiTarget,2,0)
print(np.tensordot(E, gate,4))


	
