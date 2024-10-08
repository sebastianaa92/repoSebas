#PUNTO 1 RESUELTO
a = ['a','b','c','d','e','f','g','h']
b = [1,2,3,4,5,6,7,8]

lista = list(zip(a,b))

#PUNTO 2 RESUELTO
L1 = ['a','b','c','d','e','f','g','h']
L2 = [1,2,3,4,5,6,7,8]

# for i, L1i in enumerate(L1):
#     for j, L2j in enumerate(L2):
#         if i >= j:
#             print(L1i,L2j)

#PUNTO 3 RESUELTO
#from itertools import combinations
# for i in range(1,8):
#     subsets = tuple(combinations(L1, i))
#     print(subsets , end = '\n') 
 
#PUNTO 4 RESUELTO
# from itertools import product
# combinations = product(L1,L2)
# for combination in combinations:
#     print(combination)

#PUNTO 2
# import math
# coso = [math.sin(3*i + 17) for i in L2 if i % 2 != 0]
# print(coso)


# #PUNTO 2.1
# import random
# import numpy as np
# random.shuffle(L1)
# coso2 = np.argsort(L1)
# sorted(coso2)
# print(coso2)


#PUNTO 2 MACRO

import numpy as np
n = 100
x = np.ones(n)
# print(x)

start = 3
y = np.arange(start,3 * (n+1),3)
#print(y)

y2 = np.round(15 * np.sin(y))
#print(y2)

# indices = np.where(y2 > 6)
# contar_cincos = np.sum(y2==5)
# print("Coso",indices)
# print("Cosos",contar_cincos)


M = np.vstack([y,y2])
print(M)

M2 = np.column_stack([y.T, y2.T])
print(M2)