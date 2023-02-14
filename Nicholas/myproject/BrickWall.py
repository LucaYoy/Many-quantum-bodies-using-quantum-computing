# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:47:30 2023

@author: msyne
"""

import numpy as np
import Gates as g
import ExactDiagonalization as ed
from scipy.stats import unitary_group as U
import itertools

class Circuit:
    def __init__(self,n, m, J, h, gates=None):
        self.n = n # Number of qubits
        self.m = m # Number of layers
        self.num_gates = int(np.floor(n/2) * np.ceil(m/2) + np.floor((n-1)/2) * np.floor(m/2))
        self.psi = np.zeros(2**n) 
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n)) # Define initial psi
        
        self.phi = ed.exactDiagonalization(n, J, h) # Define target state
        
        if gates is None:
            gates = [U.rvs(4).reshape(2,2,2,2) for i in range(self.num_gates)]
        self.gates = gates
        
    def unitary(self, qu, M):
        self.psi = np.tensordot(self.gates[M], self.psi, ((2,3), (qu, qu+1)))
        self.psi = np.moveaxis(self.psi, (0,1), (qu,qu+1))
        
    def unitaryR(self, qu, M):
        self.phi = np.tensordot(self.gates[M], self.phi, ((0,1), (qu, qu+1)))
        self.phi = np.moveaxis(self.phi, (0,1),(qu,qu+1))
        
    def brick_wall(self, start_index=0, end_index=None):
        
        M = self.m    
        if end_index is None:
            end_index = self.num_gates
        gate = start_index
        for i in range(M):
            for j in range(0, self.n-1, 2):
                if gate >= end_index:
                    return self.psi
                #print(f"Applying gate {gate} to qubit {j}")# Debug
                self.unitary(j, gate)
                gate += 1
            for k in range(1, self.n - 1, 2):
                if gate >= end_index:
                    return self.psi
                #print(f"Applying gate {gate} to qubit {k}")# Debug
                self.unitary(k, gate)
                gate += 1       
        return self.psi
    
    def brick_wallR(self, start_index=0, end_index=None):
        
        M = self.m
        if end_index is None:
            end_index = 0#self.num_gates# Set variable to stop partway through a slice
            
        gate = self.num_gates - 1 # Set variable for gates to loop through

        gates = []
        for i in range(M):
            for j in range(0, self.n - 1, 2):
                if gate >= end_index:
                    gates.append(j)
            for k in range(1, self.n - 1, 2):
                if gate >= end_index:
                    gates.append(k)
        gates = gates[0:self.num_gates]
        gates = gates[::-1] 
        
        for i in range(self.num_gates):
            if gate < start_index or gate < end_index:
                break
            #print(f"Applying gate {gate} to qubit {gates[i]}")
            self.unitaryR(gates[i], i)
            gate -= 1
               
            
        return self.phi
    
    def remove_gate(self, index):
        
        num_gates = self.num_gates
        # Apply brick_wall up to index-1
        psi = self.brick_wall(end_index=index)
        # Apply brick_wallR starting at index+1
        phi = self.brick_wallR(start_index=index+1)
        
        n = Circuit.n
        
        qubit_map = []
        M = self.m
        
        for i in range(M):
            for j in range(0, Circuit.n-1, 2):
                qubit_map.append(j)
            for k in range(1, Circuit.n-1, 2):
                qubit_map.append(k)
        qubit_map = qubit_map[0:num_gates] 
        removed_gate_qubit = qubit_map[index]  
        
        # Determine the axes of psi and phi to use for tensor dot product
        psi_axes = list(range(n))
        phi_axes = list(range(n))
        
        psi_axes.remove(removed_gate_qubit)
        psi_axes.remove(removed_gate_qubit + 1)
        
        phi_axes.remove(removed_gate_qubit)
        phi_axes.remove(removed_gate_qubit + 1)

        E = np.tensordot(psi,phi,((psi_axes),(phi_axes)))

        E = E.transpose(2,3,0,1)   

        return E
    
    def optimize_circuit(self, max_iterations):
        
        overlaps = []
        errors = []
        overlapsold = []
        relative_errors = []
        iterations = 0
        M = self.m
        num_gates = self.num_gates
        
                   
        for i in range(max_iterations):    
            
            for index in range(num_gates):
                
                    E = self.remove_gate(index)

                    overlap_old = np.tensordot(E, self.gates[index], 4)                    

                    U,s,Vh = np.linalg.svd(np.conjugate(E.reshape(4,4)))
                    U_new = np.matmul(U,Vh).reshape(2,2,2,2)                    
                    overlap_new = np.tensordot(E, U_new, 4)
                    self.gates[index] = U_new                                        
                    error = 1 - abs(overlap_new)
                    errorold = 1 - abs(overlap_old)
                    
                    relative_error = abs(overlap_new) - abs(overlap_old) 
                    
                    if abs(overlap_new) < abs(overlap_old):
                        print("Error, overlap isn't increasing")
                    
                    overlaps.append(abs(overlap_new))
                    errors.append(error)
                    overlapsold.append(abs(overlap_old))
                    relative_errors.append(relative_error)  
                                
        return relative_errors, overlaps, overlapsold
        
        
Qubits = 4
Layers = 3
J = 1
H = 1

Circuit = Circuit(Qubits, Layers, J ,H)
p = Circuit.optimize_circuit(1)

#-----------------------------------------------------------------------------
# Checks

# Circuit the same forwards and backwards?
#P = Circuit.brick_wall()
#Q = Circuit.brick_wallR()

#if P.all() == Q.all():
#    print("correct")

#-----------------------------------------------------------------------------
# Remove a gate test:

#P = Circuit.brick_wall(3)
#Q = Circuit.brick_wallR(2)    

# Splitting circuit (no gate removed)
#overlap = abs(np.tensordot(P,Q,4))

# Normal circuit

#Circuit2 = Circuit(4,3,1,1)
#A = Circuit2.brick_wall(5)
#Phi = Circuit2.phi

#overlap2 = abs(np.tensordot(A, Phi.conj(),4))

















