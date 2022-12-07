import BrickWall_51 as bw
import numpy as np
from scipy.stats import unitary_group as U
import Quantum_circuit_via_kron_prod_41 as k

N = 4
M = 4
psi = np.zeros(2**N)
psi[0]  = 1
psiReshaped = psi.reshape(tuple([2]*N))

U = [U.rvs(4) for i in range(6)]
UReshaped = list(map(lambda u: u.reshape(2,2,2,2), U))

solutionTD = bw.brickWall(N, M, psiReshaped,UReshaped[0],UReshaped[1],UReshaped[2],UReshaped[3],UReshaped[4],UReshaped[5])
print(solutionTD)
solutionKN = k.computeCircuitGate(psi,k.computeSliceGate(N,(U[0],0,1),(U[1],2,3)),k.computeSliceGate(N,(U[2],1,2)),k.computeSliceGate(N,(U[3],0,1),(U[4],2,3)),k.computeSliceGate(N,(U[5],1,2)))
print(solutionKN)
solutionTD2 = bw.computeAnyCircuitUsingTensorDot(psiReshaped,(UReshaped[0],0,1),(UReshaped[1],2,3),(UReshaped[2],1,2),(UReshaped[3],0,1),(UReshaped[4],2,3),(UReshaped[5],1,2))
print(solutionTD2.flatten()) 

print (solutionTD == solutionKN) #why gives false??