import BrickWall as bw 
# To graph the overlap

Qubits = 8
Layers = 10

J = 3
H = 2

Circuit = bw.Circuit(Qubits, Layers, J ,H)
# Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
p=Circuit.optimize_circuit(20, 0.0001, True, False)