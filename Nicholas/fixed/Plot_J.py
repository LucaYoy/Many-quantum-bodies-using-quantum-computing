# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:38:38 2023

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

phi = ed.exactDiagonalization(Qubits, J, H)[1]

J = et.compute_J([4,5], phi)
print(J)