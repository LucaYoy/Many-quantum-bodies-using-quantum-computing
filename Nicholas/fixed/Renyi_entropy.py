import numpy as np

def compute_renyi_entropy(A, psi, alpha):
    # Find number of qubits
    qubits = len(psi.shape)
    n = len(A)
	  
    # Find which qubits are to be contracted
    contracted_qubits = [i for i in range(qubits) if i not in A]
    # Find the partial state
    partial_state = np.tensordot(psi, psi.conj(),
                                 axes=(contracted_qubits, contracted_qubits))

    partial_state = partial_state.reshape((2**n, 2**n))
    # Find the eigenvalues of the matrix
    eigenvalues,_ = np.linalg.eigh(partial_state)
    # Remove any eigenvalues which arise due to rounding errors
    eigenvalues = np.array([eigenvalue for eigenvalue in eigenvalues if eigenvalue>10**(-12)])
    
    # Generalize finding the entropy
    # von Neumann entropy
    if alpha == 1:
        entropy = -np.sum(eigenvalues * np.log(eigenvalues))
    # Renyi entropy    
    else: 
        entropy = (1 / (1 - alpha)) * np.log(np.sum(eigenvalues**alpha))
                                              
    return entropy