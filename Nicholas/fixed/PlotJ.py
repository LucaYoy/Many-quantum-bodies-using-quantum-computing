# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:21:58 2023

@author: msyne
"""

import Entanglement3 as et
import ExactDiagonalization as ed
import matplotlib.pyplot as plt
import BrickWall as bw
import numpy as np

Qubits = 8
J = 1
H = 1
G = 0

phi = ed.exactDiagonalization(Qubits, J, H, G)[1]

print(et.compute_J(3, phi))