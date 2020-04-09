import numpy as np
#A = np.array([[0,1,1],[1,0,1],[1,1,0]])
#A = np.array([[2,-1,1],[0,1,1],[-1,1,1]])
A = np.array([[1,2,4,1],[0,2,0,7],[0,0,3,4],[0,0,0,2]])
v,a = np.linalg.eig(A)#特征值保存在a中，特征向量保存在b中
v1,a1=np.linalg.eig(A.T)
print(v)
print(np.around(a,decimals=2))
#用公式Aa=va,验证是否正确
for i in range(3):#方法一
    if np.allclose(np.dot(v[i], a[:, i]), np.dot(A,a[:,i])):#np.allclose()方法在第七节提到过
        print ('Right')
    else:
        print ('Error')