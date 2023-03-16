# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:46:56 2023

@author: msyne
"""

import BrickWall as bw
import matplotlib.pyplot as plt

Qubits = 10
Layers = 20
J = 1
H = 0.5

plt.figure(figsize=(8,6))
for i in range(5):
    Circuit = bw.Circuit(Qubits, Layers, J, H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    overlaps,_,_ = Circuit.optimize_circuit(20, 0.001, False, True)
    
    plt.plot(range(len(overlaps)), overlaps, "-bo")
    
    Circuit2 = bw.Circuit(Qubits, Layers, J, H, gatesrandom=False)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    overlaps2,_,_ = Circuit2.optimize_circuit(20, 0.001, False, True)
    
    plt.plot(range(len(overlaps2)), overlaps2, "-ro")

plt.xlabel("Number of iterations")
plt.ylabel("1 - overlap")
plt.axhline(y=0, color='k', linestyle='dashed', label="Exact")
plt.legend(["Aprroximation random gates", "Aprroximation close to identity"])
plt.show()

