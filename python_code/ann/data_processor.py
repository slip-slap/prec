import pandas as pd
import numpy as np

df = pd.read_csv("./train_data/clt_data.csv",delimiter=',')
shape = df.shape
print(df.head(5))
df.drop(df[df["tsai_wu"] > 5].index, inplace = True)

def column_normalize(df):
    for i in range(15,shape[1],1):
        column = df.iloc[:,i:i+1]
        column_max_value = column.max().values.tolist()
        print(column_max_value)
        for index in range(0,shape[0],1):
            df.iloc[index, i] = round(df.iloc[index,i]/column_max_value[0],3)





#df.reindex(np.random.permutation(df.index))    
df.to_csv("normalize_remove_row_test.csv",index=False,header=False)
