# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:43:31 2022

@author: msyne
"""

import BrickWallTensorDot as bw
import numpy as np
import randomunitary as ru
import matplotlib.pyplot as plt
import ExactDiagonalization as ed


def remove_gate(index, Circuit,CircuitED, num_gates):
    # Apply brick_wall up to index-1
    psi=bw.brick_wall(num_gates, Circuit, end_index=index)
    # Apply brick_wallR starting at index+1
    phi=bw.brick_wallR(num_gates, CircuitED, start_index=index+1)
    
    n = Circuit.n
    
    qubit_map = []
    M = int(num_gates / (CircuitED.n - 1)) + 1
    
    for i in range(M):
        for j in range(0, Circuit.n-1, 2):
            qubit_map.append(j)
            #print(f"i is {j}")
        for k in range(1, Circuit.n-1, 2):
            qubit_map.append(k)
            #print(f"i is {k}")
    qubit_map = qubit_map[0:num_gates] 
    removed_gate_qubit = qubit_map[index]  

    #print(qubit_map)                
    
    
    # Determine the axes of psi and phi to use for tensor dot product
    psi_axes = list(range(n))
    phi_axes = list(range(n))
    
    #print(f"removed gate is {index}")
    
    psi_axes.remove(removed_gate_qubit)
    psi_axes.remove(removed_gate_qubit + 1)
    
    phi_axes.remove(removed_gate_qubit)
    phi_axes.remove(removed_gate_qubit + 1)
    #print(f"axes are {psi_axes} and {phi_axes}")
    
    #print(f"shape of psi is {psi.shape}")
    #print(f"shape of phi is {phi.shape}")    
    # Generate the new gate E
    E = np.tensordot(psi,phi,((psi_axes),(phi_axes)))# (2,2,2,2)
    #print(f"shape of E is {E.shape}")
    E = E.transpose(2,3,0,1)   
    
    # The old overlap simply contracts the removed matrix with E
    U_old = np.tensordot(E,ru.matrices[index])
    overlap_old = np.tensordot(E,ru.matrices[index], axes=(range(Circuit.n),range(Circuit.n)))
    # The new overlap contracts E with the matrix obtained from SVD
    U,s,Vh = np.linalg.svd(E.reshape(4,4).conj())
    U_new = np.matmul(U,Vh).reshape((tuple([2]*Circuit.n)))
    overlap_new = np.tensordot(E,U_new,axes=(range(Circuit.n),range(Circuit.n)))
    
    if abs(overlap_old) > abs(overlap_new):
        print("something broke")
    
    #return abs(overlap_old), abs(overlap_new), U_new, U_old
    return E
    
qubits = 4

Circuit=bw.Circuit(qubits)
CircuitED=bw.CircuitED(qubits, 2, 1)
#e = remove_gate(2,Circuit,CircuitED,5)


def optimize_circuit(Circuit, CircuitED, num_gates, max_iterations):
    
    overlaps = []
    errors = []
    overlapsold = []
    relative_errors = []
    iterations = 0
    M = int(num_gates / (CircuitED.n - 1)) + 1
    
    # Initial Overlap
    print(abs(np.tensordot(Circuit.psi,CircuitED.phi,axes=(range(Circuit.n),range(Circuit.n)))))
    
    
    Phi = ed.exactDiagonalization(4,1,1)
    test = bw.brick_wall(5, Circuit)
    print(Phi.conj().shape)
    print(abs(np.tensordot(test, Phi.conj(), axes=(range(Circuit.n), range(Circuit.n)))))
    
    
     
    for index in range(num_gates):
        
        E = remove_gate(index, Circuit, CircuitED, num_gates)
        #print(f"The removed gate is {index}")
        
        U_old = np.tensordot(E,ru.matrices[index])
        overlap_old = np.tensordot(E,ru.matrices[index], axes=(range(Circuit.n),range(Circuit.n)))
        #print(abs(overlap_old))
        U,s,Vh = np.linalg.svd(E.conj().reshape(4,4))
        U_new = np.matmul(U,Vh).reshape((tuple([2]*Circuit.n)))
        overlap_new = np.tensordot(E,U_new, axes=(range(Circuit.n),range(Circuit.n)))
        
        error = 1 - abs(overlap_new)
        errorold = 1 - abs(overlap_old)
        
        relative_error = abs(overlap_new) - abs(overlap_old)    
        
        if abs(overlap_new) < abs(overlap_old):
            print("It broke")
        
        ru.matrices[index] = U_new
                       
        overlaps.append(abs(overlap_new))
        errors.append(error)
        overlapsold.append(errorold)
        relative_errors.append(relative_error)        
        
        #debug = ed.exactDiagonalization(4, 1, 1)
        #debugtest = abs(np.tensordot(E.reshape(4,4),debug.reshape(4,4)))
        
    return errors, overlapsold
        
        
r = optimize_circuit(Circuit, CircuitED, 5, 5)      
        
    
    



    
        
        
        
        
        
        
        
        
        
        
        
        
        
        






    
    
    
    
    
    
    
    