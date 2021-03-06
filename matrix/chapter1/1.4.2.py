import numpy as np
print('''求解矩阵方程AX=B,X=（A_-1)B''')
A = np.array([[-1,4], [-2,7]])
B= np.array([[2,-1,3], [1,0,-2]])
if np.around(np.linalg.det(A),decimals=2)!=0.00 :
    X=np.dot(np.linalg.inv(A),B)
    print(X)
print(np.linalg.solve(A,B))
print('''求解矩阵方程XA=B,X=B（A_-1)''')
A = np.array([[1,0,-2],[0,-2,1],[-2,-1,5]])
B= np.array([[-1,1,0], [1,2,-1]])
#XA=B,X=B（A_-1)
A_det=np.linalg.det(A)
A_inverse=np.linalg.inv(A)
print(np.dot(B,A_inverse))
print('''求解矩阵方程AXB=C,X=(A_-1)C(B_-1)''')
A= np.array([[1,1], [-1,-2]])
B = np.array([[-1,1,0],[0,1,-1],[1,0,-2]])
C = np.array([[1,-1,0],[-1,0,1]])
A_det=np.linalg.det(A)
B_det=np.linalg.det(B)
A_1=np.linalg.inv(A)
B_1=np.linalg.inv(B)
A_1C=np.dot(A_1,C)
X=np.dot(A_1C,B_1)
print(X)

'''print(np.linalg.solve(A,B)) #solve仅适用于ax=b，求解线性方程用，
 a要求是方阵且线性独立，不然出错，详看源码envs\aidev\Lib\site-packages\numpy\linalg\linalg.py'''

