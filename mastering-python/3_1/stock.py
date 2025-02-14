
import csv 
# copying over 1_5 stock class 
class Stock: 
    def __init__(self, name, shares, price): 
        self.name = name 
        self.shares = shares 
        self.price = float(price)
    
    def cost(self): 
        return self.shares * self.price 
    def sell_shares(self, n:int):
        self.shares -= n

# On 2, should a read portfolio function be part of the class? 
    # I would argue no, since it instantiates a bunch of class instances 

def read_portfolio(filepath): 
    stocks = [] 

    f_csv = csv.reader(open(filepath))
    headers = next(f_csv) # needed to skip headers
    rows = list(f_csv)

    for i, (name, shares, price) in enumerate(rows): 
        s = Stock(name, shares, price)
        stocks.append(s)

    return stocks 

def print_portfolio(portfolio): 
    # tbh no clue how to do this 
    print(f'{"name":>10} {"shares":>10} {"price":>10}') # 10 character long, right aligned 
    print(f'{"-" * 10} ' * 3) # dashes 
    for s in portfolio:
        print(f'{s.name:>10} {s.shares:>10} {s.price:>10.2f}')

