
from decimal import Decimal

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        # probably don't want to do type conversions here
        # bc then you're mixing constructing an instance of the class with data conversion
        self.name = name
        self.shares = shares
        self.price = price

    # adding a class method as an alternate constructor
    # https://www.reddit.com/r/AskComputerScience/comments/swe5kn/what_is_classmethod_in_python_and_why_we_need/
    # use from by convention 
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

class DStock(Stock):
        types = (str, int, Decimal)

def read_portfolio(filepath):
    import csv
    portfolio = []
    with open(filepath) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv) # needed to skip headers
        for row in f_csv:
            record = Stock.from_row(row)
            portfolio.append(record)
    return stocks

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
    row = ['ACME', '50', '91.1']

    stock = Stock.from_row(row)
    print(stock.name, type(stock.shares), type(stock.cost()))

    dstock = DStock.from_row(row)
    print(dstock.name, type(dstock.shares), type(dstock.cost()))

    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    print(portfolio)
