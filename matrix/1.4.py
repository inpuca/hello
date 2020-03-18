import numpy as np
A = np.array([[1, -2, 1], [0, 2, -1], [1, 1, -2]])
A_det = np.linalg.det(A) #求A的行列式，不为零则存在逆矩阵
A_inverse = np.linalg.inv(A) #求A的逆矩阵
print(A_det)
#print(A_inverse)
E=np.dot(A, A_inverse) # 若可逆则AB=BA=E
O=np.around(E,decimals=2) #输出只保留两位小娄
print(O)
