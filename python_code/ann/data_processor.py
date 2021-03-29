import pandas as pd
import numpy as np

TRAIN_DATA_PATH = './train_data/'
TRAIN_DATA_NAME = 'm1_normalization_reindex.csv'


df = pd.read_csv(TRAIN_DATA_PATH+TRAIN_DATA_NAME, delimiter=',')
shape=df.shape
print(df.head(10))
#df.drop(df[df["tsai_wu"] > 5].index, inplace = True)
#df.drop(df[df["ms"] > 5].index, inplace = True)

#max_value = [80, 80, 80, 90,   86, 196, 1.27, 181.0, 10.3, 0.28, 7.17, 2062.0, 1701.0, 70, 246, 105]
#max_value =  [90, 90, 90, 100, 100, 200, 1.5,  200,   15,    0.4, 8,    2100  , 1800  , 80, 260, 110]

def column_normalize(df):
    for i in range(0,shape[1]-2,1):
        column = df.iloc[:,i:i+1]
        column_max_value = column.max().values.tolist()
        print(column_max_value)
        print(max_value[i])
        #max_value.append(column_max_value[0])
        for index in range(0,shape[0],1):
            df.iloc[index, i] = round(df.iloc[index,i]/max_value[i],3)

#column_normalize(df)
#df.reindex(np.random.permutation(df.index))    
df = df.sample(frac=1)
df.to_csv(TRAIN_DATA_PATH + "m1_normalization_reindex.csv",index=False,header=True)
