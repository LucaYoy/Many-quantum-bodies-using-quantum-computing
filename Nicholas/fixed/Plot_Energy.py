# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:01:34 2023

@author: msyne
"""

import ExactDiagonalization as ed
import BrickWall as bw
import matplotlib.pyplot as plt
import numpy as np

Qubits = 8
J = 1
h = 1
Layers = 6

phi = ed.exactDiagonalization(Qubits, J, h)
exact_energy,_,_ = phi 
_,_,H = phi
E = []

for x in range(1, Layers):
    Circuit = bw.Circuit(Qubits, Layers, J, h)
    psi = Circuit.optimize_circuit(10, 0.0001, False, False)[2]
    psi = psi.flatten()
    E.append((np.vdot(psi, np.matmul(H, psi))))
    
plt.plot(range(x), E, "-o", label="Approximation")
    
plt.axhline(y=exact_energy, color='k', linestyle="dashed", label="Exact")
plt.xlabel('Layers')
plt.ylabel('Energy (eV)')
plt.legend()
plt.show()

