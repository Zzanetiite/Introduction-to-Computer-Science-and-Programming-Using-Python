# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:55:06 2022

@author: Zanete Dijeva
"""

"""
Task.
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change 
each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment 
that will pay off all debt in under 1 year.

Assume that the interest is compounded monthly according to t
he balance at the end of the month (after the payment for that 
month is made). The monthly payment must be a multiple of 
$10 and is the same for all months.
    
"""

def monthlyInterestRate(annualInterestRate):
    '''
    Parameters
    ----------
    annualInterestRate : Float
        Annual interest rate of a credit.

    Returns
    -------
    Monthly interest rate.

    '''
    return (annualInterestRate/12)
 
def monthlyUnpaidBalance(balance, monthlyPayment) :
    '''
    Parameters
    ----------
    balance : Float
        The outstanding balance on the credit card.
    monthlyPayment : Float
        Minimum monthly payment value.

    Returns
    -------
    Balance remaining once the monthly payment is made.

    '''
    return (balance - monthlyPayment)

def updatedBalanceEachMonth(monthlyUnpaidBalance, monthlyInterestRate):
    '''
    Parameters
    ----------
    monthlyUnpaidBalance : Float
        Balance remaining once the monthly payment is made.
    monthlyInterestRate : Float
        Monthly interest rate.

    Returns
    -------
    Remaining balance at the start of next month when next payment is due.

    '''
    return ((monthlyUnpaidBalance)+(monthlyInterestRate*monthlyUnpaidBalance))

def annualBalance(balance, annualInterestRate, MonPay):
    '''
    Parameters
    ----------
    balance : Float
        The outstanding balance on the credit card.
    annualInterestRate : Float
        Annual interest rate of a credit.
    monthlyPaymentRate : Float
        Minimum monthly payment rate as a decimal.
    monPay : Float
        Monthly payment.   

    Returns
    -------
    Annual Remainin Balance as flaot with 2 dec. places.

    '''
    # Monthly interest rate is constant for the next 12 months
    monIntRate = monthlyInterestRate(annualInterestRate)
    
    # Months left until annual balance statement
    months = 12
    
    while months > 0 :
        # Calculating non-consant variables
        montUnpBal = monthlyUnpaidBalance(balance, MonPay)
        updBalEMon = updatedBalanceEachMonth(montUnpBal, monIntRate)
        
        # Updating balance monthly and counting months until annual statement
        balance = updBalEMon  
        months -= 1
        
    return round(balance,2)

def ClearBalanceInAYear(balance, annualInterestRate, MonPay, months, dev):
    # Monthly interest rate is constant for the next 12 months
    monIntRate = monthlyInterestRate(annualInterestRate)
      
    # value by which MonPay will be incremented / reduced
    incr = 0.1
     
    # If output balance is within deviation
    if abs(annualBalance(balance, annualInterestRate, MonPay)) < (MonPay * dev) :
        print('Balance within dev ', annualBalance(balance, annualInterestRate, MonPay))
        # Check if negative and if so use the value (closest to pay off debt fully)
        if annualBalance(balance, annualInterestRate, MonPay) < 0 :
            print('Within negative dev ', MonPay)
            MonPay = round((MonPay),2)
            return MonPay
        # Else, add increment (next eligible value after previous) and output result
        else:
            MonPay = MonPay + incr
            MonPay = round((MonPay),2)
            print('Within positive dev ', MonPay) 
            return MonPay
    
    # If output balance is not within deviation add increment and loop until it is
    while abs(annualBalance(balance, annualInterestRate, MonPay)) > (MonPay * dev) :
        print('Balance outs dev ', annualBalance(balance, annualInterestRate, MonPay))
        if annualBalance(balance, annualInterestRate, MonPay) < 0 :
            print('Negative outs dev ', MonPay)
            addition = abs(annualBalance(balance, annualInterestRate, MonPay)) / 12
            MonPay = MonPay - addition
        else:
            addition = abs(annualBalance(balance, annualInterestRate, MonPay)) / 12
            MonPay = MonPay + addition
    print ("end of try")
    return ClearBalanceInAYear(balance, annualInterestRate, MonPay, months, dev)


balance = 999999
annualInterestRate = 0.18

# Months planning to pay the debt off in
months = 12

# deviation from final balance (25% from monthly payment - intuitive)
dev = 0.001

# Monthly interest rate is constant for the next 12 months
monIntRate = monthlyInterestRate(annualInterestRate)

# As a starting point of monthly payment - cumulative int. rate not considered
MonPayStart = round((balance / months) + (balance * monIntRate * (1 - dev)),-1)
print('Example starting MonPay: ', MonPayStart)    


 
print(ClearBalanceInAYear(balance, annualInterestRate, MonPayStart, months, dev))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    