# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:03:09 2023

@author: msyne
"""

import os
import matplotlib as plt

#n = 14
#J = 1
#h = 1
#g = 1
#m = 5
filename = 'sweeps=50_n=6_J=1_h=1_g=1_m=5_gates=Identity.txt'


store_overlap = True
gates = []
with open(filename, 'r') as f:
        
    #filename = os.path.splitext(os.path.basename(f.name))[0]
    
    #fig, ax = plt.subplots(figsize=(16,14))
    
    file_contents = f.read()
    
    gates_index = file_contents.find('Gates:')
    gate_data = file_contents[gates_index + len('Gates:'):]
    
gate_lines = gate_data.split('\n')
run_gates = {}

# Iterate over the lines in the gate data
for i, line in enumerate(gate_lines):
    # Check if the line starts with "Run "
    if line.startswith("Run "):
        # If it does, extract the run name
        parts = line.strip().split(": ")
        run_name = parts[0]
        
        # Find the index of the next line that starts with "Run "
        next_run_index = i + 1
        for j in range(i + 1, len(gate_lines)):
            if gate_lines[j].startswith("Run "):
                next_run_index = j
                break
        
        # Extract the gate strings for this run and concatenate them into a single string
        gate_string = ""
        for k in range(i + 1, next_run_index):
            gate_string += gate_lines[k].replace("[", "").replace("]", "")
            
        #complex_numbers = [complex(x) for x in gate_string.split()]
        
        # Add the gate string to the dictionary under the run name
        run_gates[run_name] = gate_string
          
     
import re 

#pattern = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?[-+](?:\d*\.?\d+(?:[eE][-+]?\d+)?)?j"
#pattern = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?[-+]\d*\.?\d+(?:[eE][-+]?\d+)?j"
#pattern = r"[-+]?\d+\.\d+|\d+[-+]\d+\.\d+j|[-+]?\d+\.\d+j|[-+]?\d+[-+]\d+j"
#pattern = r"[-+]?\d+\.\d+[-+]\d+\.\d+j|[-+]?\d+\.\d+j|[-+]?\d+[-+]\d+j|[-+]?\d+\.\d+[-+]\d+j"
pattern = r"[-+]?\d+\.\d+\s*[-+]\s*\d+\.\d+j|[-+]?\d+\.\d+j|[-+]?\d+\s*[-+]\s*\d+j|[-+]?\d+\.\d+\s*[-+]\s*\d+j"




complex_list = []

# Iterate over the values in the dictionary
for gates in run_gates.values():
    # Use regular expression to find complex numbers in the string
    complex_numbers = [complex(match.replace(' ', '')) for match in re.findall(pattern, gates)]

    # Append the complex numbers to the list
    complex_list.extend(complex_numbers)
import numpy as np
# Create a list of objects with 16 complex numbers each
gatess = []
for i in range(0, len(complex_list), 16):
    object_complex_numbers = complex_list[i:i+16]
    object_4d_array = np.array(object_complex_numbers).reshape(2,2,2,2)
    gatess.append(object_4d_array)
    
import ExactDiagonalization as ed  
from scipy.stats import unitary_group as U
import scipy.linalg as sp

class Circuit:


    def __init__(self,n, m, J, h, G, gates=None, gatesrandom=False):
        self.n = n # Number of qubits
        self.m = m # Number of layers
        self.num_gates = int(np.floor(n/2) * np.ceil(m/2) + np.floor((n-1)/2) * np.floor(m/2))
        
        # Create initial zero state
        self.psi = np.zeros(2**n) 
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n)) # Define initial psi
        
        #self.phi = ed.exactDiagonalization(n, J, h, G)[1] # Define target state
        self.phi = ed.exactDiagSparse(n, J, h, G)[1]
        
        self.left = self.psi.copy()  # current state of left half of circuit
        self.right = self.psi.copy()  # current state of right half of circuit

        self.gates = gatess

    def resetLeft(self):
        """ Resets the currently stored left half of circuit """
        self.left = self.psi.copy()

    def resetRight(self):
        """ Resets the currently stored right half of circuit """
        self.right = self.psi.copy()

    def applyUnitary(self, qubit, index):
        """ Applies unitary to left acting on current left half of circuit.
        """
        self.left = np.tensordot(self.gates[index], self.left, ((2,3), (qubit, qubit+1)))
        self.left = np.moveaxis(self.left, (0,1), (qubit, qubit+1))
        
    def applyUnitaryR(self, qubit, index):
        """ Applies unitary to right acting on current right half of circuit.
        """
        self.right = np.tensordot(self.gates[index], self.right, ((0,1), (qubit, qubit+1)))
        self.right = np.moveaxis(self.right, (0,1), (qubit, qubit+1))

    def brick_wall(self, end_index=None):
        """ Applies all gates up to end_index to the left
        """

        self.resetLeft()

        if end_index is None: 
            end_index = self.num_gates  
        end_index = 13
        gate_index = 0
        for layer in range(self.m):

            # loop over even qubits if layer is even
            if layer % 2 == 0:
                for qubit in range(0, self.n-1, 2):
                    # end iteration before we get to end_index
                    if gate_index >= end_index:
                        return self.left
                    #print(f"Applying gate {gate_index} to qubit {qubit}")
                    self.applyUnitary(qubit, gate_index)  # apply unitary to left
                    gate_index += 1

            # loop over odd qubits if layer is odd
            if layer % 2 == 1:
                for qubit in range(1, self.n-1, 2):
                    # end iteration before we get to end_index
                    if gate_index >= end_index:
                        return self.left
                    #print(f"Applying gate {gate_index} to qubit {qubit}")
                    self.applyUnitary(qubit, gate_index)  # apply unitary to left
                    gate_index += 1
             
        return self.left
    
    def brick_wallR(self, start_index=0):
        """ Applies all gates up to from start_index to the right
        """

        self.resetRight()

        gate_index = self.num_gates - 1

        even_qubits = [x for x in range(0, self.n-1, 2)]
        odd_qubits = [x for x in range(1, self.n-1, 2)]

        # Go through layers in reverse!
        for layer in range(self.m-1,-1,-1):

            # Loop over even qubits (in reverse order!) if layer is even
            if layer % 2 == 0:
                for qubit in even_qubits[::-1]:
                    # End iteration before we get to end_index
                    if gate_index < start_index:
                        return self.right
                     
                    #print(f"Applying gate {gate_index} to qubit {qubit}")
                    self.applyUnitaryR(qubit, gate_index)  # apply unitary to right
                    gate_index -= 1

            # Loop over odd qubits if layer is odd
            if layer % 2 == 1:
                for qubit in odd_qubits[::-1]:
                    # end iteration before we get to end_index
                    if gate_index < start_index:
                        return self.right
                    #print(f"Applying gate {gate_index} to qubit {qubit}")
                    self.applyUnitaryR(qubit, gate_index)  # apply unitary to right
                    gate_index -= 1

        return self.right
    
    def finalpsi(self):
        
        final_psi = self.brick_wall()
        
        return final_psi
        
#Circuit = Circuit(6, 5, 1, 1, 1)
#p = Circuit.finalpsi()


 
        
        
        
        
        
        