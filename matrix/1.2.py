import numpy as np
A = np.array([[3,1,0,0],[2,1,0,0],[0,0,1,4],[0,0,2,5]])
B = np.array([[-1,0,1,0],[0,-1,0,1],[3,0,2,1],[1,-1,1,2]])
C = np.array([[2,4,0,0],[1,3,0,0],[0,0,3,1],[0,0,0,2]])
B_T = np.transpose(B)

w = np.dot(A,C)
AB=np.dot(A,B)
B_TA=np.dot(B.T,A)
print(AB-B_TA)
#  print(w)