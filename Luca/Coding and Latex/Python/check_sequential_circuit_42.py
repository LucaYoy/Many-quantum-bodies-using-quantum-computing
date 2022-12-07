import Quantum_circuit_via_kron_prod_41 as k
import Sequential_gates_circuit_3 as sc
import usefulGates as g
import numpy as np
import BrickWall_51 as bw

n = 4
CNOT = np.reshape(g.CNOT,(2,2,2,2))
H = np.reshape(g.H,(2,2))
RXX = np.reshape(g.RXX,(2,2,2,2))
psi = np.zeros(2**n)
psi[0] = 1

solution1 = k.computeCircuitGate(psi,k.computeSliceGate(n,(g.CNOT,2,3)),k.computeSliceGate(n,(g.CNOT,1,2)),k.computeSliceGate(n,(g.CNOT,0,1)),k.computeSliceGate(n,(g.H,0)))
solution2 = sc.sequentialCircuit(n,H,CNOT,CNOT,CNOT) #first example

solution3 = k.computeCircuitGate(psi,k.computeSliceGate(n,(g.H,0)),k.computeSliceGate(n,(g.CNOT,0,1)),k.computeSliceGate(n,(g.CNOT,1,2)),k.computeSliceGate(n,(g.RXX,1,2)),k.computeSliceGate(n,(g.CNOT,2,3)))
solution4 = sc.sequentialCircuit(n,H,CNOT,CNOT,CNOT, extraGateAtLayer=(RXX,2)) #second example

print(solution1 == solution2,'\n',solution3 == solution4)
