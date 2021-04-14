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
	f = open(filename, 'r')
	rows = csv.reader(f)
	stock = {}
	for row in rows:
		if row:
			stock[row[0]] = float(row[1])
	return stock

# prices = read_prices('Data/prices.csv')
# print(prices)
# print(prices['IBM'])

def retire(stocks_list, stocks_price):
	stl = read_portfolio_list_of_dict(stocks_list)
	stp = read_prices(stocks_price)
	list_portfolio = []
	for stock in stl:
		current_portfolio = {
			'name' : stock['name'],
			'shares' : int(stock['shares']),
			'price' : float(stp.get(stock['name'])),
			'change' : round(float(stp.get(stock['name'])) - float(stock['price']), 2)
			}
		list_portfolio.append(current_portfolio)
	total = 0.0
	total_gain = 0.0
	for s in list_portfolio:
		total += s['shares']*s['price']
		total_gain += s['change']
	# return [total, total_gain]
	return list_portfolio

# portfolio = retire('Data/portfolio.csv', 'Data/prices.csv')
# print(f"Total: {portfolio[0]}  Total Gain/Loss: {portfolio[1]}")

#Section 2.3
def make_report(stocks_list, stocks_price):
	portfolio = retire(stocks_list, stocks_price)
	headers = ('Name', 'Shares', 'Price', 'Change')
	portfolio_tuple = [tuple(stock.values()) for stock in portfolio]
	print('      Name     Shares      Price      Change')
	print('---------- ---------- ---------- -----------')
	for name, shares, price, change in portfolio_tuple:
		price = "${:.2f}".format(price)
		print(f'{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}')

report = make_report('Data/portfolio.csv', 'Data/prices.csv')

#Section 2.5
