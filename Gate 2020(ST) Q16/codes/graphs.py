# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1siwhDrYNv8j5oBat7JWL8YOI4IxvoCz-
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import abs

def rect1(x):
    if (abs(-x/4)<=0.5):
        return 1/4 
    else:
       return 0

X = np.linspace(-3,3,1000000)

Y = [rect1(x) for x in X]
plt.xlabel('X')
plt.ylabel('$pdf$')
plt.plot(X,Y)
plt.grid()
plt.savefig('Assignment5.png' , dpi=100)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from numpy import abs

def rect(x):
    if (abs(x)<=0.5):
        return 1
    elif (abs(x) == 0.5):
      return 1/2     
    else:
       return 0

X = np.linspace(-2,2,1000000)

Y = [rect(x) for x in X]
plt.xlabel('X')
plt.ylabel('$rect(x)$')
plt.plot(X,Y)
plt.grid()
plt.savefig('rect.png' , dpi=100)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from numpy import abs
import math

def sinc(x):
    if (x==0):
        return 1    
    else:
       return (math.sin((math.pi)*x))/((math.pi)*x)

X = np.linspace(-4,4,1000000)

Y = [sinc(x) for x in X]
plt.xlabel('x')
plt.ylabel('$sinc(x)$')
plt.plot(X,Y)
plt.grid()
plt.savefig('sinc.png' , dpi=100)
plt.show()