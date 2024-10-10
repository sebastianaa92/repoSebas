#Librerias
import numpy as np
import pandas as pd


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

#2.1.1  Implement two substantially different ways to create these vectors in Python using.
# the Numpy package and test it for n = 100. Make sure that x/y are numpy arrays!Define n 
# constant in the code (don’t use a function to receive an input from the user through a textfield).
n = 100
x = np.ones(n)
# print(x)

start = 3
y = np.arange(start,3 * (n+1),3)
#print("Esto es y",y)


#2.1.2 Apply the function f (z) = 15·sin(z) to the entries of y, round the results to integers,and save
# the resulting vector as a new variable y2.
# Are all entries greater than 2? How many entries are equal to 5?
y2 = np.round(15 * np.sin(y))
#print("Esto es y2",y2)

#Print the indices of elements of y2 greater than 6
# indices = np.where(y2 > 6)

#Are all entries greater than 2?

#How many entries are equal to 5?
# contar_cincos = np.sum(y2==5)

# print("Coso",indices)
# print("Cosos",contar_cincos)


#2.2. Create a matrix M consisting of rows y and y2 . Create, in two different ways, a matrix M2 consisting of columns y T and y2T.
# In numpy, .T is just a shortcut for .transpose(), so that’s not too different solutions!.

M = np.array([y,y2])
# print(M)

M2 = np.array([y2.T, y2.T])
# print(M2)

#2.3. Extend matrices M and M2 by x as a new row/column respectively; name these as M3 and M4 , respectively.
# M3 = np.concatenate((M,[x]),axis=0 )
# print(M3)

# M4 = np.concatenate((M2,[x]),axis=0)
# print(M4)


#2.4.Determine the indices of all columns of M (the one defined in part 2) whose entries are 
#(each) greater than 5. Use these indices to print the filtered columns of M.
coso2 = M>5
coso3 = np.all(M > 5 , axis = 0)
print(coso3)
coso4 = np.where(np.all(M>6, axis=0))
print(coso4)
tales = M[:, coso4]
print(tales)

#3. Create three Pandas DataFrames, which respectively represent the following tables


valores1  = [["Alexander", 19, "male", "student"],["Jane",36,"female","physician"]]
valores2 = [["Eric", 22, "male", "lawyer"],["Laura",48,"female","teacher"]]
valores3 = [["Peter", 31, "male", "engineer"],["Julia",24,"female","consultant"]]
df1 = pd.DataFrame(valores1,columns=["Names","Age","Sex","Profesion"])
df2 = pd.DataFrame(valores2,columns=["Names","Age","Sex","Profesion"])
df3 = pd.DataFrame(valores3,columns=["Names","Age","Sex","Profesion"])
print(df1)
print(df2)
print(df3)

# valores = [["Alexander", 19, "male", "student"],["Jane",36,"Female","physician"]] + [["Eric", 22, "male", "lawyer"],["Laura",48,"Female","teacher"]]+[["Peter", 31, "male", "engineer"],["Julia",24,"Female","consultant"]]
# df = pd.DataFrame(valores, columns=["Name","Age","Sex","Profession"])
# print(df)

#3.2. Create a new Pandas DataFrame that is the union of the above three
union_df = pd.concat([df1,df2,df3],ignore_index = True)
print(union_df)

#3.3. Create a new Pandas DataFrame with data being as follows:

salarios = [600,4200,172,183,173,169]
size = [181,162,178,183,173,169]
names = union_df["Names"]
valores_unidos = pd.DataFrame({"Names": names,"Size" : size, "Salarios" : salarios})
print(valores_unidos)

join = pd.merge(union_df,valores_unidos, on = "Names")
print(join)