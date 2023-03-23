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
Layers = 5
iterations=100

plt.figure(figsize=(8,6))
for i in range(5):
    Circuit = bw.Circuit(Qubits, Layers, J, H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?, new optimization?
    _,overlaps,_, iterations,_= Circuit.optimize_circuit(iterations, 10**-12, plot=False, show_overlap=False, 
                                                         stopped_flag=False, optimizationnew=False)
    plt.plot(range(len(overlaps)), overlaps, "-b", label="Old Optimization")
    
    Circuit2 = bw.Circuit(Qubits, Layers, J, H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?, new optimization?
    _,overlaps2,_, iterations2,_= Circuit.optimize_circuit(iterations, 10**-12, plot=False, show_overlap=True, 
                                                         stopped_flag=False, optimizationnew=True)
    
    plt.plot(range(len(overlaps2)), overlaps2, "-r", label='New Optimization')
    
plt.axhline(y=0, color='k', linestyle='dashed', label="Exact")
plt.xlabel("Number of iterations")
plt.ylabel("1 - overlap")
#plt.axhline(y=10**-14, color='k', linestyle='dashed', label="Exact")
plt.xscale("log")
plt.yscale("log")
plt.legend(["Old Optimization", "New Optimization"])
plt.title(f"J={J},h={H}, {Layers} Layers, Qubits = {Qubits}")
plt.show()