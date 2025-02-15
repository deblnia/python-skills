
from abc import ABC, abstractmethod
import csv 


def print_portfolio(portfolio): 
    # tbh no clue how to do this 
    print(f'{"name":>10} {"shares":>10} {"price":>10}') # 10 character long, right aligned 
    print(f'{"-" * 10} ' * 3) # dashes 
    for s in portfolio:
        print(f'{s.name:>10} {s.shares:>10} {s.price:>10.2f}')

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()
    # could maybe add an attribute for the formats? 

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

# need to add upper headers and decimals 
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [f"{item:{fmt}}" for fmt, item in zip(self.formats, rowdata)]
        super.row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])



def create_formatter(name, col_formats=None, headers_upper=None):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')
    
    if col_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = col_formats

    if headers_upper:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

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

# could try something like this 
# def print_table(records, fields, formats, formatter):
#     formatter.headings(fields)
#     for r in records:
#         rowdata = [f"{getattr(r, fieldname):{fmt}}"
#                    for fieldname, fmt in zip(fields, formats)]
#         formatter.row(rowdata)


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
    

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
