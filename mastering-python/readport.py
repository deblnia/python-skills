import csv
import read_rides # can use this to read in the portfolio in other ways 
from pprint import pprint
from collections import Counter, defaultdict

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')

# filtering 
[s for s in portfolio if s['shares'] > 100]

# total cost 
sum([s['shares']*s['price'] for s in portfolio])

# all unique stock names 
{ s['name'] for s in portfolio }

# total shares of each stock 
totals = { s['name']: 0 for s in portfolio }
for s in portfolio:
    totals[s['name']] += s['shares']

# could also get this using a Counter 
totals = Counter()
print(totals.most_common(2))

# you can also add counters together 
more = Counter()
more['IBM'] = 75
more['AA'] = 200
more['ACME'] = 30
print(totals + more)

# use defaultdicts to group data 
byname = defaultdict(list)
for s in portfolio:
    byname[s['name']].append(s)

byname['IBM']


### ASSIGNMENT ###  


bus_dicts = read_rides.read_rides_as_dicts('data/ctabus.csv')

'''
How many bus routes exist in Chicago?
'''

len({s['route'] for s in bus_dicts}) # 81 


'''
How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
'''

sum([bus['rides'] for bus in bus_dicts if bus['date'] == '02/02/2011' and bus['route'] == '22']) # 5055 

'''
What is the total number of rides taken on each bus route?
'''



'''
What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
'''
