import pandas as pd

dataframe = pd.read_csv('/Users/cbohara/Desktop/INTRO_DS/data/olympics.csv', index_col=0, skiprows=1)
dataframe.head()

for col in dataframe.columns:
    if col[:2] == '01':
        dataframe.rename(columns={col:'Gold'+col[4:]}, inplace = True)
    if col[:2] == '02':
        dataframe.rename(columns={col:'Silver'+col[4:]}, inplace = True)
    if col[:2] == '03':
        dataframe.rename(columns={col:'Bronze'+col[4:]}, inplace = True)

print(dataframe)
