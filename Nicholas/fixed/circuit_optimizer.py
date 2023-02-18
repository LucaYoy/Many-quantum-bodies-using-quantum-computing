import BrickWall as bw 

Qubits = 4
Layers = 3
J = 3
H = 2

Circuit = bw.Circuit(Qubits, Layers, J ,H)
Circuit.optimize_circuit(20, 0.0001)
