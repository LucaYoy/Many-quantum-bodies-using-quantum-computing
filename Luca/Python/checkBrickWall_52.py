import BrickWall_51 as bw
import numpy as np
from scipy.stats import unitary_group as U
import Quantum_circuit_via_kron_prod_41 as k

circuit = bw.BrickWallCircuit(4, 4)
psi = np.zeros(2**circuit.N)
psi[0]  = 1
U = [gate.reshape(4,4) for gate in circuit.gates]

solutionTD = circuit.computeUsingTensorDot()
print(solutionTD.flatten(),'\n -----')
solutionKN = k.computeCircuitGate(psi,k.computeSliceGate(circuit.N,(U[0],0,1),(U[1],2,3)),k.computeSliceGate(circuit.N,(U[2],1,2)),k.computeSliceGate(circuit.N,(U[3],0,1),(U[4],2,3)),k.computeSliceGate(circuit.N,(U[5],1,2)))
print(solutionKN,'\n -----')

#print (solutionTD == solutionKN) #why gives false??