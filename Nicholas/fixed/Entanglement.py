# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:03:35 2023

@author: msyne
"""

import numpy as np
import BrickWall as bw
import matplotlib.pyplot as plt
import ExactDiagonalization as ed

def compute_entanglement(psi, n):
    """Splits the circuit at a chosen point and computes the entanglement
    entropy
    """
    # Check number of qubits 
    qubits = len(psi.shape)
    # Contract the qubits from n to the total number of qubits
    contracted_qubits = range(qubits)[n:]
    # Find the partial state
    partial_state = np.tensordot(psi, psi.conj(), 
                                 axes=(contracted_qubits,contracted_qubits))
    
    # Reshape the tensor into a matrix
    partial_state = partial_state.reshape((2**n,2**n))
    # Find the eigenvalues of the matrix
    eigenvalues,_ = np.linalg.eigh(partial_state)
    # Remove any eigenvalues which arise due to rounding errors
    eigenvalues = [eigenvalue for eigenvalue in eigenvalues if eigenvalue>10**(-12)]
    
    entropy = -np.sum(eigenvalues * np.log(eigenvalues))
    
    return entropy

def compute_entanglement2(psi,n):
    """Performs singular valued decomposition to compute entanglement
    """
    # Check number of qubits
    qubits = len(psi.shape)
    # Set initial wavefunction
    phi = psi    
    # Calculate reshaped matrix
    phi = phi.reshape(2**n, 2**(qubits - n))
    
    _,eigenvalues,_ = np.linalg.svd(phi)
    entropy = -np.sum(eigenvalues**2 * np.log(eigenvalues**2))
    
    return entropy

if __name__ == "__main__":

    Qubits = 8
    
    J = 3
    h = 4
    
    plt.figure(figsize=(9, 6))

    Circuit = bw.Circuit(Qubits, 3, J, h)
    psi = Circuit.brick_wall()
    
    entropies = []
    for n in range(0, Qubits+1):
        entropy = compute_entanglement(psi, n)
        entropies.append(entropy)
    
    plt.plot(range(Qubits+1), entropies, label=f'3 layers')
        
    phi = ed.exactDiagonalization(8, J, h)

    entropies_exact = []
    for n in range(0, Qubits):
        entropy = compute_entanglement(phi, n)
        entropies_exact.append(entropy)

    entropies_exact.append(0)
    plt.plot(range(Qubits+1), entropies_exact, label=f'psi target, J = {J}')
    
    plt.xlabel('i band')
    plt.ylabel('Entanglement entropy')
    plt.legend()
    plt.show()
   

    
    
    
    
    