import numpy as np
A = np.array([[1,-1,-1],[-2,2,1],[2,-1,3]])
B = np.array([[-1],[1],[1]])
#AX=B
print(np.linalg.solve(A,B))
#X=(A_-1)B
A_det=np.linalg.det(A)
A_1=np.linalg.inv(A)
print(np.dot(A_1,B))
print('-----2-4.1题')
A = np.array([[1,-2,2],[-2,3,4],[2,-4,3]])
B = np.array([[-1],[2],[1]])
print(np.linalg.det(A))
print(np.dot(np.linalg.inv(A),B))
print('-----2-4.2题')
A = np.array([[1,-2,1],[1,1,-2],[-2,1,2]])
B = np.array([[-2],[4],[1]])
print(np.linalg.det(A))
print(np.dot(np.linalg.inv(A),B))