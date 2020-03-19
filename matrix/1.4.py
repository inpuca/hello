import numpy as np
A = np.array([[1, -2, 1], [0, 2, -1], [1, 1, -2]])
A_det = np.linalg.det(A) #求A的行列式，不为零则存在逆矩阵
A_inverse = np.linalg.inv(A) #求A的逆矩阵
print(A_det)
#print(A_inverse)
E=np.dot(A, A_inverse) # 若可逆则AB=BA=E
O=np.around(E,decimals=2) #输出只保留两位小娄
print(O)
# 下面是习题1-4，第2题
A = np.array([[5,-2], [3,0]])
P= np.array([[1,2], [1,3]])
mytest= np.array([[9,-6], [-2,2]])
p_det=np.linalg.det(P)
#if np.around(p_det,decimals=2)!=0.00 :
p_inverse = np.linalg.inv(P)
print(p_inverse)
P_1A=np.dot(p_inverse,A)

P_1AP=np.dot(P_1A,P)
print("3-----------------")
print(P_1AP)
print(np.power(P_1AP,10))
print(np.dot(p_inverse,P))


