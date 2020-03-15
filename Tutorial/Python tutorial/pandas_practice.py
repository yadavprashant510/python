import numpy as np
import pandas as pd
pd.__version__


data = pd.Series([0.25,0.5,0.75,1.0])
data



data.values

data.index

data = pd.Series([0.25, 0.5, 0.75, 1.0],
index=['a', 'b', 'c', 'd'])
data

population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
'Florida': 170312, 'Illinois': 149995}

states = pd.DataFrame({'population': population_dict,'area': area_dict})
states2 = pd.DataFrame(population_dict,columns=['population'])

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
'data2': range(3)})

df1

df2

pd.merge(df2,df1)

dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

dummy_data2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2'])
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])

df1

df2

df_row = pd.concat([df1, df2])

df_row

df_row_reindex = pd.concat([df1, df2], ignore_index=True)

df_row_reindex

frames = [df1,df2]
df_keys = pd.concat(frames, keys=['x', 'y'])


df_keys

df_keys.loc['x']

df_keys.loc['y']

df_col = pd.concat([df1, df2],axis = 1)

df_col

df_row = pd.merge(df1, df2,on='id')

df_row

# +
dummy_data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
df3 = pd.DataFrame(dummy_data3, columns = ['id', 'Feature3'])


# -

df3

df_row = pd.merge(df_row, df3,on='id')

df_row

df_merge_difkey = pd.merge(df_row, df3, left_on='id', right_on='id')


df_merge_difkey

df1

df2

df_outer = pd.merge(df1, df2, on='id',how= 'outer')


df_outer

df_suffix = pd.merge(df1, df2, left_on='id',right_on='id',how='outer',suffixes=('_left','_right'))
df_suffix


df_right = pd.merge(df1, df2, on='id',how= 'right')
df_right

df_left = pd.merge(df1, df2, on='id',how= 'left')
df_left

df_index = pd.merge(df1, df2, right_index=True, left_index=True)
df_index

df1 = pd.read_excel("F:\Python\SKU.xlsx",index='False')

df1


