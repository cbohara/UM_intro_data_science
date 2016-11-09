my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)

# list comprehension provides readability and performance benefits
my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)

# convert function into list comprehension
def times_tables():
    times = []
    for i in range(10):
        for j in range (10):
            times.append(i*j)
    return times

print(times_tables() == [i * j for i in range(10) for j in range(10)])
