# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oiA3hNv0jobbJwUrrYQyuqyLfrjmRbLA
"""

import matplotlib.pyplot as plt

x1=[0,1,2,3,4,5]
y1=[5,4,3,2,1,0]
plt.plot(x1,y1,label='x1+x2=5')
x2=[2,2,2,2,2]
y2=[1,2,3,0,-1]
plt.plot(x2,y2,label='x1=2')
x3=[-1,0,1,2]
y3=[3,3,3,3]
plt.plot(x3,y3,label='x2=3')
x4=[2]
y4=[3]
plt.plot(x4,y4,marker='o')
plt.xlim(-1,7)
plt.ylim(-1,7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()
plt.show()

import matplotlib.pyplot as plt

x1=[0,1,2,3,4,5]
y1=[5,4,3,2,1,0]
plt.plot(x1,y1,label='x1+x2=5')
x2=[1,1,1,1]
y2=[-1,0,1,2]
plt.plot(x2,y2,label='x1=1')
x3=[-1,0,1]
y3=[2,2,2]
plt.plot(x3,y3,label='x2=2')
x4=[1]
y4=[2]
plt.plot(x4,y4,color='purple',marker='o')
plt.xlim(-1,7)
plt.ylim(-1,7)
plt.legend()
plt.show()

import matplotlib.pyplot as plt

x1=[0,1,2,3,4,5]
y1=[5,4,3,2,1,0]
plt.plot(x1,y1,label='x1+x2=5')
x2=[4,4,4,4,4,4]
y2=[-1,0,1,2,3,4]
plt.plot(x2,y2,label='x1=4')
x3=[-1,0,1,2,3,4]
y3=[4,4,4,4,4,4]
plt.plot(x3,y3,label='x2=4')
x4=[4]
y4=[4]
plt.plot(x4,y4,color='purple',marker='o')
x5=[1,2,3,4]
y5=[4,3,2,1]
plt.plot(x5,y5,color='red',marker='o')
plt.xlim(-1,7)
plt.ylim(-1,7)
plt.legend()
plt.show()

