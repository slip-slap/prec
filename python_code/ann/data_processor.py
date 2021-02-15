import pandas as pd
import numpy as np

df = pd.read_csv("./train_data/train_data_composite_material1.csv",delimiter=',',header=None)
shape = df.shape
print(shape)
for i in range(0,shape[1]-2,1):
    column = df.iloc[:,i:i+1]
    column_max_value = column.max().values.tolist()
    for index in range(0,shape[0],1):
        df.iloc[index, i] = round(df.iloc[index,i]/column_max_value[0],3)

df.reindex(np.random.permutation(df.index))    
df.to_csv("normalize.csv",index=False,header=False)
