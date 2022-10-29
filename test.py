import numpy as np
import matplotlib.pyplot as plt 


x = np.arange(0,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
args = [x,y1]
plt.plot(*args, label = "hello")
plt.title("example")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()