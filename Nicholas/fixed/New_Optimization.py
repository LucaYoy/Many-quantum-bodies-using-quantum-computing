# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:45:57 2023

@author: msyne
"""

import BrickWall as bw
import matplotlib.pyplot as plt

Qubits = 6
H = 1
J = 1
Layers = 6

plt.figure(figsize=(8,6))
for i in range(5):
    Circuit = bw.Circuit(Qubits, Layers, J, H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?, new optimization?
    _,overlaps,_, iterations,_= Circuit.optimize_circuit(10, 10**-12, True, False, False)
    
    plt.plot(range(len(overlaps)), overlaps, "-bo", label="Old Optimization")
    
    Circuit2 = bw.Circuit(Qubits, Layers, J, H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?, new optimization?
    _,overlaps2,_, iterations2,_= Circuit.optimize_circuit(10, 10**-12, True, True, True)
    
    plt.plot(range(len(overlaps2)), overlaps2, "-ro", label='New Optimization')
    
plt.axhline(y=0, color='k', linestyle='dashed', label="Exact")
plt.legend()
plt.show()