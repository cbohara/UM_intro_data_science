import pandas as pd

df = pd.read_csv('/Users/cbohara/Desktop/INTRO_DS/data/census.csv')
# print(df)

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

df = df[columns_to_keep]
df.set_index(['STNAME', 'CTYNAME'])
print(df)
