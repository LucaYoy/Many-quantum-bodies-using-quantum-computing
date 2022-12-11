import BrickWall_51 as bw
import numpy as np
from scipy.stats import unitary_group as U
import Quantum_circuit_via_kron_prod_41 as k

N = 4
M = 4
nrGates = int(np.ceil(M/2)*2+(M-np.ceil(M/2)))
psi = np.zeros(2**N)
psi[0]  = 1
psiReshaped = psi.reshape(tuple([2]*N))

U = [U.rvs(4) for i in range(nrGates)]
UReshaped = list(map(lambda u: u.reshape(2,2,2,2), U))

solutionTD = bw.brickWall(N, M, psiReshaped, UReshaped).flatten()
print(solutionTD,'\n -----')
solutionKN = k.computeCircuitGate(psi,k.computeSliceGate(N,(U[0],0,1),(U[1],2,3)),k.computeSliceGate(N,(U[2],1,2)),k.computeSliceGate(N,(U[3],0,1),(U[4],2,3)),k.computeSliceGate(N,(U[5],1,2)))
print(solutionKN,'\n -----')
solutionTD2 = bw.computeAnyCircuitUsingTensorDot(psiReshaped,[(UReshaped[0],0,1),(UReshaped[1],2,3),(UReshaped[2],1,2),(UReshaped[3],0,1),(UReshaped[4],2,3),(UReshaped[5],1,2)]).flatten()
print(solutionTD2, '\n -----') 

#print (solutionTD == solutionKN) #why gives false??