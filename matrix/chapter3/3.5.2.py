import numpy as np
import common.rsmat as rs
print("习题第3题")
a = np.array([[1,2,2,3,-1],[2,2,3,2,-1],[3,2,1,1,2],[-1,-1,1,-1,-2]])
print(np.linalg.matrix_rank(a))
y=rs.rsmat(a)
print(y)
print("习题第4题")
A= np.array([[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]])
a=np.array([[1],[1],[2],[1]])
c=np.array([[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,2],[0,0,0,1,1]])
c_simple=rs.rsmat(c)
#a=A*x,x=A_-1*a
A_inv=np.linalg.inv(A)
x=np.dot(A_inv,a)
print(x)
B=np.array([[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]])
#求a到b的过渡矩阵,b=ap,p=a_-1*b
A_inv=np.linalg.inv(A)
P=np.dot(A_inv,B)
print(P)
#求向量a在基B下的坐标,a=B*y,a=A*x,所以:y=x*P_-1
P_inv=np.linalg.inv(P)
y=np.dot(P_inv,x)


