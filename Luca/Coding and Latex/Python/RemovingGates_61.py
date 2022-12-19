import BrickWall_51 as bw
import numpy as np

circuit = bw.BrickWallCircuit(8, 10)
psiTarget = np.array([1 for i in range(2**circuit.N)]).reshape(tuple([2]*circuit.N))
psiCheck = circuit.computeUsingTensorDot()

#only for checking purposes
def splitCircuit(splitLayer):
	nrGatesTillSplit = int(np.floor(circuit.N/2)*np.ceil(splitLayer/2)+np.floor((circuit.N-1)/2)*np.floor(splitLayer/2))

	firstHalfCircuit = bw.BrickWallCircuit(circuit.N, splitLayer,gates = circuit.gates[0:nrGatesTillSplit])
	secondHalfCircuit = bw.BrickWallCircuit(circuit.N, circuit.M - splitLayer,psiIn = np.conjugate(psiTarget),reverseOrder=1, gates=circuit.gates[nrGatesTillSplit:])

	return firstHalfCircuit, secondHalfCircuit

def removeGate(indexLayer,indexRelativeToLayer):
	nrGatesTillSplit = int(np.floor(circuit.N/2)*np.ceil(indexLayer/2)+np.floor((circuit.N-1)/2)*np.floor(indexLayer/2))
	nrGatesOnLayer = int(np.floor((circuit.N-indexLayer%2)/2))
	indexOfGate = nrGatesTillSplit + indexRelativeToLayer
	gatesWithQubits = circuit.gatesWithQubitsIndices()
	#print(gatesWithQubits)
	qubitsOfGate = gatesWithQubits[indexOfGate][1], gatesWithQubits[indexOfGate][2]
	qubitsToContract = [qubit for qubit in range(circuit.N) if qubit not in qubitsOfGate ]
	#print(qubitsToContract)
	firstHalfGatesWithQubits =  gatesWithQubits[:nrGatesTillSplit+nrGatesOnLayer][:indexOfGate] + gatesWithQubits[:nrGatesTillSplit+nrGatesOnLayer][indexOfGate+1:]
	#print(firstHalfGatesWithQubits)

	firstHalfCircuit = bw.BrickWallCircuit(circuit.N, indexLayer+1,gates = firstHalfGatesWithQubits) #This is not quite a brick wall since one gate is missing, however all we need is to use computeUsingTensorDot method
	secondHalfCircuit = bw.BrickWallCircuit(circuit.N, circuit.M - indexLayer-1,psiIn = np.conjugate(psiTarget),reverseOrder=1, gates=circuit.gates[nrGatesTillSplit+nrGatesOnLayer:])
	#print(secondHalfCircuit.gatesWithQubitsIndices(circuit.M))

	#Care in how we take tensor dot between the two halves to get indices in correct places to make life easier when we add gates back 
	E = np.tensordot(secondHalfCircuit.computeUsingTensorDot(MOriginal = circuit.M),firstHalfCircuit.computeUsingTensorDot(gatesWithQubitsIndices = firstHalfCircuit.gates),axes = (qubitsToContract,qubitsToContract)) #4 legs
	return E, circuit.gates[indexOfGate] #return gate removed only for checking purposes

#checks
overlap1 = np.tensordot(circuit.computeUsingTensorDot(),np.conjugate(psiTarget),circuit.N)
print(overlap1)

firstHalfCircuit, secondHalfCircuit = splitCircuit(2)
overlap2 = np.tensordot(firstHalfCircuit.computeUsingTensorDot(),secondHalfCircuit.computeUsingTensorDot(MOriginal = circuit.M),circuit.N)
print(overlap2)

#putting gate back should give same as overlap1 and overlap2
E, gate = removeGate(1,2)
print(np.tensordot(E, gate,4))


	
