import numpy as np
print("-------3-1.2题---------")
a = np.array([[1],[2],[3]])
b= np.array([[1,0,1],[1,1,-1],[1,-1,0]])
b_det=np.linalg.det(b)
print(b_det)
print(np.dot(np.linalg.inv(b),a))
#问题：线性方程有解充要条件，矩阵方程有解充要条件，这个问题要解决