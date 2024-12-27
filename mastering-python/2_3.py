'''
Another good talk I like on Python iteration: https://nedbatchelder.com/text/iter/iter.html#1
This one is kind of also okay? https://www.youtube.com/watch?v=V2PkkMS2Ack
'''

import csv
import pprint
from collections import defaultdict

f = open('data/portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv) # needed to skip headers
rows = list(f_csv)

# iterating over a sequence of data 
for row in rows: 
    print(f"simple iteration: \n{row}")

# unpacking pre-iteration 
for name, shares, price in rows:
    print(f"tuple unpacking: \n {name}, {shares}, {price}")

# can use _ or __ as throw-away variables if we don't care 
for name, _, price in rows: 
    print(f"tuple unpacking with throwaway: \n {name}, {price}")

# you can use * to unpack an unknown number of values! 
byname = defaultdict(list)
for name, *data in rows: 
    byname[name].append(data)
print(f"wildcard unpacking: \b {byname['IBM']}")
for share, price in byname['IBM']:
    print(f"within wildcard unpacking: \n {shares}, {price}")

# can use enumerate to get index 
for i, v in enumerate(rows): 
    print(f"enumerate example: \n {i}, {v}")

# can still unpack with enumerate 
for i, (name, shares, price) in enumerate(rows): 
    print(f"enumerate with unpacking example: \n  {i}, {name}, {share}, {price} ")
    break 
    # this is also an important part of iteration IMO 
    # break will break out of the current loop 
    # continue will break out of the current iteration of the loop

# zip can be used to pair data 
print("pairing data with zip: \n")
for col, val in zip(headers, rows[0]): 
    print(col, val)
    break

# or make a dictionary 
print("making dictionary with zip: \n")
zd = dict(zip(headers, row))
print(zd.items())

# or sequence of dictionaries 
for row in rows: 
    record = dict(zip(headers, row))
    print(f"sequence of dictionaries: \n {record}")

# generators 
nums = [1,2,3,4,5]
squares = (x*x for x in nums)
squares 

for n in squares: 
    print(n)

print("Generators can only be used once.")
for n in squares:
    print(n)

# next and yield are important for generators 
squares = (x*x for x in nums)
print(next(squares)) # gives results one at a time 

def squares(nums): 
    for x in nums: 
        yield x*x # feeds nicely to the for 

for n in squares(nums):
    print(n)








