# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:13:20 2022

@author: msyne
"""

import numpy as np
import Gates as g
import randomunitary as rd

class Circuit:
    def __init__(self,n):
        self.n = n
        self.psi = np.zeros(2**n)
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n))# define initial psi
        
        
def had(qu,Circuit):# Hadamard gate
    Circuit.psi = np.tensordot(g.Had,Circuit.psi,(1,qu))
    Circuit.psi = np.moveaxis(Circuit.psi,0,qu)
        
def cNOT(qu,Circuit):# CNOT gate
    Circuit.psi = np.tensordot(g.CNOTt,Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))
    
def unitary(qu,Circuit,M):# Random unitary
    Circuit.psi = np.tensordot(rd.matrices[M],Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))
    
def unitaryR(qu,Circuit,M):# Random unitary
    Circuit.psi = np.tensordot(rd.matrices[M],Circuit.psi,((0,1),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))    

def brick_wall(M, num_gates, Circuit, start_index=0, end_index=None):
    if end_index is None:
        end_index = num_gates# Set a variable to stop partway through a slice
    gate = start_index # Set variable for gates to loop through
    for i in range(M):
        for j in range(0, Circuit.n, 2):# Loop through gates on odd slices
            if gate >= end_index:
                return Circuit.psi
            #print(f"Applying gate {gate} to qubit {j}")# Debug
            unitary(j, Circuit, gate)
            gate += 1
        for k in range(i % 2 + 1, Circuit.n - 1, 2):# Loop through gates on even slices
            if gate >= end_index:
                return Circuit.psi
            #print(f"Applying gate {gate} to qubit {k}")# Debug
            unitary(k, Circuit, gate)
            gate += 1
    return Circuit.psi       

def brick_wallR(M, num_gates, Circuit, start_index=0, end_index=None):
    if end_index is None:
        end_index = num_gates
    gate = num_gates - 1 # Set variable for gates to loop through
    for i in range(M):
        for j in range(Circuit.n - 2, -1, -2):# Loop through gates on odd slices
            if gate < start_index:
                return Circuit.psi
            #print(f"Applying gate {gate} to qubit {j}")
            unitaryR(j, Circuit, gate)
            gate -= 1
        for k in range(i % 2 + 1, Circuit.n - 1, 2):# Loop through gates on even slices
            if gate < start_index:
                return Circuit.psi
            #print(f"Applying gate {gate} to qubit {k}")
            unitaryR(k, Circuit, gate)
            gate -= 1
    return Circuit.psi  

#Circuit=Circuit(4)
#gate_remover(2, 2, Circuit)
 
#Circuit2=Circuit(4)
#brick_wallR(2,5,Circuit2)
#s = Circuit2.psi.reshape(4,4)
         
#Circuit1=Circuit(4)
#brick_wall(2,3,Circuit1)   
#t = Circuit1.psi.reshape(4,4)  

#f = np.inner(s,t)
#f = np.linalg.norm(f)

class Circuit2:# For testing
    def __init__(self,n):
        self.n = n
        self.psi = np.zeros(2**n)
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n))#define initial psi

def solutionM(Circuit2):# Add the gates in 1 by 1, as a check
    unitaryR(1,Circuit2,2)
    unitaryR(0,Circuit2,1)
    unitaryR(2,Circuit2,0)
    #unitary(0,Circuit2,3)
    #unitary(2,Circuit2,4)
    #unitarycsv(1,Circuit2,5)
       
Circuit2=Circuit2(4)
solutionM(Circuit2)
#r = Circuit2.psi.reshape(4,4)

        




