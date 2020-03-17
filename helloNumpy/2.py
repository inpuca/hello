import numpy as np
a = np.array([[0, 1, 2, 3, 4],[1,2,3,4,5]])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

print(a) # >>>[0 1 2 3 4]
print(b) # >>>[0 1 2 3 4]
print(c) # >>>[0 1 2 3 4]
print(d) # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
print(a[1,3]) # >>>3
print("1------------------------------")
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

print(a[2, 4])  # >>>25
print("2-----------------------------------------")
# MD slicing
print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15] 步长为2
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]
print("3-----------------------------------------")
# Incomplete Indexing
a = np.arange(0, 100, 10)
print(a)
b = a[:5]
c = a[a >= 50]
print(b) # >>>[ 0 10 20 30 40]
print(c) # >>>[50 60 70 80 90]
print("4----------------------------------")
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)
# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
print("5----------------------------------------------------")

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))
