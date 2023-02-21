'''
Author:Arjun Patel 
Pledge:"I Pledge my honor that I have abided by the Steven Honor System"- AP 
'''
#Problem 1

def addOne(L):
    """This function takes a list L and adds one to each element in the list"""
    if L==[]:
        return []
    else:
        return [L[0]+1]+addOne(L[1:])

#Problem 2

def explode(S):
    """This fucntion takes a string and returns a list of characters where each if a string of lenth 1"""
    if S =='':
        return []
    else:
        return list(S[0]) + list(explode(S[1:]))

#Problem 3

def even(x):
    """This function returns true or false for an input n by determining if it is even"""
    if x%2==0:
        return True
    else: return False

def odd(x):
    """This fucntion returns true or false for an input n by determining if it is odd"""
    if x%2==1:
        return True
    else: return False
    
def myFilter(func,L):
    """This function accepts a function and list and returns the list elements that correspond to the function"""
    if L==[]:
     return []
    elif func(L[0]) == True:
        return [L[0]] + myFilter(func, L[1:])
    else:
        return myFilter(func, L[1:])

#Problem 4
    
def sumPos(L):
    """This fucntion accepts a list of numbers and returns the sum of only positive elements within the list"""
    if L==[]:
        return 0
    elif L[0] > 0:
        return L[0]+sumPos(L[1:])
    else: return sumPos(L[1:])
