import pandas as pd
import numpy as np

# convert list into panda series
animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))

numbers = [1, 2, 3]
print(pd.Series(numbers))

# panda does a type conversion of None to object
animals = ['Tiger', 'Bear', None]
print(pd.Series(animals))

# panda converts None to NaN (not a number) which is actually a floating number for efficiency
numbers = [1, 2, None]
print(pd.Series(numbers))

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}

panda_sports = pd.Series(sports)
print(panda_sports)

# query the value at index 3 using iloc attribute
panda_sports.iloc[3]

# query the series for the value for the key
panda_sports.loc['Golf']

# use vectors for speedy calculations
example = pd.Series([100.00, 120.00, 101.00, 3.00])
total = np.sum(example)

# best practice to utilize panda series vectors vs. loop transformations
speedy = pd.Series(np.random.randint(0,1000,10000))
speedy += 2

# how to append data to numpy series
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving = pd.Series(['Australia', 'Barbados', 'Pakistan', 'England'],
                            index = ['Cricket', 'Cricket', 'Cricket', 'Cricket'])

all_countries = original_sports.append(cricket_loving)
print("-----Original----")
print(original_sports)
print("----Cricket----")
print(cricket_loving)
print("----All----")
print(all_countries)
print("--Maintain Original--")
print(original_sports)
