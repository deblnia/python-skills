
import sys 

class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

def create_formatter(name):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')
    return formatter_cls()

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

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


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    import csv
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records


if __name__ == '__main__':
    # QA 
    s = Stock('goog', 1,2)
    print(repr(s)) 
    # QB 
    p = read_csv_as_instances('data/portfolio.csv', Stock) 
    print(repr(p)) 
    # QC 
    a = Stock('GOOG', 100, 490.1)
    b = Stock('GOOG', 100, 490.1)
    print(a == b)
    # QD 
    formatter = create_formatter('text')
    with redirect_stdout(open('out.txt', 'w')) as file:
        print_table(p, ['name','shares','price'], formatter)
        file.close()