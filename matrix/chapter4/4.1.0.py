"""
当［x，y］=0时，称向量x与y正交,内积=0时，正交
如果α≠0，取 b=a/||a||则β是一个单位向量,称之为单位化
下面的包实现了施密特（Schmidt）正交化
https://blog.csdn.net/ouening/article/details/83279894
https://www.cnblogs.com/fengyubo/p/10516798.html
手写正交化
https://blog.csdn.net/panghaomingme/article/details/60963918
"""
import common.rsmat as rs
import numpy as np
from sympy.matrices import Matrix, GramSchmidt
A=np.array([[1,1,2],[-4,2,2]])
y=rs.rsmat(A)
l = [Matrix([1,2,-1]), Matrix([-1,3,1]), Matrix([4,1,0])]
o = GramSchmidt(l)
print(o)
a = [Matrix([1,0,-2]), Matrix([1,4,1]), Matrix([-1,1,1])]
A=GramSchmidt(a,True)
print(A)

