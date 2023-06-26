# Name: Arjun Patel 
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"-AP

# CS 115 - hw3

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]


def letterScore(letter,scoreList):
    '''This function returns the scrabble score that is associated with a lowercase letter'''
    L = scoreList[0]
    if letter=="":
        return 0
    else:
        L = scoreList[0]
        if letter == L[0]:
            return L[1]
        else:
            return letterScore(letter,scoreList[1:])
    

def wordScore(S,scoreList):
    '''This function returns the sum of each letter's scrabble score within a string'''
    if S=="":
        return 0
    else:
        return letterScore(S[0],scoreList) + wordScore(S[1:], scoreList)
    
