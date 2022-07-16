In [1]: import numpy as np
   ...: data = np.array([
   ...:     [34, 175, 72],
   ...:     [22, 136, 50]
   ...: ])
   ...: tens = np.array([
   ...:     [10, 10, 10],
   ...:     [10, 10, 10]
   ...: ])
   ...:
   ...: np.add(data, tens)

Out[1]:
array([[ 44, 185,  82],
       [ 32, 146,  60]])