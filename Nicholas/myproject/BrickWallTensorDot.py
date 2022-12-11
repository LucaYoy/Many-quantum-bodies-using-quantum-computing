# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:13:20 2022

@author: msyne
"""

import numpy as np
import Gates as g
from scipy.stats import unitary_group as U

U = U.rvs(4)
U = U.reshape(2,2,2,2)

class Circuit:
    def __init__(self,n):
        self.n = n
        self.psi = np.zeros(2**n)
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n))#define initial psi
        
        
def had(qu,Circuit):#Hadamard gate
    Circuit.psi = np.tensordot(g.Had,Circuit.psi,(1,qu))
    Circuit.psi = np.moveaxis(Circuit.psi,0,qu)
        
def CNOT(qu,Circuit):#CNOT gate
    Circuit.psi = np.tensordot(g.CNOTt,Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))

def unitary(qu,Circuit):#random unitary
    Circuit.psi = np.tensordot(U,Circuit.psi,((2,3),(qu,qu+1)))
    Circuit.psi = np.moveaxis(Circuit.psi,(0,1),(qu,qu+1))


def solutionT(Circuit):
    #had(0,Circuit)
    for i in range(Circuit.n%2,Circuit.n-1,2):
      unitary(i,Circuit)
    for j in range(Circuit.n%2+1,Circuit.n-1,2):
      unitary(j,Circuit)
    
def solver(M,Circuit):
    for i in range(M):
        solutionT(Circuit)

Circuit=Circuit(4)
solver(2,Circuit)      
print(Circuit.psi.flatten())   
t = Circuit.psi.reshape(4,4)

#class Circuit2:
#    def __init__(self,n):
#        self.n = n
#        self.psi = np.zeros(2**n)
#        self.psi[0] = 1
#        self.psi = self.psi.reshape(tuple([2]*n))#define initial psi

#def solutionM(Circuit2):
    #Had(0,Circuit2)
    #Unitary(0,Circuit2)
    #Unitary(2,Circuit2)
    #Unitary(4,Circuit2)
    #Unitary(1,Circuit2)
    #Unitary(3,Circuit2)
    #Unitary(2,Circuit2)
    #Unitary(1,Circuit2)
    
#Circuit2=Circuit2(4)
#solutionM(Circuit2)
#print(Circuit2.psi.flatten()) 
#r = Circuit2.psi.reshape(4,4)







