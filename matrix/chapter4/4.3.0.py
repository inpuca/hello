"""
P-1 AP=B,对A进行运算P -1 AP称为对A进行相似变换
定理一：若n阶矩阵A与B相似，则A与B有相同的特征多项式，从而A与B有相同的特征值．
定理二：n阶矩阵A与对角阵相似（即A能对角化）的充分必要条件是A有n个线性无关的特征向
量
推论：如果n阶矩阵A的n个特征值互不相等，则A与对角阵相似

相似矩阵：秩，迹，行列式，特征值，特征向量都相等，可逆或都不可逆

"""
import numpy as np
import common.rsmat as rs
from sympy import Matrix
#A = np.array([[3,2,-1],[-2,-2,2],[3,6,-1]])#
#A = np.array([[-3,1,-1],[-7,5,-1],[-6,6,-2]])#
A = np.array([[2,-1,2],[5,-3,3],[-1,0,-2]])#
v,a = np.linalg.eig(A)#特征值保存在a中，特征向量保存在b中
a_rank=np.linalg.matrix_rank(a)
print(v)
print(np.around(a,decimals=2))
y=rs.rsmat(a)
print(y)
#第二种方法求最简阵
#A_rref = np.array(Matrix(a).rref()[0].tolist()).astype(np.float)
#print(A_rref)
#用公式Aa=va,验证是否正确
for i in range(3):#方法一
    if np.allclose(np.dot(v[i], a[:, i]), np.dot(A,a[:,i])):#np.allclose()方法在第七节提到过
        print ('Right')
    else:
        print ('Error')