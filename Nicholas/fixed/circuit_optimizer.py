import BrickWall as bw 
import matplotlib.pyplot as plt
import time
import numpy as np
start_time = time.time()
# To graph the overlap

Qubits = 6
H = 1
J = 1
G = 1
Layers = 5
iterations = 50

fig, ax = plt.subplots(figsize=(16,14))
for i in range(1):
    Circuit = bw.Circuit(Qubits, Layers, J ,H, G, gatesrandom=False)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    _,overlaps,_, iterations,_, gatesflat= Circuit.optimize_circuit(iterations, 10**-6, show_overlap=True, 
                                                          stopped_flag=False
                                                          , optimizationnew=True )
    
    flag = False
    for i in range(len(overlaps) -1, 0, -1):
        if abs(overlaps[-1] - overlaps[i]) > 0.0001:
            x_cutoff = i
            flag=True
            break
        #index = i
        #x_cutoff = iterations[index]
        
    #if flag is True:
    #    plt.xlim(1, x_cutoff)
    
    plt.plot(range(iterations), overlaps)#, label=f"{Layers} Layers")
    plt.xlabel("Number of iterations")
    plt.ylabel("1 - Overlap")
#plt.axhline(y=10**-14, color='k', linestyle='dashed', label="Exact")
plt.xscale("log")
plt.yscale("log")
#plt.xlim(1,iterations)
plt.title(f"J={J},h={H}, Gates close to identity, {Layers} Layer, Qubits = {Qubits}, {iterations} iterations")
plt.show()

#gates = [np.reshape(elem, (4,4)) for elem in gatesflat]

#gatesfloat = []
#for gate in gatesflat:
#    gatesfloat.append(float(gate.real))
#    gatesfloat.append(float(gate.imag))
    
    
    
print ("Took", time.time() - start_time, "seconds to run")

