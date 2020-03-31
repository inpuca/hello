#线性相关，齐次方程存在一组有非零解，线性无关没有非零解
#向量组α 1 ，α 2 ，…，α m （m≥2）线性相关的充分必要条件是存在某一个向量α j （1≤j≤m）可由其余向量线性表示
#两个向量α 1 ，α 2 线性相关的充分必要条件是它们的分量对应成比例．
#部分相关，则整体相关,整体无关，则部分必无关
import numpy as np
print('---习题2-1---')#AX=B,BX=A,有解
A = np.array([[1,2,0],[1,0,1],[0,1,3]])
B = np.array([[2,3,6],[-1,6,12],[3,5,10]])
y = np.array([[3,6,9],[-2,4,11],[5,7,12]])
print(np.linalg.det(A))
print(np.around(np.linalg.det(B),decimals=2))
print(np.around(np.linalg.det(y),decimals=2))
#print(np.dot(np.linalg.inv(A),B))
#print(np.dot(np.linalg.inv(B),A))
