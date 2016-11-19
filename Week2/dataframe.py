# xDataFrame is a 2-dimensional labeled data structure
# similar to a spreadsheet or SQL table, or a dict of a series of objects
# avoid chaining with dataframe
import pandas as pd

purchase1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase2 = pd.Series({'Name': 'Kevin',
                       'Item Purchased': 'Kitty Litter',
                       'Cost': 2.50})
purchase3 = pd.Series({'Name': 'Amanda',
                       'Item Purchased': 'Bird Food',
                       'Cost': 40.50})
dataframe = pd.DataFrame([purchase1, purchase2, purchase3], index = ['Store1', 'Store2', 'Store3'])
print("Examples of accessing data in dataframes")
print(dataframe)
print("-------------------")
print(dataframe.loc['Store2', 'Cost'])
print("-------------------")
# swap row and column layout
print(dataframe.T)
print("-------------------")
print(dataframe.loc['Store1']['Cost'])
print("-------------------")
print(dataframe.loc[:,['Name', 'Cost']])
print("-------------------")
print("Use drop to delete a row in the dataframe")
# returns copy of dataframe with given rows removed
print(dataframe.drop('Store1'))
print("-------------------")
# does not affect original dataframe data
print(dataframe)
print("-------------------")
# best practice in pandas to copy dataframe and alter
# avoid in place changes to dataframe
copy_dataframe = dataframe.copy()
copy_dataframe = copy_dataframe.drop('Store1')
print(copy_dataframe)
print("-------------------")
print("Use del to delete column")
del copy_dataframe['Name']
print(copy_dataframe)
