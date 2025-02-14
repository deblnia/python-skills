
# classes have three functions: 
    # getattr 
    # setattr 
    # delattr 
    # there's also the probe, hasattr 

# this is the more generic version of the print table function 
def print_table(objs:list[any], fields:list[str]): 
    # needed the boiler plate from the last function 
    print(''.join(f'{fieldname:>10}' for fieldname in fields))
    print(f'{"-" * 10} ' * len(fields)) # dashes 
    for obj in objs:
        print(''.join(f'{getattr(obj, field):>10}' for field in fields))


# a method is attribute that executes when you add ()
# can also use getattr etc. for that 
class Stock: 
    def __init__(self, name, shares, price): 
        self.name = name 
        self.shares = shares 
        self.price = float(price)
    
    def cost(self): 
        return self.shares * self.price 
    def sell_shares(self, n:int):
        self.shares -= n

if __name__ == 'main':
    demo_stock = Stock('GOOG', 10, 500)

    c = demo_stock.cost
    c.__self__ # shows original location of method 
    c.__func__ # shows the name of the function 
    c.__func__(c.__self__) # execute the function 

    # sell function 
    s = demo_stock.sell_shares 
    s.__func__(s.__self__, 5)
    print(s.shares)
