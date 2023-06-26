'''
Created on 3.24.23
@author:   Arjun Patel
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"
                                                                        -A.P

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False 
    else:
        return True
#******************************************************************************

#The base 2 representation of thr number 42 --> 101010
    
#If you are given an odd base-10 number, the rightmost bit will always be 1 in base-2 representation
#If you are given an even base-10 number, the rightmost bit will always be 0 in base-2 representation

#If given a base-2 number, by eliminating the rightmost bit, we get the original number divided by 2 (half the original #) 
#For odd number in base-2, eliminating the rightmost bit will still give you half of the original number rounded down to the nearest integer
    
#If we already had the base-2 representation of Y, we could easily find base-2 representation of N
    #If N is even, we would simply add 0 to the rightmost place and shit the existing representation to the left 
    #If N is odd, we simlply would add a 1 to the rightmost place and shift the existing representation to the left 
    
#******************************************************************************

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n//2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        right_most=int(s[-1])
        rest_of_left=s[:-1]
        return 2 * binaryToNum(rest_of_left)+ right_most

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    x = binaryToNum(s)
    y = x + 1
    z = numToBinary(y)
    if len(z) != 8:
        zeros = 8-len(z)
        return("0"*zeros)+z

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n>0:
        count(increment(s),n-1)
#*****************************************************************************

#The ternary representation for the value 59 is 2012. This is because
        # 59/3 = 19 remiander 2
        # 19/3 = 6 remainder 1
        # 6/3 = 2 remainder 0 
        # 2/3 = 0 remainder 2

#*****************************************************************************

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%3 == 0:
        return numToTernary(n//3) + "0"
    elif n%3 == 1:
        return numToTernary(n//3) + "1"
    else:
        return numToTernary(n//3) + "2"
    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif s[-1] == "0":
        return 3 * ternaryToNum(s[:-1])
    elif s[-1] == "1":
        return 3 * ternaryToNum(s[:-1]) + 1
    else:
        return 3 * ternaryToNum(s[:-1]) + 2
        
