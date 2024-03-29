import numpy as np
import ExactDiag_21 as ed

def S(A,psiTarget):
	nrQubits = len(psiTarget.shape)
	n = len(A)

	qubitsToContract = list(set(range(nrQubits)) - set(np.array(A)-1))
	rhoA = np.tensordot(psiTarget, np.conjugate(psiTarget), (qubitsToContract,qubitsToContract)) #partial state
	eigenvalues = np.linalg.eigh(rhoA.reshape((2**n,2**n)))[0] #eigenvalues of partial state
	eigenvalues = [eigenvalue for eigenvalue in eigenvalues if eigenvalue>10**(-12)]
	entropy = -np.sum(eigenvalues*np.log(eigenvalues))

	return entropy

def I(A,B,psiTarget): return S(A, psiTarget) + S(B, psiTarget) - S(list(set(A)|set(B)), psiTarget)

def J(d,psiTarget):
	N = len(psiTarget.shape)
	return np.sum([I([i],[j],psiTarget) for i in range(1,N+1) for j in range(1,N+1) if abs(i-j)==d])/2

def matrixI(psiTarget):
	nrQubits = len(psiTarget.shape)
	return [[I([i],[j],psiTarget) for j in range(1,nrQubits+1)] for i in range(1,nrQubits+1)]
