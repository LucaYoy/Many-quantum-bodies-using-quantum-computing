# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:00:14 2022

@author: msyne
"""
import numpy as np

A = 1/np.sqrt(2)
Id = np.identity(2)
H = np.array([[1,1],[1,-1]])
Had = np.multiply(A,H)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
CNOT = CNOT.reshape((2,2,2,2))

psi = np.zeros([2,2,2,2])

psi[0,0,0,0] = 1#initial state of psi

psi = np.tensordot(Had,psi,axes=([1],[0]))

psi = np.tensordot(CNOT,psi,axes=([2,3],[0,1]))

psi = np.tensordot(CNOT,psi,axes=([2,3],[1,2]))
psi = psi.transpose((2,0,1,3))

psi = np.tensordot(CNOT,psi,axes=([2,3],[2,3]))
psi = psi.transpose((2,3,0,1))


print(psi.flatten())