"""
如果α 1 ，α 2 ，…，α r 是向量空间V的一个基，则V中任一向量β可唯一线性表示为
β=λ 1 α 1 +λ 2 α 2 +…+λ r α r ，
则称常数λ 1 ，λ 2 ，…，λ r 为向量β在基α 1 ，α 2 ，…，α r 下的坐标．
"""
import numpy as np
A = np.array([[1,2,-1],[0,1,1],[1,-1,-3]])
B=np.array([[2],[-1],[6]])
A_det=np.linalg.det(A)
#AX=B,X=A_-1*B
#print(A_det)
A_inv=np.linalg.inv(A)
print(np.dot(A_inv,B))


