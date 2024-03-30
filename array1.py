import numpy as np


a=np.array([[23,56,67,9,78,8]])                # 1 dimensional array
print(a)
print(a.size)
print(len(a))


print(a[0, 1])                  # getting index of 0 row and 1 colum
print(a.shape)                  # getting dimension of array



#    changing particular index
a[0,2]=76
print(a)
print(a.size)



