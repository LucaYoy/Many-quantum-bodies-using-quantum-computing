import BrickWall as bw 


Qubits = 6
Layers = 8

J = 3
H = 2

Circuit = bw.Circuit(Qubits, Layers, J ,H)
p=Circuit.optimize_circuit(20, 0.0001, False)