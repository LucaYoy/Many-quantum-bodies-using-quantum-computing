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
h = 1.5
G = 0
Layers = 10

phi = ed.exactDiagonalization(Qubits, J, h, G)
exact_energy,_,_ = phi 
_,_,H = phi
Evalues = []

for i in range(1, 5):
    Circuit = bw.Circuit(Qubits, i, J, h, G)
    psi = Circuit.optimize_circuit(100, 0.000001, False, True, True)[2]
    psi = psi.flatten()
    E = np.vdot(psi, np.matmul(H, psi.conj()))
    print(psi.shape)
    print(H.shape)
    Evalues.append(E)
    
plt.plot(range(i), Evalues, "-o", label="Approximation")
    
plt.axhline(y=exact_energy, color='k', linestyle="dashed", label="Exact")
plt.xlabel('Layers')
plt.ylabel('Energy (eV)')
plt.legend()
plt.show()

