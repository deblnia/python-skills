import csv 
import reader
from sys import intern
from typing import AnyStr, List 
from collections import defaultdict

f = open('data/portfolio.csv')
rows = csv.reader(f)

headers = next(rows)
row = next(rows)
coltypes = [str, int, float]


r = list(zip(coltypes, row))
# doing conversion 
record = [func(val) for func, val in zip(coltypes, row)]
# doing conversion dictionary
dict(zip(headers, record))
{name : func(val) for name, func, val in zip(headers, coltypes, row)} # or a dict comprehension

## PARSING UTILITY FUNCTION 
def read_csv_as_dicts(filename:AnyStr, coltypes:List[str])->dict: 
    '''
    Input: 
        - filename: a CSV filetype with one row of headers 
        - coltypes: a list of 
    Return: 
        - a dictionary typecast according to coltypes 
    '''
    result = [] 
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows) # skipping headers
    for row in rows: 
            record = { name : func(value) for name, func, value in zip(headers, coltypes, row)}
            result.append(record)
    return result

portfolio = read_csv_as_dicts('Data/portfolio.csv', [str,int,float])
for s in portfolio:
    print(s)

# 181 different routes, but 54K different strings? 
bus = read_csv_as_dicts('data/ctabus.csv', [str,str,str,int])
len({ id(row['route']) for row in bus }) # id get the unique ones
len({ row['route'] for row in bus }) 

# use sys.intern to cache strings 
rows = reader.read_csv_as_dicts('Data/ctabus.csv', [intern, intern, str, int])

