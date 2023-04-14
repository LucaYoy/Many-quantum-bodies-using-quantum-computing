# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

A = 1/np.sqrt(2)
Id = np.identity(4)
H = np.array([[1,1],[1,-1]])
Had = np.multiply(A,H)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
CNOTt = CNOT.reshape((2,2,2,2))
X = np.array([[0,1],[1,0]])
Y = np.array([[0,-1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])

theta = np.pi
RXX = np.round(np.exp(-1j*theta/2*np.kron(X,X)),2)
RXXt = RXX.reshape((2,2,2,2))

M = np.random.randn(4,4) + 1j*np.random.randn(4,4)
H = M + np.matrix.getH(M)
U = np.exp(1j*H)#random unitary
Ut = U.reshape((2,2,2,2))

M2 = np.random.randn(2,2) + 1j*np.random.randn(2,2)
H2 = M2 + np.matrix.getH(M2)
U2 = np.exp(1j*H2)#random unitary