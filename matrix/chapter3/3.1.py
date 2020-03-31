"""
#向量组，维数相同的向量称为向量组
#向量一般说的是列向量
#a1*x1=(列的逐个元素乘以x1)
#线性组合 a1x1+a2x2+a3x3=b
#向量b能否用向量组(a1,a2,a3)线性表示，就看能线性方程a1x1+a2x2+a3x3=b，是否有解

#能否线性表示的充要条件：（唯一）线性表示的充分必要条件是线性方程组x 1 α 1 +x 2 α 2 +…+x n α n =β有（唯一）解

#print(np.linalg.det(A))
#print(np.dot(np.linalg.inv(A),B))
#很明显上面都是无解或多解的
#相互能够线性表示，称之为等价向量组，双向有解就是等价
# B向量组能否由向量组A线性表示，AX=B的矩阵方程是否有解
#单向有解能线性表示，双向有解就是等价

"""
import numpy as np

print('---例4---')
A = np.array([[1,0,-1],[1,2,1],[-1,1,2]])
B = np.array([[5],[3],[6]])
#print(np.linalg.det(A))
#print(np.dot(np.linalg.inv(A),B))
print('---例5---')
A = np.array([[1,2,-3],[0,1,2],[-2,-5,4]])
B = np.array([[5],[4],[-7]])

print('---例6---')
A = np.array([[1,-2],[1,0],[-1,1]])
B = np.array([[3,-3,-1],[1,1,1],[-2,1,0]])
#AX=B,B能否由A线性表示,X=(A_-1)*B
#print(np.linalg.det(A))
#print(np.linalg.solve(A,B)) 无解，非方阵不能求逆，也不能用SOLVE来解决，待解决这个问题
print('---例7---')#AX=B,BX=A,有解
A = np.array([[1,-1,1],[0,1,2],[-1,2,5]])
B = np.array([[1,0,1],[1,1,0],[0,1,1]])
print(np.linalg.det(A))
print(np.linalg.det(B))
print(np.dot(np.linalg.inv(A),B))
print(np.dot(np.linalg.inv(B),A))

