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
H = 1.5
G = 0

phi = ed.exactDiagonalization(Qubits, J, H, G)[1]

matrix_exact,_,_ = et.mutual_info_matrix(phi)

fig, axs = plt.subplots(1, 4, figsize=(10,3), sharey=True)
fig.suptitle("Mutual Information Matrix")

im1 = axs[0].imshow(matrix_exact, cmap='Greens')
axs[0].set_title('Exact')


Circuit = bw.Circuit(Qubits, 1, J, H, G)
psi = Circuit.optimize_circuit(100, 0.00001, False, True, True)[2]
matrix1,_,_ = et.mutual_info_matrix(psi)

im2 = axs[1].imshow(matrix1, cmap='Greens')
axs[1].set_title('1 Layer')

Circuit2 = bw.Circuit(Qubits, 2, J, H, G)
psi2 = Circuit2.optimize_circuit(50, 0.00001, False, True, True)[2]
matrix2,_,_ = et.mutual_info_matrix(psi2)

im3 = axs[2].imshow(matrix2, cmap='Greens')
axs[2].set_title('2 Layers')

Circuit3 = bw.Circuit(Qubits, 3, J, H, G)
psi3 = Circuit3.optimize_circuit(50, 0.00001, False, True, True)[2]
matrix3,_,_ = et.mutual_info_matrix(psi3)

im4 = axs[3].imshow(matrix3, cmap='Greens')
axs[3].set_title('3 Layers')



fig.colorbar(im2, ax=axs.ravel().tolist())

plt.show()


