
import csv
from stock import Stock
from collections import defaultdict

def read_portfolio(filepath):
    import csv
    portfolio = []
    with open(filepath) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv) # needed to skip headers
        for row in f_csv:
            record = Stock.from_row(row)
            portfolio.append(record)
    return portfolio

# more generic
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

if __name__ == '__main__':
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    print(portfolio)