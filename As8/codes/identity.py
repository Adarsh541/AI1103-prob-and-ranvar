# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xlO_tB2OwburkWbIHe3IzEweRX4XF30n
"""

import numpy as np
#5x1 martrix
u=np.random.randint(100,size=(5,1))
#5x1 matrix
x=np.random.randint(100,size=(5,1))
#5x5 matrix
v=np.random.randint(100,size=(5,5))
#transpose of matrix u
ut=u.transpose()
#transpose of matrix x
xt=x.transpose()
#product of two matices
utx=ut.dot(x)
xtv=xt.dot(v)
lhs=utx.dot(xtv)
xxt=x.dot(xt)
utxxt=ut.dot(xxt)
rhs=utxxt.dot(v)
print(lhs)
print(rhs)