# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:56:25 2020

@author: 12786
"""
import numpy as np
import random
import math

result = []
x = [random.uniform(-1,1), random.uniform(-1,1)]
y = [math.sin(i*math.pi) for i in x ]
b0 = (y[0]+y[1])/2
a1 = (y[0]-y[1])/(x[0]-x[1])
b1 = y[0] - a1*x[0]


bias_sq0 = (y[0]-b0)**2 + (y[1]-b0)**2
bias_sq1 = (y[0]-a1*x[0]-b1)**2 + (y[1]-a1*x[1]-b1)**2

#假设1，预测的均值是b0；假设2，预测的均值是(y0+y1)/2
var0 = 0
var1 = ((a1*x[0]+b1)-b0)**2 +((a1*x[1]+b1)-b0)**2
result.append([bias_sq0, bias_sq1, var0, var1])
print(result)
