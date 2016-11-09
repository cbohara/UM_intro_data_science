# unpack a sequence into different variables using tuple
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x

print(fname)
print(lname)

# built in method for convenient string formatting
sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'
}

sales_statement = '{} bought {} item(s) at the price of ${} each for a total of ${}.'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))
