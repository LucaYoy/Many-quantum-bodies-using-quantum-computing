import numpy as np

def computeEntropy(n,psiTarget):
	nrQubits = len(psiTarget.shape)
	qubitsToContract = range(nrQubits)[n:]
	rhoA = np.tensordot(psiTarget, np.conjugate(psiTarget), (qubitsToContract,qubitsToContract)) #partial state
	eigenvalues = np.linalg.eigh(rhoA.reshape((2**n,2**n)))[0] #eigenvalues of partial state
	eigenvalues = [eigenvalue for eigenvalue in eigenvalues if eigenvalue>10**(-12)]
	entropy = -np.sum(eigenvalues*np.log(eigenvalues))

	return entropy