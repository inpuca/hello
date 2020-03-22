import numpy as np
#求解伴随矩阵
A = np.array([[1,2,3],[2,3,1],[3,1,2]])
A_det=np.linalg.det(A)
A_1=np.linalg.inv(A)
A_companions=A_1*A_det
print(A_companions)