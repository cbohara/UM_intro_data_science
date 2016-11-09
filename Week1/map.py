# list of prices for same item in index for each list
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]

# compare item to item price between the two stores to find the best price
# python utilizes lazy evaluation for efficient memory management
cheapest = map(min, store1, store2)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + " " + person.split()[-1]

list(map(split_title_and_name, people))
