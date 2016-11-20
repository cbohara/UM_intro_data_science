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

# boolean mask returns true or false whether the country has won at least one gold medal
dataframe['Gold'] > 0

# use where function to apply boolean mask to the series and return series of the same shape
only_gold = dataframe.where(dataframe['Gold'] > 0)
# replaces data of countries that have not won a gold to NaN
only_gold.head()
print(only_gold)
print(only_gold['Gold'].count())

# better way for querying that eliminates countries that have not won a gold rather than replace with NaN
only_gold = dataframe[dataframe['Gold']>0]
only_gold.head()
print(only_gold)
