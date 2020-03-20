import numpy as np
#所有元素都是零的m×n矩阵称为零矩阵，记为O m×n ，或简记为O
#E n阶对角阵，对角线上全是1，叫单位阵，记为1
#（A T ） T =A；
#（A+B） T =A T +B T ;
#（AB） T =B T A T ;
#（kA） T =kA T
#求(AB).T
A= np.array([[2,-1,3], [1,1,1]])
B = np.array([[1,-1],[0,2],[-1,1]])
print(np.dot(B.T,A.T))
print(np.dot(A,B).T)
print('#1.1-3')#3
A= np.array([[3,-1,2], [2,1,-2]])
B = np.array([[1,5,1],[-2,-1,0]])
print(A+2*B)
print(3*A-B)
print(np.dot(A,B.T))
print(np.dot(A.T,B))
print('#1.1-5')#3
A= np.array([[1,0,0], [0,1,2],[0,2,1]])
B = np.array([[1,0,0],[0,2,5],[0,5,2]])
print(np.power(A,3))
print(np.linalg.matrix_power(A,2))
print(np.dot(A,A))
print(np.dot(A,A)+3*A-2*B)
print('#1.1-6')#3
A= np.array([[1],[2],[3]])
B = np.array([[3,-2,1]])
print(np.dot(A,B))
A= np.array([[2,3,1]])
B = np.array([[1],[-1],[2]])
print(np.dot(A,B))
