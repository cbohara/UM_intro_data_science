import csv

with open('/Users/cbohara/Desktop/INTRO_DS/data/mpg.csv') as csvfile:
    # csv.Dictreader has read in each row of our csv file as a dictionary
    mpg = list(csv.DictReader(csvfile))

# all values in the dictionaries are strings, so we need to convert to float
# average city fuel economy across all cars
avg_cty = sum(float(car['cty']) for car in mpg) / len(mpg)

# quantify the relationship between cylinder size and city mpg
# use set to return the different number of cylinder types (no repeats)
cylinder_sizes = set(car['cyl'] for car in mpg)

#  group cars by number of cylinder, and finding the average cty mpg for each group
avg_cty_mpg_each_cylinder_size = []

# iterate through all cylinder types
for size in cylinder_sizes:
    mpg_sum = 0
    count = 0
    # iterate through all dictionaries
    for car in mpg:
        # if the cylinder size matches
        if car['cyl'] == size:
            # add the current cars mpg to sum
            mpg_sum += float(car['cty'])
            # increment count
            count += 1
    # append avg mpg calculation to the list
    avg_cty_mpg_each_cylinder_size.append((size, mpg_sum / count))

# sort the output list from smallest to largest number of cylinders
avg_cty_mpg_each_cylinder_size.sort(key=lambda x : x[0])

# quantify the relationship between vehicle type and highway mpg
# use set to return unique vehicle type values
vehicle_types = set(car['class'] for car in mpg)

# list for relationship between vehicle type and hwy mpg
avg_hwy_mpg_each_vehicle_type = []

for vehicle_type in vehicle_types:
    mpg_sum = 0
    count = 0
    for car in mpg:
        if car['class'] == vehicle_type:
            mpg_sum += float(car['hwy'])
            count += 1
    avg_hwy_mpg_each_vehicle_type.append((car, mpg_sum / count))

avg_hwy_mpg_each_vehicle_type.sort(key=lambda x: x[1])
