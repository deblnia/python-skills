
class Stock:
    __slots__ = ('name', '_shares', '_price') # this is a list of the only attributes that can be set
    # internal variables should have a leading underscore
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    @property # this makes it so that this is a property not a method that needs to be called
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError("Shares must be an integer")
        if value < 0:
            raise ValueError("Shares must be positive")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price must be positive")
        self._price = value
