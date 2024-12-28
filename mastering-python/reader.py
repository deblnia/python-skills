import csv 

f = open('data/portfolio.csv')
rows = csv.reader(f)

headers = next(rows)
row = next(rows)
coltypes = [str, int, float]


