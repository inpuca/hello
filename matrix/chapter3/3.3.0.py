""" 矩阵的行向量组的秩与它的列向量组的秩相等，都等于矩阵的秩"""
import numpy as np
print("------求解矩阵的秩--------")
""" 求解矩阵的秩"""
A = np.array([[1,1,2,3],[-1,2,0,1],[0,3,2,4]])
B = np.array([[2,-3,4,4,5],[0,-2,1,-1,3],[0,0,0,0,4],[0,0,0,0,0]])
R_A=np.linalg.matrix_rank(A);
print(R_A)
print(np.linalg.matrix_rank(B))
A = np.array([[1,-1,0,-1],[1,3,2,2],[3,1,-4,4]])
B = np.array([[1,1,1,1,-1],[2,1,3,-1,1],[1,2,0,6,-2],[4,3,5,-1,-3]])
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(B))