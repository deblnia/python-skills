
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