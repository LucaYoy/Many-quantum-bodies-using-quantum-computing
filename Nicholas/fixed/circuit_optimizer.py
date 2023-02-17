import BrickWall as bw #I think this name will be changed tp the name of what my full brick wall file is named

Qubits = 4
Layers = 3
J = 3
H = 2

Circuit = bw.Circuit(Qubits, Layers, J ,H)
Circuit.optimize_circuit(20, 0.0001)