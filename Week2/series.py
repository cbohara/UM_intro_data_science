import pandas as pd
import numpy as np

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
