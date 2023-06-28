# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:46:27 2023

@author: King Vann

Pst = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month
n is number of mnths

"""
def computesPmt(PV, r,n):
    """
     Parameters
    ----------
    PV : TYPE
        DESCRIPTION. present value (amt borrow)
    r : TYPE
        DESCRIPTION. interest rate APR
    n : TYPE
        DESCRIPTION. number of months to pay back loan

    Returns
    -------
    Pmt : TYPE
        DESCRIPTION. how much you pay each month

    """
    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt

def computesPv(Pmt, r ,n):
    """
    

    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much i can afford for monthly payment
    r : TYPE float
        DESCRIPTION. interest rate APR
    n : TYPE integer
        DESCRIPTION. number of months

    Returns
    -------
    PV: TYPE. float
        Description. amunt of $$ i can afford to borrow
    
    formula:
    PV =(1-(1+r)**(-n)) *Pmt / r

    
    r = r/100
    r = r/12
    """
    
    Pv = (1-(1+r)**(-n)) * Pmt / r
    return Pv

# input the PV
import numpy as np

while(True):
    choice = int(input('enter choice 1 for PV, 2 for Pmt -> '))
    if(choice == 1 or choice == 2):
        break
    else:
        print(f"enter a 1 or 2, you entered {choice}")
    
    
if choice == 2:
    PV = input('enter PV: ')
    PV = float(PV)
    #equivalently PV = float(input('enter PV: '))
    print(f"PV = {PV} \n")
    
    r= input('interest APR: ')
    r = float(r)/100
    r = r/12
    print(f"interest = {r: 0.3f}")
    
    n = int(input('how many months: '))
    print(f"\nn = {n} months")
    
    pmt = computesPmt(PV, r,n)
    pmt = np.round(pmt, 2)
    print(f"payment is {pmt: } per month")

if choice == 1:
    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt = {Pmt} \n")
    
    r= input('interest APR: ')
    r = float(r)/100
    r = r/12
    print(f"interest = {r: 0.3f}")
    
    n = int(input('how many months: '))
    print(f"\nn = {n} months")
    
    Pv = computesPv(Pmt, r, n)
    print(Pv)