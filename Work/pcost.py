# pcost.py
#
# Exercise 1.27
# def portfolio_cost(filename):
# 	total_cost = 0
# 	with open(filename, 'rt') as f:
# 		headers = next(f).split(',')
# 		for line in f:
# 			row = line.split(',')
# 			if not row[1]:
# 				print(row[0] + " No Shares")
# 				continue
# 			cost = int(row[1]) * float(row[2])
# 			total_cost += cost
# 	return total_cost


# cost = portfolio_cost('Data/portfolio.csv')
# print('Total Cost', cost)

#1.33
import sys
import csv

# def portfolio_cost(filename):
# 	total_cost = 0
# 	f = open(filename)
# 	rows= csv.reader(f)
# 	headers= next(rows)
# 	for rowno, row in enumerate(rows, start=1):
# 		try:
# 			cost = int(row[1]) * float(row[2])
# 		except ValueError:
# 			print(f'Row {rowno}: Bad row: {row}')
# 		total_cost += cost
# 	return total_cost

# if len(sys.argv) == 2:
# 	filename = sys.argv[1]
# else:
# 	filename = 'Data/portfolio.csv'

# cost = portfolio_cost('Data/missing.csv')
# print('Total Cost: ', cost)


#Section 2.4- Zip Practice
def portfolio_cost(filename):
	f = open(filename)
	rows= csv.reader(f)
	headers= next(rows)
	total_cost = 0
	for rowno, row in enumerate(rows, start=1):
		record = dict(zip(headers, row))
		try:
			nshares = int(record['shares'])
			price = float(record['price'])
			total_cost += nshares * price
		except ValueError:
			print(f'Row {rowno}: Bad row: {row}')
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfoliodate.csv')
print(cost)

#invert dictionary key values
pricelist = list(zip(prices.values(),prices.keys()))
'''
can run data processing on dictionary data keys like min, max, sorted
warning: zip stops once shortest input sequence is exhausted
'''
