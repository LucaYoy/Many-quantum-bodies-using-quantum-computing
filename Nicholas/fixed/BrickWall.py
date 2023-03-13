import numpy as np
import Gates as g
import ExactDiagonalization as ed
from scipy.stats import unitary_group as U
import matplotlib.pyplot as plt

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
    
    def remove_gate(self, index):
        """ Applies gates using brick_wall up to before the 'removed' gate, and
        brick_wallR up to after the 'removed gate'. Then joins the two halves together
        to create a new gate
        """
        # Apply brick_wall up to index
        left_circuit = self.brick_wall(end_index=index)
        # Apply brick_wallR starting at index+1
        right_circuit = self.brick_wallR(start_index=index+1)
        
        qubit_map = []
        # Create a qubit map which determines which qubit the gates are applied on
        for i in range(self.m):
            for j in range(0, self.n-1, 2):
                qubit_map.append(j)
            for k in range(1, self.n-1, 2):
                qubit_map.append(k)
        # Make sure the qubit map doesn't exceed the total number of gates        
        qubit_map = qubit_map[0:self.num_gates] 
        # Set a variable for the qubit where the removed gate would be applied
        removed_gate_qubit = qubit_map[index]  
        
        # Determine the axes of psi and phi to use for tensor dot product
        psi_axes = list(range(self.n))
        phi_axes = list(range(self.n))
        
        # Remove the axes of the removed gate from left circuit
        psi_axes.remove(removed_gate_qubit)
        psi_axes.remove(removed_gate_qubit + 1)
        # Remove the axes of the removed gate from right circuit
        phi_axes.remove(removed_gate_qubit)
        phi_axes.remove(removed_gate_qubit + 1)

        # Take the tensor product of both sides along the remaining axes
        E = np.tensordot(left_circuit, right_circuit,((psi_axes),(phi_axes)))
        
        # Re-order the axes for later use
        E = E.transpose(2,3,0,1) 

        return E
    
    def optimize_circuit(self, max_iterations, min_overlap_change, plot=True):
        """ Removes and replaces gates with the best possible gate in order to 
        give the largest overlap
        """
        
        # Create empty lists of any vairables that need to be stored
        overlaps = []
        overlapsold = []
        relative_errors = []
        iterations = 0
        overlap_change = float('inf') 
                           
        for i in range(max_iterations):    
            
            for index in range(self.num_gates):
                # Remove each gate one by one    
                E = self.remove_gate(index)
                # The old overlap simply replaces the removed gate    
                overlap_old = np.tensordot(E, self.gates[index], 4) 
                   
                # Perform singular-valued decomposition to generated the best gate 
                U,s,Vh = np.linalg.svd(np.conjugate(E.reshape(4,4)))
                U_new = np.matmul(U,Vh).reshape(2,2,2,2)
                
                # The new overlap uses the newly generated gate                    
                overlap_new = np.tensordot(E, U_new, 4)
                # Replace the list of old gates with the new gates
                self.gates[index] = U_new    
                             
                relative_error = abs(overlap_new) - abs(overlap_old) 
                # Add a check to make sure the gates are being generated correctly
                if abs(overlap_new) < abs(overlap_old):
                    print("Error, overlap isn't increasing")

            overlaps.append(1-(abs(overlap_new)))

            relative_errors.append(relative_error)  
            
            # Calculate the change in overlap between the old and new overlaps
            if iterations > 0:
                overlap_change = abs(overlaps[-1] - overlaps[-2])
                
            if min_overlap_change > overlap_change:
                print(f"Stopped after iteration {iterations} with final overlap {overlaps[-1]}")
                break
            
            # Plot the overlap against the number of iterations (optional)
            if plot:
                plt.plot(range(iterations+1), overlaps, 'b')
                plt.xlabel("Number of iterations")
                plt.ylabel("1 - Overlap")
                plt.show()
        
            iterations += 1
      
            
        if overlap_change > min_overlap_change:

            print(f"Stopped after {iterations} iterations, with final overlap {overlaps[-1]}")  

        final_psi = self.brick_wall()
        #print(abs(np.tensordot(final_psi, self.phi, axes=self.n)))
                              
        return relative_errors, overlaps, final_psi
        
    