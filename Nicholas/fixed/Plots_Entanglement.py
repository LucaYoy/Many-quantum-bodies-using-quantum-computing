# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:02:52 2023

@author: msyne
"""

import Entanglement3 as et
import ExactDiagonalization as ed
import BrickWall as bw 
import matplotlib.pyplot as plt

Qubits = 8
J = 1
H = 1.5
G = 0

phi = ed.exactDiagonalization(Qubits, J, H, G)[1]

entropies_exact = []

for i in range(0, len(phi.shape)+1):
    
    entropy = et.compute_entropy(list(range(i)), phi)
    
    entropies_exact.append(entropy)
    
for Layers in range(1,4):
    entropies = []
    Circuit = bw.Circuit(Qubits, Layers, J, H, G)
    psi=Circuit.optimize_circuit(100,10**-12, True, True, True)[2]
    
    for i in range(0, len(psi.shape)+1):
        entropy = et.compute_entropy(list(range(i)), psi)
        entropies.append(entropy)
    
    plt.plot(range(0, len(psi.shape)+1), entropies, "-o", label=f"{Layers} Layers")
    
plt.plot(range(0, len(phi.shape)+1), entropies_exact, "-o", label="Target State")
plt.xlabel('Qubit')
plt.ylabel('Entropy')
plt.legend()
plt.show()

pli = phi.flatten()
poi = psi.flatten()