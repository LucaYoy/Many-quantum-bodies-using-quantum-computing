# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:58:40 2023

@author: msyne
"""

import numpy as np
import BrickWall as bw
import matplotlib.pyplot as plt
import ExactDiagonalization as ed


def compute_entropy(A,psi):
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
    eigenvalues = [eigenvalue for eigenvalue in eigenvalues if eigenvalue>10**(-12)]
    # Calculate entropy
    entropy = -np.sum(eigenvalues * np.log2(eigenvalues))
    
    return entropy
    
    
def compute_I(A,B,psi):
    
    A_entropy = compute_entropy(A, psi)
    B_entropy = compute_entropy(B, psi)
    AUB_entropy = list(set(A)|set(B))
    AUB_entropy = compute_entropy(AUB_entropy, psi)
    
    return A_entropy + B_entropy - AUB_entropy

def compute_J(d, psi):
    n = len(psi.shape)
    sum = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if abs(i-j) == d:
                sum += compute_I([i], [j], psi)
    return sum/2


def mutual_info_matrix(psi):
    n = len(psi.shape)
    I_matrix = np.zeros((n, n))
    abs_d = np.arange(1, n)
    sum_I = np.zeros_like(abs_d, dtype=float)
    
    for A in range(n):
        for B in range(n):
            if A != B:
                I_matrix[A][B] = compute_I([A], [B], psi)
            else:
                I_matrix[A][B] = compute_I([A], [B], psi)
                
                # Calculate d
                d = abs(A - B)
                # Calculate entropy
                # Sum values and then move to next value of d
                if d <= abs_d[-1]:
                    sum_I[d-1] += I_matrix[A][B]
                                           
    return I_matrix, abs_d, sum_I
    
    
    
    
    
    
    
    
    
    
    

    
    