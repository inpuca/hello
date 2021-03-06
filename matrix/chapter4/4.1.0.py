"""
当［x，y］=0时，称向量x与y正交,内积=0时，正交
如果α≠0，取 b=a/||a||则β是一个单位向量,称之为单位化
下面的包实现了施密特（Schmidt）正交化
https://blog.csdn.net/ouening/article/details/83279894
https://www.cnblogs.com/fengyubo/p/10516798.html
m[0]表示0行,m[:,0]表示0列
"""
import common.rsmat as rs
import numpy as np
from sympy.matrices import Matrix, GramSchmidt
import common.gram_schmidt as schmidt
A=np.array([[1,1,2],[-4,2,2]])
y=rs.rsmat(A)
l = [Matrix([1,2,-1]), Matrix([-1,3,1]), Matrix([4,1,0])]
o = GramSchmidt(l)
print(o)
a = [Matrix([1,0,-2]), Matrix([1,4,1]), Matrix([-1,1,1])]
A=GramSchmidt(a,True)
print("-------------")
print(A)
print("-----2--------")
l = [Matrix([1,1,-1]), Matrix([1,2,3]), Matrix([2,3,5])]
o = GramSchmidt(l,True)
m = np.array(o)
print(m)

print(round((m[:,1]*m[:,2]).sum(),2))

print("-----2.1--------")
a = np.array([[1,1,-1],[1,2,3],[2,3,5]])
y=schmidt.gram_schmidt(a)
m = np.array(y)
print(y)
print(round((m[:,0]*m[:,2]).sum(),2))
x_norm=np.linalg.norm(m, ord=2, axis=0, keepdims=False)
print(x_norm)
print("-----2.2--------")
a = np.array([[1,1,-1],[-1,0,0],[0,-1,0],[0,0,1]])
y=schmidt.gram_schmidt(a)
m = np.array(y)
print(y)
print(round((m[:,0]*m[0:,1]).sum(),2))
x_norm=np.linalg.norm(m, ord=2, axis=0, keepdims=False)
print(x_norm)
print("-----2.3--------")
