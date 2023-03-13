# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:51:14 2023

@author: msyne
"""

import Entanglement3 as et
import ExactDiagonalization as ed
import matplotlib.pyplot as plt
import BrickWall as bw
import numpy as np

Qubits = 8
J = 1
H = 0.5

phi = ed.exactDiagonalization(Qubits, J, H)

I_matrix, abs_d, sum_I = et.mutual_info_matrix(phi)

for Layers in range(1,4):
    entropies = []
    Circuit = bw.Circuit(Qubits, Layers, J, H)
    psi=Circuit.optimize_circuit(Qubits, 0.0001, False)[2]
    
    I_matrix2, abs_d2, sum_I2 = et.mutual_info_matrix(psi)
    
    sum_I2 = [x for x in sum_I2 if x >= 1e-12]
    
    plt.plot(np.log(abs_d2), np.log(sum_I2), "-o", label=f"{Layers} Layers")

plt.plot(np.log(abs_d), np.log(sum_I), "-o", label="Target State")
plt.xlabel('d')
plt.ylabel('Sum of I_matrix')
plt.title('Sum of I_matrix vs d')
plt.legend()
plt.show()