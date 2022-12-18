# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:21:55 2022

@author: msyne
"""

import numpy as np
import Gates as g

def exactDiagonalization(n,J,h):
    
    H = np.zeros((2**n,2**n))
    
    for i in range(1,n):
        
        H += -J * np.kron(np.kron(np.eye(2**(i-1)),g.X) ,np.kron(g.X,np.eye(2**(n-i-1))))
        
        H += h * np.kron(np.eye(2**(i)), np.kron(g.Z, np.eye(2**(n-i-1))))
    
    return H

H = exactDiagonalization(3,1,0)

E,V = np.linalg.eigh(H)
    
    