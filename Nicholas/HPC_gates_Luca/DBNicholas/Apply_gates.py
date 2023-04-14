import pickle

Qubits = 8
J = 1
h = 1.5
G = 0

all_gates = []
for Layers in range(3,8):
    filename = f'optimizedGates{J}{h}{G}_{Qubits}_{Layers}'

    def load_obj(filename) :
        with open(filename + '.pkl', 'rb') as f:
            return pickle.load(f)
        
    gates = load_obj(filename)
    all_gates.append(gates)

import numpy as np

class Circuit: 
    
    def __init__(self, n, m):
        
        self.n = n
        self.m = m
        self.num_gates = int(np.floor(n/2) * np.ceil(m/2) + np.floor((n-1)/2 * np.floor(m/2)))
        
        self.psi = np.zeros(2**n)
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n))
        
        self.left = self.psi.copy()
        self.gates = gates
        
    def resetLeft(self):
        self.left = self.psi.copy()
        
    def applyUnitary(self, qubit, index):
        
        self.left = np.tensordot(self.gates[index], self.left, ((2,3), (qubit, qubit+1)))
        self.left = np.moveaxis(self.left, (0,1), (qubit, qubit+1))
        
    def brick_wall(self, end_index=None):
        """ Applies all gates up to end_index to the left
        """

        self.resetLeft()

        if end_index is None: 
            end_index = self.num_gates  
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
    
 
    
    
    
    
    
    
    
    
    
    
    
    