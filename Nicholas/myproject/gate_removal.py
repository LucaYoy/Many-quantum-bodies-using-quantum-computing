# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:43:31 2022

@author: msyne
"""

import BrickWallTensorDot as bw
import numpy as np
import scipy as sp
import randomunitary as ru

def remove_gate(M,index, Circuit, num_gates):
    # Apply brick_wall up to index-1
    psi=bw.brick_wall(M, num_gates, Circuit, end_index=index)
    # Apply brick_wallR starting at index+1
    phi=bw.brick_wallR(M, num_gates, Circuit, start_index=index+1)
    # Generate the new gate E
    E = np.tensordot(psi,phi).reshape(4,4)
    # The old overlap simply contracts the removed matrix with E
    U_old = np.tensordot(E,ru.matrices[index].reshape(4,4))   
    # The new overlap contracts E with the matrix obtained from SVD
    U,s,Vh = sp.linalg.svd(E.conj())
    U_new = np.dot(U,Vh)
    U_new = np.tensordot(U_new,ru.matrices[index].reshape(4,4))
    return abs(U_new),abs(U_old)
    
    
Circuit=bw.Circuit(4)
E = remove_gate(2,0,Circuit,5)
