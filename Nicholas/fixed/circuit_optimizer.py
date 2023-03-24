import BrickWall as bw 
import matplotlib.pyplot as plt
# To graph the overlap

Qubits = 4
H = 1
J = 1
Layers = 5
iterations = 1000
for i in range(5):
    Circuit = bw.Circuit(Qubits, Layers, J ,H, gatesrandom=True)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    _,overlaps,_, iterations,_ = Circuit.optimize_circuit(iterations, 10**-12, show_overlap=True, 
                                                          stopped_flag=False
                                                          , optimizationnew=False )
    
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
