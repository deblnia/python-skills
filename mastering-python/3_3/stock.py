
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


if __name__ == '__main__':
    import tableformat
    import reader 

    row = ['ACME', '50', '91.1']

    stock = Stock.from_row(row)
    print(stock.name, type(stock.shares), type(stock.cost()))

    dstock = DStock.from_row(row)
    print(dstock.name, type(dstock.shares), type(dstock.cost()))

    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', Stock)
    tableformat.print_table(portfolio, ['name', 'shares', 'price'])
