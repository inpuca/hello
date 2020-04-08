import numpy as np

def gram_schmidt(X):
    O = np.zeros(X.shape)
    for i in range(X.shape[1]):
        # orthogonalization（正交化）
        vector = X[:, i]
        space = O[:, :i]
        projection = vector @ space
        vector = vector - np.sum(projection * space, axis=1)
        # normalization（归一化）
        norm = np.sqrt(vector @ vector)
        vector /= abs(norm) < 1e-8 and 1 or norm

        O[:, i] = vector
    return O

a = np.array([[1,0,2],[1,4,1],[-1,1,1]])
y=gram_schmidt(a)
m = np.array(y)
print(y)
print(round((m[1]*m[2]).sum(),2))
x_norm=np.linalg.norm(m, ord=2, axis=0, keepdims=False)
print(x_norm)
