import BrickWall as bw 
import matplotlib.pyplot as plt
# To graph the overlap

Qubits = 8
#Layers = 5
H = 1
J = 1.5
for Layers in range(1,7):
    Circuit = bw.Circuit(Qubits, Layers, J ,H, gatesrandom=False)
    # Sweeps, Accuracy, ShowGraph?, ShowFinalOverlap?
    _,overlaps,_, iterations=Circuit.optimize_circuit(5000, 0.000000001, True, True)
    
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
    
    plt.plot(range(iterations), overlaps, label=f"{Layers} Layers")
    plt.xlabel("Number of iterations")
    plt.ylabel("1 - Overlap")
plt.axhline(y=0, color='k', linestyle='dashed', label="Exact")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()
