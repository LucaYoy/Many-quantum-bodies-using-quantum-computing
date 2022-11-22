import numpy as np

psi = np.zeros((2,2,2))
psi[0,0,0] = 1

def circuit0(psi):
	hadamard = 1/np.sqrt(2)*np.array([[1,1],[1,-1]])
	CNOT = np.reshape([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],(2,2,2,2))
	psi1 = np.tensordot(hadamard,psi,(1,0))
	psi2 = np.tensordot(CNOT,psi1,((2,3),(0,1)))
	return np.tensordot(CNOT,psi2,((2,3),(1,2))).flatten()

print(circuit0(psi))