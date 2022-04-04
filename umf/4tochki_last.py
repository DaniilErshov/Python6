# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:04:38 2022

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt 

def f(p,u1,u2,t,h,q):
    u2[p] = u1[p] - t / (2*h) * (u1[p+1] - u1[p-1]) + (t**2*q/h**2)*(u1[p-1] - 2*u1[p] + u1[p+1])








m_lst = ["100", "500","1000", "5000", "10000"]
N = 10000
t_except = 0.9
x_all = 3
t = t_except / N
for step in m_lst:
  M = int(step)
  h = 3 / M
  u0 = np.zeros(M + 1)
  u1 = np.zeros(M + 1)
  u2 = np.zeros(M + 1)
  for i in range(int(0.1/h), int(0.2/h) + 1):
      u1[i] = 1.
      u0[i] = 1.
  for tmp in range(0, N):
      for p in range(1, M):
        f(p, u1, u2, t, h, 0.5) 
      u1 = u2
      u2 = np.zeros(M + 1)
  x_array = [i * h for i in range(M+1)]
  plt.plot(x_array, u1, label = step)

exact = np.zeros(M + 1)
for i in range(int(0.1/h + M *t_except/x_all), int(0.2/h + M *t_except/x_all)):
    exact[i] = 1 
    
plt.plot(x_array, exact)  
  
plt.legend()
plt.show() 
