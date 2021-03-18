
# coding: utf-8

# In[65]:

""" This is a simple module to create a sine wave"""
import math
import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,45,90,135,180,225,270,315,360])
y=np.array([0,0,0,0,0,0,0,0,0],dtype=float)
z=np.array([0,0,0,0,0,0,0,0,0],dtype=float)
#print(y)
for e in range(0,8):
    #print(round(math.sin(math.radians(x[e])),3))
    y[e]=round(math.sin(math.radians(x[e])),3)
    z[e]=round(math.cos(math.radians(x[e])),3)
#print(y)
plt.xlabel("Angle")
plt.ylabel("Sine values")
plt.plot(x,y)
plt.savefig('sine.pdf', format='pdf')
plt.show()
plt.close()
plt.xlabel("Angle")
plt.ylabel("Cosine values")
plt.plot(x,z)
plt.savefig('cosine.pdf', format='pdf')
plt.show()
plt.close()
print(math.sin(math.radians(90)))
print("End of run")
