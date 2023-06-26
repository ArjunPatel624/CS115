'''
Created on  4/20/23
@author(s): Arjun Patel and Javain Batista 
Pledge:     "I pledge my honor that I have abided by the Stevens Honor System"
            -A.P & J.B
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
# You may write helpers if you see fit. Remember: do not
# import anything, and do not use loops.
#*********************************************************************

#The following 3 funcions are helper functions that will help in writing compress and uncompress

def isOdd(n):
    '''Returns weather or not the integer argument is odd'''
    return n % 2 == 1


def binaryToNum(s):
    """Given that s is a string argument in binary format(0s and 1s),
        this function returns the number associated with the binary representation
        s"""
    if s == "":
        return 0
    elif s[-1] == "1":
        return 2 * binaryToNum(s[:-1]) + 1
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])


def numToBinary(n, size=COMPRESSED_BLOCK_SIZE):
    """Given that n a non-negative interger, this function returns the binary representation of n"""
    if n == 0:
        return "0" * size
    elif isOdd(n) == True:
        return numToBinary(int(n // 2), size - 1) + "1"
    else:
        return numToBinary(n//2, size-1) + "0"

#main functions
    
def compress(S):
    '''compresses a 64-bit binary image (represented as 1's
    and 0's) using a run-length encoding'''
    def compAlt( S, length, current):
        if S == "":
            if length != 0:
                binary = numToBinary(length)
                return binary
            else:
                return ""
        if length == MAX_RUN_LENGTH or current != S[0]:
            binary = numToBinary(length)
            if current == "1":
                current = "0"
            else:
                current = "1"
            return binary + compAlt(S, 0, current)
        return compAlt(S[1:], length + 1, current)
    return compAlt(S, 0, "0")

def uncompress(C):
    '''uncompresses a run-length encoding to its original
    64-bit binary image'''
    def uncompAlt(C, current):
        if C == "":
            return ""
        num = (binaryToNum(C[0:COMPRESSED_BLOCK_SIZE]))
        if current == "0":
            return (current * num) + uncompAlt(C[COMPRESSED_BLOCK_SIZE:], "1")
        else:
            return (current * num) + uncompAlt(C[COMPRESSED_BLOCK_SIZE:], "0")
    return uncompAlt(C, "0")
        
