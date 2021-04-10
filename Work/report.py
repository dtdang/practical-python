# report.py
#
# Exercise 2.4
import csv 
from pprint import pprint

def read_portfolio_list(filename):
	portfolio = []
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		print(headers)
		for row in rows:
			holding = (row[0], int(row[1]), float(row[2]))
			portfolio.append(holding)
	return portfolio


def read_portfolio_list_of_dict(filename):
	portfolio = []
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			stock = {
				headers[0] : row[0],
				headers[1] : int(row[1]),
				headers[2] : float(row[2])
			}
			portfolio.append(stock)
			
	return portfolio

# report = read_portfolio_dict('Data/portfolio.csv')
# pprint(report)

def read_prices(filename):
	f = open('Data/prices.csv', 'r')
	rows = csv.reader(f)
	for row in rows:
		print(row)
