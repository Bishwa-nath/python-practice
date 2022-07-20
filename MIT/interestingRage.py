<<<<<<< HEAD
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance*monthlyPaymentRate)
    balance = balance + (annualInterestRate/12.0 * balance)

print('Remaining balance:', round(balance, 2))
=======
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance*monthlyPaymentRate)
    balance = balance + (annualInterestRate/12.0 * balance)

print('Remaining balance:', round(balance, 2))
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
