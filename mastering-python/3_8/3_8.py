
if __name__ == '__main__': 
    import reader
    import stock
    import tableformat

    portfolio = reader.read_csv_as_instances('../data/portfolio.csv', stock.Stock)

    tableformat.print_portfolio(portfolio)

    # experiment 
    # class PortfolioFormatter(tableformat.TextTableFormatter):
    #     def row(self, rowdata):
    #         formats = ['{}', '{:d}', '{:.2f}']
    #         rowdata = [fmt.format(d) for fmt, d in zip(formats, rowdata)]
    #         super().row(rowdata)
    
    # mixin!
    # better bc don't need to pick a formatter or write the formatting myself 
    class PortfolioFormatter(tableformat.ColumnFormatMixin, tableformat.TextTableFormatter):
        formats = ['%s', '%d', '%0.2f']

    formatter = PortfolioFormatter()
    tableformat.print_table(portfolio, ['name','shares','price'], formatter)
    
    # another mixin 
    class UpperHeadersMixin:
        def headings(self, headers):
            super().headings([h.upper() for h in headers])

    class PortfolioFormatter(UpperHeadersMixin, tableformat.TextTableFormatter):
        pass
    
    formatter = PortfolioFormatter()
    tableformat.print_table(portfolio, ['name','shares','price'], formatter)

    # demo'ing mixins 
    formatter = tableformat.create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
    tableformat.print_table(portfolio, ['name','shares','price'], formatter)
    formatter = tableformat.create_formatter('text', upper_headers=True)
    tableformat.print_table(portfolio, ['name','shares','price'], formatter)

    
