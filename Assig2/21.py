import numpy as np
import matplotlib.pyplot as plt

x=[0,1]
y=[1,1]
for z in range(2,10):
    c=y[z-1]+y[z-2]
    y+=[c]
    x+=[z]

#subplots
plt.subplot()
plt.stem(x,y)
plt.ylabel('$x(n)$')
plt.grid()# minor
plt.savefig('21.png')
