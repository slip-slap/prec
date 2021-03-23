import pandas as pd
import numpy as np

#df = pd.read_csv("../data/stock_history_data/000001.csv")
#print(df.head())

A = [[1,1,1,0,0],
     [3,3,3,0,0],
     [4,4,4,0,0],
     [5,5,5,0,0],
     [0,2,0,4,4],
     [0,0,0,5,5],
     [0,1,0,2,2]
     ]

"""
normal_matrix = np.matmul(np.array(A),np.array(A).transpose())

eigenvalue, eigvector = np.linalg.eig(normal_matrix)

print(eigenvalue)
#print(eigvector)

"""
A = [[1,1,1,0,0],
     [3,3,3,0,0],
     [4,4,4,0,0],
     [5,5,5,0,0],
     [0,2,0,4,4],
     [0,0,0,5,5],
     [0,1,0,2,2]
     ]

normal_matrix = np.matmul(np.array(A).transpose(),np.array(A))

eigenvalue, eigvector = np.linalg.eig(normal_matrix)

print(eigenvalue)
#print(eigvector)
