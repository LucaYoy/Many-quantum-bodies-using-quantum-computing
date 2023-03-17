# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:36:22 2023

@author: msyne
"""

import Entanglement as et
import ExactDiagonalization as ed
import BrickWall as bw 
import matplotlib.pyplot as plt

Qubits = 8
J = 1
h = 0.5

plt.figure(figsize=(8, 5))
for Layers in range(1,4):

    Circuit = bw.Circuit(Qubits, Layers, J ,h)
    psi=Circuit.optimize_circuit(10, 0.0001, False)[2]

    entropies = []
    for n in range(0, Qubits+1):
        entropy = et.compute_entanglement(psi, n)
        entropies.append(entropy)
    
    plt.plot(range(Qubits+1), entropies,'-o', label=f'{Layers} layers')

    
phi = ed.exactDiagonalization(Qubits, J, h)[1]

entropies_exact = []
for n in range(0, Qubits):
    entropy = et.compute_entanglement(phi, n)
    entropies_exact.append(entropy)

entropies_exact.append(0)
plt.plot(range(Qubits+1), entropies_exact,'-o', label=f'psi target, J = {J}')

plt.xlabel('i band')
plt.ylabel('Entanglement entropy')
plt.legend()
plt.show()