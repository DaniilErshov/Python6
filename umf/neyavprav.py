# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:39:33 2022

@author: Данило
"""

import copy
import numpy as np
import matplotlib.pyplot as plt 

def f(p,u1,u2,t,h):
    u2[p+1] = u2[p] - h*(u2[p] - u1[p])/t







m_lst = ["1000", "2000", "5000", "10000", "40000"]
N = 300
t_except = 0.9
x_all = 3
t = t_except / N
for step in m_lst:
  M = int(step)
  h = x_all / M
  u0 = np.zeros(M + 1)
  u1 = np.zeros(M + 1)
  u2 = np.zeros(M + 1)
  for i in range(int(0.1/h), int(0.4/h) + 1):
      u1[i] = 1.
      u0[i] = 1.
      u2[i] = 1.
  for tmp in range(0, N):
      for p in range(1, M):
        f(p, u1, u2, t, h) 
      u1 = copy.deepcopy(u2)
      u2 = copy.deepcopy(u0)
          
  x_array = [i * h for i in range(M + 1)]
  plt.plot(x_array, u1, label = step)

exact = np.zeros(M + 1)
for i in range(int(0.1/h + M *t_except/x_all), int(0.4/h + M *t_except/x_all)):
    exact[i] = 1 
    
plt.plot(x_array, exact) 
  
plt.legend()
plt.show() 