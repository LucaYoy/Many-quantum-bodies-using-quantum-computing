# Many quantum bodies using quantum computing
In this project we aim to build a quantum circuit that will approximate a ground state of a many body system.
## Procedure
* Find the exact ground state (target state) using exact diagonalization
* Use a brick wall structure circuit for the quantum circuit approximation
* Carry optimization on the parameters of the circuit to find the parameters that minimze the infidelity
* Once optimization is complete, use the quantum circuit approximation to measure different correlation functions like the entropy,energy and mutual information
* Do the measurements also on the exact state and compare
* Analyze the results and see what they infer about the quantum circuit
## Tech stack
* Vanilla Python
* Numpy
* Matplotlib
* Linux scripting
* Augusta HPC 
