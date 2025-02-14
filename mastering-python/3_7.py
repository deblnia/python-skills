
from abc import ABC, abstractmethod
import csv 

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    @abstractmethod
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

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print(f'<th>{h}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        print(f'<tr>{"".join(f"<td>{d}</td>" for d in rowdata)}</tr>')

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
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

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

if __name__ == "__main__":
    # A 
    portfolio = read_csv_as_instances('data/portfolio.csv', Stock)
    class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass
    print_table(portfolio, ['name','shares','price'], MyFormatter())

    # B 
    class NewFormatter(TableFormatter):
        def headers(self, headings):
            pass
        def row(self, rowdata):
            pass
    f = NewFormatter()

    # C 
    parser = DictCSVParser([str, int, float])
    port = parser.parse('data/portfolio.csv')
    port = read_csv_as_instances('Data/portfolio.csv', Stock)
