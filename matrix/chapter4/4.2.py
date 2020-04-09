"""
|A-λE|=0,A的特征值就是特征方程的根

"""
import numpy as np
A = np.diag((1, 2, 3))#创建一个对角矩阵！
v,a = np.linalg.eig(A)#特征值保存在a中，特征向量保存在b中
print(v)
print(a)
#用公式Aa=va,验证是否正确
for i in range(3):#方法一
    if np.allclose(np.dot(v[i], a[:, i]), np.dot(A,a[:,i])):#np.allclose()方法在第七节提到过
        print ('Right')
    else:
        print ('Error')
