# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:46:56 2023

@author: msyne
"""

import BrickWall as bw
import matplotlib.pyplot as plt

Qubits = 6
Layers = 6
J = 1
H = 1
iterations = 1000

plt.figure(figsize=(8,6))
for i in range(5):
    # 
    Circuit = bw.Circuit(Qubits, Layers, J, H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    _,overlaps,_, iterations,_=Circuit.optimize_circuit(iterations, 10**-12, True, True)
    
    plt.plot(range(iterations), overlaps, "-b")
    
    Circuit2 = bw.Circuit(Qubits, Layers, J, H, gatesrandom=False)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    _,overlaps2,_,iterations,_ = Circuit2.optimize_circuit(iterations, 10**-12, False, True)
    
    plt.plot(range(iterations), overlaps2, "-r")

plt.xlabel("Number of iterations")
plt.ylabel("1 - overlap")
plt.axhline(y=10**-14, color='k', linestyle='dashed', label="Exact")
plt.xscale("log")
plt.yscale("log")
plt.legend(["Old Optimization", "New Optimization"])
plt.show()

