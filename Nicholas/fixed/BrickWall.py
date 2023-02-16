import numpy as np
import Gates as g
import ExactDiagonalization as ed
from scipy.stats import unitary_group as U

class Circuit:
    """ Class that implements brickwall quantum circuit and optimization

    Properties:

    Methods:

    """

    def __init__(self,n, m, J, h, gates=None):
        self.n = n # Number of qubits
        self.m = m # Number of layers
        self.num_gates = int(np.floor(n/2) * np.ceil(m/2) + np.floor((n-1)/2) * np.floor(m/2))
        
        # Create initial zero state
        self.psi = np.zeros(2**n) 
        self.psi[0] = 1
        self.psi = self.psi.reshape(tuple([2]*n)) # Define initial psi
        
        self.phi = ed.exactDiagonalization(n, J, h) # Define target state
        
        self.left = self.psi.copy()  # current state of left half of circuit
        self.right = self.phi.copy()  # current state of right half of circuit

        if gates is None:
            gates = [U.rvs(4).reshape(2,2,2,2) for i in range(self.num_gates)]
        self.gates = gates

    def resetLeft(self):
        """ Resets the currently stored left half of circuit """
        self.left = self.psi.copy()

    def resetRight(self):
        """ Resets the currently stored right half of circuit """
        self.right = self.phi.copy()

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
            end_index = self.num_gates - 1

        gate_index = 0
        for layer in range(self.m):

            # loop over even qubits if layer is even
            if layer % 2 == 0:
                for qubit in range(0, self.n-1, 2):
                    # end iteration before we get to end_index
                    if gate_index > end_index:
                        return self.left

                    self.unitary(qubit, gate_index)  # apply unitary to left
                    gate_index += 1

            # loop over odd qubits if layer is odd
            if layer % 2 == 1:
                for qubit in range(1, self.n-1, 2):
                    # end iteration before we get to end_index
                    if gate_index > end_index:
                        return self.left
                    
                    self.unitary(qubit, gate_index)  # apply unitary to left
                    gate_index += 1

        return self.left
    

    def brick_wallR(self, start_index=0):
        """ Applies all gates up to from start_index to the right
        """

        self.resetRight()

        gate_index = self.num_gates - 1

        even_qubits = [x for x in range(0, self.n-1, 2)]
        odd_qubits = [x for x in range(1, self.n-1, 2)]

        # go through layers in reverse!
        for layer in range(self.m-1,-1,-1):

            # loop over even qubits (in reverse order!) if layer is even
            if layer % 2 == 0:
                for qubit in even_qubits[::-1]:
                    # end iteration before we get to end_index
                    if gate_index <= start_index:
                        return self.right

                    self.unitaryR(qubit, gate_index)  # apply unitary to right
                    gate_index -= 1

            # loop over odd qubits if layer is odd
            if layer % 2 == 1:
                for qubit in odd_qubits[::-1]:
                    # end iteration before we get to end_index
                    if gate_index <= start_index:
                        return self.right
                    
                    self.unitaryR(qubit, gate_index)  # apply unitary to right
                    gate_index -= 1

        return self.right