import matplotlib.pyplot as plt
import numpy as np
import rng
import lcg

lcg = lcg.LCG() 


x = lcg.random(100000)
y = lcg.random(100000)
plt.plot(x, y, ls='', marker=',', markeredgecolor='none')

plt.show()