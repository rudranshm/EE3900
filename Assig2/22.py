import numpy as np
import matplotlib.pyplot as plt

x=[0,1]
y=[1,1]
j=[0,1]
for z in range(2,10):
    c=y[z-1]+y[z-2]
    y+=[c]
    x+=[z]
    j+=[y[z-2]+y[z]]

#subplots
plt.subplot()
plt.stem(x,j)
plt.ylabel('$x(n)$')
plt.grid()
plt.savefig('22.png')