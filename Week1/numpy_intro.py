import numpy as np

# convert python list to numpy array
mylist = [1, 2, 3]
x = np.array(mylist)

# or just pass in directly
y = np.array([4, 5, 6])

# list of lists to create a multidimensional array
matrix = np.array([[7, 8, 9], [10, 11, 12]])
# show matrix (rows, columns)
matrix.shape

# arange returns values within a given interval
# ex: start at 0 count up by 2, stop before 30
n = np.arange(0, 30, 2)

# reshape returns an array with the same data with a new shape
# ex: reshape array to be 3x5
n = n.reshape(3, 5)

# linspace returns evenly spaced numbers
# ex: return 9 evenly spaced values from 0 to 4
o = np.linspace(0, 4, 9)

# resize changes the shape and size of array in-place
o.resize(3, 3)

# ones returns a new array of given shape and type, filled with ones
np.ones((3, 2))

# zeros returns a new array of given shape and type, filled with zeros
np.zeros((2, 3))

# create an array using repeating list
# ex: returns [1 2 3 1 2 3 1 2 3]
np.array([1, 2, 3] * 3)

# ex: returns [1 1 1 2 2 2 3 3 3]
np.repeat([1, 2, 3], 3)

print(['a','b','c']+[1, 2, 3])
