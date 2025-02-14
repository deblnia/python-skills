import reader 
import stock 
import tableformat

if __name__ == "__main__":
    # A 
    portfolio = reader.read_csv_as_instances('data/portfolio.csv', stock.Stock)
    class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass
    tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())

    # B 
    class NewFormatter(tableformat.TableFormatter):
        def headers(self, headings):
            pass
        def row(self, rowdata):
            pass
    f = NewFormatter()

    # C 
    parser = reader.DictCSVParser([str, int, float])
    port = parser.parse('data/portfolio.csv')
    port = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
