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
    break # this is also an important part of iteration IMO 
    # break will break out of the current loop 
    # continue will break out of the current iteration of the loop

# zip can be used to pair data 
for col, val in zip(headers, row[0]): 
    print(col, val)



