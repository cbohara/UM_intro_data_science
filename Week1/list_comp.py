my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)

# list comprehension provides readability and performance benefits
my_list = [number for number in range(0,1000) if number % 2 == 0]

# convert function into list comprehension
def times_tables():
    times = []
    for i in range(10):
        for j in range (10):
            times.append(i*j)
    return times

print(times_tables() == [i * j for i in range(10) for j in range(10)])

# all user ids are 2 lower-case letters followed by 2 numbers
# write a list comprehension for all possible user id
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [one_char + two_char + one_num + two_num for one_char in lowercase
    for two_char in lowercase for one_num in digits for two_num in digits]
