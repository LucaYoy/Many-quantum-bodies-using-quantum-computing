# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:55:23 2023

@author: msyne
"""

import numpy as np
import BrickWall as bw
import ExactDiagonalization as ed
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.linalg import eigh

def entanglement_entropy(psi, A, B):
    """ Takes an input wavefunction and two sites,
    and returns the entanglement on the sites
    """
    
    # Check number of qubits
    qubits = len(psi.shape)
    
    # Indices of qubits not in A or B
    remaining_qubits = [i for i in range(qubits) if i not in [A,B]]

    # Contract the qubits not in A or B
    contracted_qubits = tuple(remaining_qubits)
    partial_state = np.tensordot(psi, psi.conj(), 
                                 axes=(contracted_qubits,contracted_qubits))
    
    partial_state = partial_state.reshape((2**2,2**2))
    
    # Find the eigenvalues of the matrix
    eigenvalues,_ = np.linalg.eigh(partial_state)
    # Remove any eigenvalues which arise due to rounding errors
    eigenvalues = [eigenvalue for eigenvalue in eigenvalues if eigenvalue>10**(-12)]
    
    entropy = -np.sum(eigenvalues * np.log(eigenvalues))
    
    return entropy, remaining_qubits
   
def mutual_information(psi):
    """Takes an input wavefunction, and finds the resulting entanglement entropy
    matrix
    """
    # Number of qubits
    qubits = len(psi.shape)
    
    # Initialize matrices
    entropy_matrix = np.zeros((qubits,qubits))
    abs_d = np.arange(1, qubits)
    sum_entropy = np.zeros_like(abs_d, dtype=float)
    
    # Iterate over all sites
    for A in range(qubits):
        for B in range(A + 1, qubits):
            entropy = entanglement_entropy(psi, A, B)
            # Assign each place in matrix its corresponding value
            entropy_matrix[A, B] = entropy
            entropy_matrix[B, A] = entropy   
            
            #print(f"A = {A} with B = {B}")
            
            # Calculate d
            d = abs(A - B)
            # Sum values and then move to next value of d
            if d <= abs_d[-1]:
                sum_entropy[d-1] += entropy
            
    return entropy_matrix, abs_d, sum_entropy



if __name__ == "__main__":
    
    Qubits = 8
    J = 1
    h = 1
    for Layers in range(1,4):
    
        Circuit = bw.Circuit(Qubits, Layers, J ,h)
        psi=Circuit.optimize_circuit(Qubits, 0.0001, False)[2]
            
        entropy_matrix1, abs_d, sum_entropy1 = mutual_information(psi)
        
        plt.plot(abs_d, sum_entropy1, '--o',  label=f'{Layers} layers')
    plt.xlabel('log(d)')
    plt.ylabel('log(J)')
    
    phi = ed.exactDiagonalization(Qubits, J, h)
        
    entropy_matrix, abs_d, sum_entropy = mutual_information(phi)
    plt.plot(abs_d, sum_entropy,'--o', label='Target state' )
    plt.legend()
    #plt.xscale('log')
    #plt.yscale('log')
    plt.show()
    
    p = entanglement_entropy(psi, 1, 1)
    
    #g = et1.compute_entanglement(psi, 1)

















    