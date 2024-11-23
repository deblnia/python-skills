#opens this file, reads all lines, and calculates how much it cost to purchase
# all of the shares in the portfolio. To do this, compute the sum of the second
# column multiplied by the third column.

def portfolio_cost(file):
    total_cost = 0.0

    with open(file, 'r') as f: 
        for line in f:
            row = lin e.split()
            total_cost += (float(row[1]) + float(row[2]))
    return total_cost 

print(portfolio_cost('Data/portfolio.dat'))

# I like the suggestion in the exercise to run this interactively python3 -i file 

