# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

#1.8
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month = 0
while principal > 0:
	month += 1
	if month >= extra_payment_start_month and month <= extra_payment_end_month:
		principal = principal * (1+rate/12) - (payment + extra_payment)
		total_paid += payment + extra_payment
	else:
		principal = principal * (1+rate/12) - payment
		total_paid += payment
	if principal < 0: #correct overpayment in last month
		total_paid += principal
		principal += principal * -1
	print(f"{month} {round(total_paid,2)} {round(principal,2)}")

print('Total paid', round(total_paid, 2))
print('Total months', month)