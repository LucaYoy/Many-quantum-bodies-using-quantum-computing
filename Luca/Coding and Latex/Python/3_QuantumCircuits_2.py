import numpy as np

#useful gates
H = 1/np.sqrt(2)*np.array([[1,1],[1,-1]])
CNOT = np.reshape([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],(2,2,2,2))
RXX = np.reshape(np.cos(np.pi/8)*np.identity(4)-1j*np.sin(np.pi/8)*np.kron(np.array([[0,1],[0,-1]]),np.array([[0,1],[0,-1]])),(2,2,2,2))

def circuit(n, *gates, extraGateAtLayer = (None,None)):
	psi = np.zeros(2**n)
	psi[0] = 1
	psi = psi.reshape(tuple([2]*n))
	#print(extraGateAtLayer)

	psi = np.tensordot(gates[0],psi, (1,0)) #first gate is single qubit
	for i in range(1,n):
		psi = np.moveaxis(np.tensordot(gates[i],psi,axes = ([2,3],[i-1,i])),[0,1],[i-1,i]) #following gates are 2 qubit neighbouring gates starting from 1st qubit.
		if i == extraGateAtLayer[1]: 
			psi = np.moveaxis(np.tensordot(extraGateAtLayer[0],psi,axes = ([2,3],[i-1,i])),[0,1],[i-1,i])

	return psi.flatten() 

print(circuit(4,H,CNOT,CNOT,CNOT),'\n') #first example in meeting
print(circuit(4,H,CNOT,CNOT,CNOT,extraGateAtLayer=(RXX,2))) #second example
