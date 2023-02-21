#Arjun Patel
#CS115 Lab 1 -> map and reduce
#2.2.23
#"I pledge my honor that I have abided by the Stevens Honor System"-Arjun Patel

from cs115 import *
from functools import reduce
from math import factorial 


def inverse(n):
    """This function returns the reciprocal of the input n"""
    if n==0:
        print("The value 0 cannot be expressed as an inverse since it would be undefined. Please enter a different number.")
    else:
        return 1/(n)
    
def add(x,y):
    """This function takes the sum of two inputs x and y"""
    return x+y

def e(n):
    """This function returns the value of e in the Taylor expansion that corresponds to the input n by adding n terms in the expression"""
    if n == 0:
        return 1
    else:
        s = map(factorial, range(1,n+1))
        t = map(inverse,s)
        return 1+ reduce(add,t) 
        
    
   
    


    
