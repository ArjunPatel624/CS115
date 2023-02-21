# Name: Arjun Patel 
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"-Arjun Patel
# 2.17.23

def change(amount,coins):
    '''returns a non-negative integer, which represents the miminum number of
    coins needed to make up the given amount'''
    if amount==0:
        return 0
    elif coins==[]:
        return float("inf")
    elif coins[0]>amount:
        return change(amount,coins [1:])
    else:
        use = 1+ change (amount-coins [0],coins)
        lose = 0 + change(amount,coins[1:]) 
        return min(use,lose)
