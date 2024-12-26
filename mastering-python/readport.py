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
for s in portfolio:
    totals[s['name']] += s['shares']
print(f"EXAMPLE: two most common - {totals.most_common(2)}")

# you can also add counters together 
more = Counter()
more['IBM'] = 75
more['AA'] = 200
more['ACME'] = 30
print(f"EXAMPLE: adding counters - {totals + more}")

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
# this works but it wasn't sorted so it's too much and too hard to read 
# totals = {bus['route'] : 0 for bus in bus_dicts}
# for i in bus_dicts: 
#     totals[i['route']] += i['rides']
# print(f"BUS TOTAL RIDES - {totals}")

totals = Counter()
for s in bus_dicts:
    totals[s['route']] += s['rides']
print(f"Top 2 routes by rides - {totals.most_common(2)}")

'''
What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
'''
rides_by_route_and_year = defaultdict(lambda: {'2001': 0, '2011': 0}) # {'route' : {'2001' : 0, '2011' : 0}}

for entry in bus_dicts:
    year = entry['date'].split('/')[2]
    if year in ['2001', '2011']:  
        rides_by_route_and_year[entry['route']][year] += entry['rides']

increase = [
    (route, data['2011'] - data['2001']) 
    for route, data in rides_by_route_and_year.items()
]

top_5_routes = sorted(increase, key=lambda x: x[1], reverse=True)[:5]
print(f"Top 5 routes by 10yr increase - {top_5_routes}")



# I like this taxonomy of using data structures: 
    # For problems where you need to determine uniqueness, use a set. Sets aren't allowed to have duplicates.
    # If you need to tabulate data, consider using a dictionary that maps keys to a numeric count.
    # If you need to keep data in order or sort data, store it in a list.