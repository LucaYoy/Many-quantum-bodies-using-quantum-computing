# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:13:20 2022

@author: msyne
"""

import numpy as np
import Gates as g
import randomunitary as rd
import ExactDiagonalization as ed
from scipy.stats import unitary_group as U

class Circuit:
    def __init__(self,n, gates=None):
        self.n = n
        self.psi = np.zeros(2**n)
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n))# Define initial psi
                               

class CircuitED:
    def __init__(self,n,J,h):
        self.n = n
        self.J = J
        self.h = h
        self.phi = ed.exactDiagonalization(n, J, h)
                              
def had(qu,Circuit):# Hadamard gate
    Circuit.psi = np.tensordot(g.Had,Circuit.psi,(1,qu))
    Circuit.psi = np.moveaxis(Circuit.psi,0,qu)
        
def cNOT(qu,Circuit):# CNOT gate
    Circuit.psi = np.tensordot(g.CNOTt,Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))
    
def unitary(qu,Circuit,M):# Random unitary
    Circuit.psi = np.tensordot(rd.matrices[M],Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))
    
def unitaryR(qu,CircuitED,M):# Random unitary
    CircuitED.phi = np.tensordot(rd.matrices[M],CircuitED.phi,((0,1),(qu,qu+1)))
    CircuitED.phi = np.moveaxis(CircuitED.phi,(0,1),(qu,qu+1))    

def brick_wall(num_gates, Circuit, start_index=0, end_index=None):
    
    # Defining number of layers internally
    M = int(num_gates / (Circuit.n - 1)) + 1
    #print(f"number of layers is {M}")
    
    if end_index is None:
        end_index = num_gates# Set a variable to stop partway through a slice
    gate = start_index # Set variable for gates to loop through
    for i in range(M):
        for j in range(0, Circuit.n-1, 2):# Loop through gates on odd slices
            if gate >= end_index:
                return Circuit.psi
            #print(f"Applying gate {gate} to qubit {j}")# Debug
            unitary(j, Circuit, gate)
            gate += 1
        for k in range(1, Circuit.n - 1, 2):# Loop through gates on even slices
            if gate >= end_index:
                return Circuit.psi
            #print(f"Applying gate {gate} to qubit {k}")# Debug
            unitary(k, Circuit, gate)
            gate += 1       
    return Circuit.psi       

def brick_wallR(num_gates, CircuitED, start_index=0, end_index=None):
    
    M = int(num_gates / (CircuitED.n - 1)) + 1
    
    if end_index is None:
        end_index = num_gates# Set variable to stop partway through a slice
    gate = num_gates - 1 # Set variable for gates to loop through
        
    gates = []
    for i in range(M):
        for j in range(0, CircuitED.n -1, 2):
            if gate < end_index:
                gates.append(j)
        for k in range(1, CircuitED.n - 1, 2):
            if gate < end_index:
                gates.append(k)
    gates = gates[0:num_gates]
    gates = gates[::-1] 
    
    for i in range(num_gates):
        if gate < start_index:
            break
        #print(f"Applying gate {gate} to qubit {gates[i]}")
        unitaryR(gates[i], CircuitED, gate)
        gate -= 1
           
        
    return CircuitED.phi   
        
#    for i in range(M):
#        for j in range(CircuitED.n - 2, -1, -2):# Loop through gates on odd slices
#            if gate < start_index:
#                return CircuitED.phi
#            print(f"Applying gate {gate} to qubit {j}")
#            unitaryR(j, CircuitED, gate)
#            gate -= 1
#        for k in range(CircuitED.n - 3,-1, -2):# Loop through gates on even slices
#            if gate < start_index:
#                return CircuitED.phi
#            print(f"Applying gate {gate} to qubit {k}")
#            unitaryR(k, CircuitED, gate)
#            gate -= 1
#    return CircuitED.phi  
 
#CircuitED=CircuitED(4,1,1)
#s=brick_wallR(3,CircuitED)
#s = CircuitED.phi.reshape(4,4)
         
#Circuit1=Circuit(4)
#t=brick_wall(8,Circuit1)   
#t = Circuit1.psi.reshape(4,4)  


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
       
#Circuit2=Circuit2(4)
#solutionM(Circuit2)
#r = Circuit2.psi.reshape(4,4)

        




