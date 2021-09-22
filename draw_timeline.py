# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:07:13 2021

@author: Krepana Krava
"""
import numpy as np
import matplotlib.pyplot as plt

execution_times = np.load('twoopttimeschedule.npy')

x = [item[0] for item in execution_times]
y = [item[1] for item in execution_times]
plt.plot(x, y, linewidth=1)
plt.plot(x, y, 'ro', markersize=1)
plt.xlim((0, 50))
#plt.title(title)
fig = plt.gcf()
fig.savefig('test2png.png', dpi=600)