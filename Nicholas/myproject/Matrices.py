# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:54:18 2022

@author: Nick
"""


import numpy as np

n = 3#int(input("Enter number of qubits: "))

J = 0
h = 1

Id = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
Y = np.array([[0,-1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])
    
a = 2**(n-2)

XId = np.identity(a)

M = J * np.kron(XId,np.kron(X,X)) + h * (np.kron(XId,np.kron(Z,Id)) + np.kron(XId,np.kron(Id,Z)))

E,V = np.linalg.eigh(M)

#H = J * np.kron(X,X) + h * (np.kron(Z,Id) + np.kron(Id,Z))
#H = J * np.kron(Id,np.kron(X,X)) + h * (np.kron(Id,np.kron(Z,Id)) + np.kron(Id,np.kron(Id,Z)))
#H = J * np.kron(np.kron(Id,X),X) + h * (np.kron(np.kron(Id,Z),Id) + np.kron(np.kron(Id,Id),Z))



#print(E)
#print(V)



