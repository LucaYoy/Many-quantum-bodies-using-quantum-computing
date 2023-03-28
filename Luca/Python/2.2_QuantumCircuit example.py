import numpy as np
import usefulGates as g

psi = np.zeros((2,2,2))
psi[0,0,0] = 1

def circuit0(psi):
	g.H = 1/np.sqrt(2)*np.array([[1,1],[1,-1]])
	CNOT = np.reshape(g.CNOT,(2,2,2,2))
	psi1 = np.tensordot(g.H,psi,(1,0))
	psi2 = np.tensordot(CNOT,psi1,((2,3),(0,1)))
	return np.tensordot(CNOT,psi2,((2,3),(1,2))).flatten()

print(circuit0(psi))