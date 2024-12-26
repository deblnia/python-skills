# opens this file, reads all lines, and calculates how much it cost to purchase
# all of the shares in the portfolio. To do this, compute the sum of the second
# column multiplied by the third column.

def portfolio_cost(file):
    total_cost = 0.0

    with open(file, 'r') as f: 
        for line in f:
            row = line.split()
            try: 
                nshares = int(row[1])
                price = float(row[2])
                total_cost = total_cost + nshares * price 
            except ValueError as e: 
                print(f"Couldn't parse {repr(line)}")
                print(f"Error: {e}")
    return total_cost 

if __name__ == '__main__': 
    print(portfolio_cost('data/portfolio.dat'))


