"""
向量空间的基=极大无关组
向量空间的维数=向量组的秩
基变换:B=AP，称之为从旧基到新基的变换公式,旧基是A，新基是B,
P=A_-1*B，称之为过渡矩阵
坐标变换:b=p_-1*a，称之为从旧标a到新标b的变换公式
"""
import numpy as np
a = np.array([[1,1,0],[1,0,1],[0,1,1]])
x=np.array([[8],[-2],[4]])
B=np.array([[1,1,-1],[1,2,2],[-2,3,1]])
#求P_-1*a=b,b=P_-1*a
"""A=a*x"""

a_inv=np.linalg.inv(a)
P=np.dot(a_inv,B)
P_inv=np.linalg.inv(P)
b=np.dot(P_inv,x)
print(b)

