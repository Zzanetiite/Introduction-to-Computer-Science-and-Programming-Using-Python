# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:55:06 2022

@author: Zanete Dijeva
"""

"""
Task.
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the 
credit card company each month.

The following variables contain values as described below:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and 
remaining balance. At the end of 12 months, print out the remaining 
balance. Be sure to print out no more than two decimal digits
of accuracy.
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

def minimumMonthlyPayment(monthlyPaymentRate, balance):
    '''
    Parameters
    ----------
    monthlyPaymentRate : Float
        Minimum monthly payment rate as a decimal.
    balance : Float
        The outstanding balance on the credit card.

    Returns
    -------
    Minimum monthly payment value.

    '''
    return (monthlyPaymentRate * balance)
    
def monthlyUnpaidBalance(balance, minimumMonthlyPayment) :
    '''
    Parameters
    ----------
    balance : Float
        The outstanding balance on the credit card.
    minimumMonthlyPayment : Float
        Minimum monthly payment value.

    Returns
    -------
    Balance remaining once the monthly payment is made.

    '''
    return (balance - minimumMonthlyPayment)

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

def annualBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Parameters
    ----------
    balance : Float
        The outstanding balance on the credit card.
    annualInterestRate : Float
        Annual interest rate of a credit.
    monthlyPaymentRate : Float
        Minimum monthly payment rate as a decimal.

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
        minMonPay = minimumMonthlyPayment(monthlyPaymentRate, balance)
        montUnpBal = monthlyUnpaidBalance(balance, minMonPay)
        updBalEMon = updatedBalanceEachMonth(montUnpBal, monIntRate)
        
        # Updating balance monthly and counting months until annual statement
        balance = updBalEMon  
        months -= 1
        
    return round(balance,2)

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04   
    
print(annualBalance(balance, annualInterestRate, monthlyPaymentRate))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    