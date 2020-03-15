import numpy as np
a = np.arange(24)
print(a)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b)
print(b.ndim)

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)