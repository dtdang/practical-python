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

def portfolio_cost(filename):
	total_cost = 0
	f = open(filename)
	rows= csv.reader(f)
	headers= next(rows)
	for row in rows:
		if not row[1]:
			print(row[0] + " No Shares")
			continue
		cost = int(row[1]) * float(row[2])
		total_cost += cost
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost: ', cost)