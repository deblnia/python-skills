# python is optimized for list.append()
import sys
import csv
import collections


items = []
print(sys.getsizeof(items))
items.append(1)
print(sys.getsizeof(items))
items.append(2)
print(sys.getsizeof(items))    # Notice how the size does not increase
items.append(3)
print(sys.getsizeof(items))    # It still doesn't increase here
items.append(4)
print(sys.getsizeof(items))    # Not yet.
items.append(5)
print(sys.getsizeof(items))    # Notice the size has jumped

# dicts and classes allow 5 values to be stored before reserved memory doubles
row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
print(sys.getsizeof(row))
row['a'] = 1 
print(sys.getsizeof(row))
row['b'] = 2
print(sys.getsizeof(row))
del row['b'] 
print(sys.getsizeof(row))

# maybe better to use tuples, named tuples, or classes with __slots__
# eg. this saves a lot of memory 
def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
# malloc'd memory (87215653, 87245590)
# estimate --> 
# nrows = 577563     # Number of rows in original file
# nrows * 240
# nrows * 4 * 8
# = 18482016

# ok but this is hard to work with 
# we can fake it 
class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []
    # will tell you to implement these two 
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
                    return [
                        {'route': self.routes[i],
                        'date': self.dates[i],
                        'daytype': self.daytypes[i],
                        'rides': self.numrides[i]}
                        for i in range(index.start or 0, index.stop, index.step or 1)
                    ]
        else:
            # If it's a single index, return a single dictionary
            return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]
            }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()      # <--- THIS CHANGED
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
    return records