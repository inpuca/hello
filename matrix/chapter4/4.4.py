"""
实对称矩阵:如果有n阶矩阵A，其矩阵的元素都为实数，且矩阵A的转置等于其本身（aij=aji）(i,j为元素的脚标），则称A为实对称矩阵
性质：
    1.实对称矩阵A的不同特征值对应的特征向量是正交的。
    2.实对称矩阵A的特征值都是实数，特征向量都是实向量。
    3.n阶实对称矩阵A必可相似对角化，且相似对角阵上的元素即为矩阵本身特征值。
    4.若A具有k重特征值λ0　必有k个线性无关的特征向量，或者说秩r(λ0E-A)至多为n-k，其中E为单位矩阵。
"""
import numpy as np
