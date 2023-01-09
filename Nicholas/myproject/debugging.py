# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:14:38 2022

@author: msyne
"""

# This file contains all the tests for the accompanying diary entry, 22/12/22

import BrickWallTensorDot as bw
import numpy as np
import ExactDiagonalization as ed
import gate_removal as gr
import randomunitary as ru

# Try the 4 qubit circuit with 5 gates 

Circuit_1=bw.Circuit(4)
S1 = bw.brick_wall(2,5,Circuit_1)
CircuitED_1=bw.CircuitED(4, 1, 1)
T1 = bw.brick_wallR(2, 5, CircuitED_1)

Psi = np.zeros([2,2,2,2])
Psi[0,0,0,0] = 1
Phi = ed.exactDiagonalization(4,1,1)

# Make sure that the overlaps are equal
#overlap_left = abs(np.tensordot(S1,np.conjugate(Phi),axes=(range(4),range(4))))
#overlap_right = abs(np.tensordot(T1,np.conjugate(Psi),axes=(range(4),range(4))))
# ------------------------------------------------------------------------------
# Now a 5 qubit circuit with 5 gates

Circuit_2=bw.Circuit(5)
S2 = bw.brick_wall(2,6,Circuit_2)
CircuitED_2=bw.CircuitED(5, 1, 1)
T2 = bw.brick_wallR(2, 6, CircuitED_2)

Psi = np.zeros([2,2,2,2,2])
Psi[0,0,0,0,0] = 1
Phi = ed.exactDiagonalization(5,1,1)

# Make sure that the overlaps are equal
#overlap_left = abs(np.tensordot(S2,np.conjugate(Phi),axes=(range(5),range(5))))
#overlap_right = abs(np.tensordot(T2,np.conjugate(Psi),axes=(range(5),range(5))))
# ------------------------------------------------------------------------------
# Now removing a gate for a 4 qubit 5 gate circuit
Circuit_3=bw.Circuit(4)
S3 = bw.brick_wall(2,2,Circuit_3)# Gates 0 and 1 applied
CircuitED_3=bw.CircuitED(4, 1, 1)
T3 = bw.brick_wallR(1, 5, CircuitED_3, start_index=(2))# Gates 4 3 2 applied

Psi = np.zeros([2,2,2,2])
Psi[0,0,0,0] = 1
Phi = ed.exactDiagonalization(4,1,1)

Circuit_4=bw.Circuit(4)
S4=bw.brick_wall(2, 5, Circuit_4)# Circuit with 5 gates

Circuit_5=bw.Circuit(4)
CircuitED_5=bw.CircuitED(4,1,1)
U_old = gr.remove_gate(2,3,Circuit_5,CircuitED_5,5)# Circuit with gate 4 removed

# Overlap between two halves of the Circuit
overlap1 = abs(np.tensordot(S3,T3,axes=(range(4),range(4))))

# Overlap between Circuit state and Target state
overlap2 = abs(np.tensordot(S4,Phi.conj(),axes=(range(4),range(4))))

# Overlap between removed gate Circuit and removed Gate
overlap3 = abs(np.tensordot(ru.matrices[3],U_old,axes=(range(4),range(4))))
#------------------------------------------------------------------------------

# Extra test; ignore
#Circuit_6=bw.Circuit(4)
#S6 = bw.brick_wall(2,3,Circuit_6)# Gates 0, 1, 2 applied
#CircuitED_6=bw.CircuitED(4, 1, 1)
#T6 = bw.brick_wallR(1, 5, CircuitED_6, start_index=(4))# Gates 4 applied

#PHI = np.tensordot(S6,T6)
#overlap4 = abs(np.tensordot(ru.matrices[3],PHI,axes=(range(4),range(4))))










