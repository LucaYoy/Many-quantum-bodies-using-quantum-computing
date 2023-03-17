# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:36:29 2023

@author: msyne
"""

import Entanglement3 as et
import numpy as np
import matplotlib.pyplot as plt
import ExactDiagonalization as ed
import BrickWall as bw

Qubits = 8
J = 1
H = 0.5

phi = ed.exactDiagonalization(Qubits, J, H)[1]

matrix,_,_ = et.mutual_info_matrix(phi)

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12,12))
fig.suptitle("Mutual Information Matrix")

axs[0, 0].set_title('Exact State', weight="bold")
im0 = axs[0, 0].imshow(matrix, cmap='Greens')
plt.colorbar(im0, ax=axs[0, 0])

for Layers in range(1,4):
    Circuit = bw.Circuit(Qubits, Layers, J, H)
    psi = Circuit.optimize_circuit(Qubits, 0.0001, False, False)[2]

    matrix,_,_ = et.mutual_info_matrix(psi)
    
    axs[Layers // 2, Layers % 2].set_title(f'{Layers} Layers', weight="bold")
    im = axs[Layers // 2, Layers % 2].imshow(matrix, cmap='Greens')
    plt.colorbar(im, ax=axs[Layers // 2, Layers % 2])

plt.show()