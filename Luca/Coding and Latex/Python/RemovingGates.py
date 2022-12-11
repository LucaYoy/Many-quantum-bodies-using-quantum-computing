import BrickWall_51 as bw
import numpy as np
from scipy.stats import unitary_group as U

N = 4
M = 5
nrGates = int(np.ceil(M/2) + M)
psi1 = np.zeros(2**N)
psi1[0]  = 1
psi1 = psi1.reshape(tuple([2]*N))
psi2 = np.array([1 for i in range(2**N)]).reshape(tuple([2]*N))
#print(psi1,psi2)
U = [U.rvs(4).reshape(2,2,2,2) for i in range(nrGates)]

overlap = np.tensordot(bw.brickWall(N, M, psi1, U),np.conjugate(psi2),N)
print(overlap)

#split at layer 1
splitLayer = 0
nrGatesTillSplit = int(np.ceil(splitLayer/2) + splitLayer)
nrGatesAfterSplit = nrGates - nrGatesTillSplit
firstHalf = bw.brickWall(N, splitLayer, psi1, U[0:nrGatesTillSplit])
print(firstHalf)
secondHalf = bw.brickWall(N, M - splitLayer, np.conjugate(psi2),U[::-1][0:nrGatesAfterSplit], (M+1)%2 , 1)
overlap2 = np.tensordot(firstHalf,secondHalf,N)
print(overlap2)
#print(U[::-1][0:nrGatesAfterSplit])

