import csv
from collections import namedtuple
import tracemalloc

# what's the source of the overhead when reading in as strings? 


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dictionaries 
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        d = {}
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

# A class 
# class Row: 
#     # slight memory optimization 
#     __slots__ = ('route', 'date', 'daytype', 'rides')
#     def __init__(self, route, date, daytype, rides):
#         self.route = route
#         self.date = date 
#         self.daytype = daytype 
#         self.rides = rides 

# A named tuple - interchangable with a class? 
Row = namedtuple('Row', ('route', 'date', 'daytype', 'rides'))


def read_rides_as_class_instances(filename):
    '''
    Read the bus ride data as a list of instances of the Row class 
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        d = {}
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records 

if __name__ == '__main__':
    tracemalloc.start()
    rows = read_rides_as_tuples('data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # class instances 
        # Memory Use: Current 133214374, Peak 133244960
    # class instances with slots 
        # Memory Use: Current 110108918, Peak 110139504
    # named tuple 
        # Memory Use: Current 119350046, Peak 119380632
    # dicts 
        # Memory Use: Current 179415342, Peak 179445928
    # tuples 
        # Memory Use: Current 114728414, Peak 114759000