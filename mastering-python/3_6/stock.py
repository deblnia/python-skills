
from decimal import Decimal

class Stock:
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
    def sell_shares(self, n:int):
        self.shares -= n

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    def __repr__(self):
        return f"Stock{self.name, self.shares, self.price}"
    def __eq__(self, other): 
        # tuple equality is a foot gun. but we persevere 
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))

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
