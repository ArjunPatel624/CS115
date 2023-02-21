#Arjun Patel

#"I pledge my honor that I have abided by the Stevens Honor System"-Arjun Patel 

# Problem Number 1

#factorial fucntion

" To use the function reduce we must import the functools library" 
from functools import reduce

"Here, we are defining the mult fucntion which will be used for the factorial fucntion"
def mult (x,y): 
    '''This function will take two inputs, x and y, and multiply them by each other'''
    return x*y

"Given that n is a positive integer, this fucntion will take range from 1 to n+1 and take the product of the sequence of numbers.Then, reduce will multiply two items at a time from the list to give us the result"
def factorial (n):
    '''This function takes a positive integer n and retunrs the factorial'''
    return reduce(mult,range(1, n+1))
    
# Problem Number 2

#Mean function

"Here we define the sum of two items x and y which we will use in our mean function"
def add (x,y):
    '''This function takes two inputs, x and y, and sums them up'''
    return x+y

"This function will add up items in a list L by two items at a time and then take that sum and divide it by the total number of items in the list"
def mean(L):
    ''' This function returns the mean of items within a list L'''
    return reduce(add,L)/len(L)
    
