# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:14:59 2022

@author: msyne
"""

import numpy as np

A = 1/np.sqrt(2)

H = np.array([[1,1],[1,-1]])
Had = np.multiply(A,H)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
CNOT = CNOT.reshape((2,2,2,2))
psi = np.zeros([2,2,2])

psi[0,0,0] = 1

psi = np.tensordot(Had,psi,axes=([1],[0]))

psi = np.tensordot(CNOT,psi,axes=([2,3],[0,1]))

psi = np.tensordot(CNOT,psi,axes=([2,3],[1,2]))
psi = psi.transpose((2,0,1))

p = print(psi.flatten())