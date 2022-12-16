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
        self.psi = self.psi.reshape(tuple([2]*n))#define initial psi
        
        
def had(qu,Circuit):#Hadamard gate
    Circuit.psi = np.tensordot(g.Had,Circuit.psi,(1,qu))
    Circuit.psi = np.moveaxis(Circuit.psi,0,qu)
        
def cNOT(qu,Circuit):#CNOT gate
    Circuit.psi = np.tensordot(g.CNOTt,Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))

def unitary(qu,Circuit):#random unitary
    Circuit.psi = np.tensordot(g.Ut,Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))
    
def unitarycsv(qu,Circuit,M):
    Circuit.psi = np.tensordot(rd.matrices[M],Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))

def brick_wall(M, num_gates, Circuit):
    gate = 0
    for i in range(M):
        for j in range(0, Circuit.n,2):
            if gate >= num_gates:
                return
            unitarycsv(j, Circuit, gate)
            gate += 1
        for k in range(i%2+1, Circuit.n-1,2):
            if gate >= num_gates:
                return
            unitarycsv(k, Circuit, gate)
            gate += 1   
      
def solutionT(Circuit):
    #had(0,Circuit)
    for i in range(Circuit.n%2,Circuit.n-1,2):
      unitary(i,Circuit)
    for j in range(Circuit.n%2+1,Circuit.n-1,2):
      unitary(j,Circuit)
    
Circuit=Circuit(4)
brick_wall(2,5,Circuit)   
t = Circuit.psi.reshape(4,4) 

class Circuit2:
    def __init__(self,n):
        self.n = n
        self.psi = np.zeros(2**n)
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n))#define initial psi

def solutionM(Circuit2):
    unitarycsv(0,Circuit2,0)
    unitarycsv(2,Circuit2,1)
    unitarycsv(1,Circuit2,2)
    unitarycsv(0,Circuit2,3)
    unitarycsv(2,Circuit2,4)
    #unitarycsv(1,Circuit2,5)
    #unitarycsv(0,Circuit2,3)
    #unitarycsv(2,Circuit2,4)
    #Unitary(0,Circuit2)
    #Unitary(2,Circuit2)
    #Unitary(4,Circuit2)
    #Unitary(1,Circuit2)
    #Unitary(3,Circuit2)
    #Unitary(2,Circuit2)
    #Unitary(1,Circuit2)
    
Circuit2=Circuit2(4)
solutionM(Circuit2)
#print(Circuit2.psi.flatten()) 
r = Circuit2.psi.reshape(4,4)







