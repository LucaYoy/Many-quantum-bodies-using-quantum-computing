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
H = 1

phi = ed.exactDiagonalization(Qubits, J, H)[1]

I_matrix, abs_d, sum_I = et.mutual_info_matrix(phi)

for Layers in range(1,4):
    Circuit = bw.Circuit(Qubits, Layers, J, H)
    psi = Circuit.optimize_circuit(100, 0.0001, False, False, True)[2]
    
    I_matrix2, abs_d2, sum_I2 = et.mutual_info_matrix(psi)
    
    plt.plot(abs_d2, sum_I2, "-o", label=f"{Layers} Layers")

plt.plot(abs_d, sum_I, "-o", label="Target State")
plt.xscale("log")
plt.yscale("log")
plt.xlabel('d')
plt.ylabel('J')
plt.title('J vs d')
plt.ylim(10**-5, 10)
plt.legend()
plt.show()