import matplotlib.pyplot as plt
import numpy as np
import lcg
import bbs
import lfsr


lcg = lcg.LCG() 

bbs = bbs.BBS()

lfsr = lfsr.LFSR()

figure, subplt = plt.subplots(2,2)

x = lcg.random(100000)
y = lcg.random(100000)
subplt[0,0].plot(x, y, ls='', marker=',', markeredgecolor='none')
subplt[0,0].set_title("Linear Congruential Generator")

x = bbs.random(100000)
y = bbs.random(100000)
subplt[0,1].plot(x, y, ls='', marker=',', markeredgecolor='none')
subplt[0,1].set_title("Blum Blum Shub Generator")

x = np.random.random(100000)
y = np.random.random(100000)
subplt[1,0].plot(x, y, ls='', marker=',', markeredgecolor='none')
subplt[1,0].set_title("Numpy Random Generator")

x = lfsr.random(100000)
y = lfsr.random(100000)
subplt[1,1].plot(x, y, ls='', marker=',', markeredgecolor='none')
subplt[1,1].set_title("Linear Feedback Shift Generator")

plt.show()