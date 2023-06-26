#Arjun Patel
#2.24.23
#"I pledge my honor that I have abided by the Stevens Honor System"- A.P
#CS115 with Professor Kevin Ryan


#The Knapsack Problem --> Lab 4 

def knapsack(capacity:int,items:list):
    '''This function returns the  max items you can fit into your knapsack
     given a weight capacity and a list of sub-lists that represent items
     to take from. The sublists have a first entry that represents the weight
     of an item and the second being its value'''
    if capacity==0:
        return 0
    elif items ==[]:
        return 0
    elif capacity<items[0][0]:
        return knapsack(capacity,items[1:])
    else:
        use = knapsack(capacity-items[0][0],items[1:])+items[0][1]
        lose = knapsack(capacity, items[1:])
        return max(use,lose)

#test case below

def testKnapsack():
    '''This function us used to test the knapsack function. If each statement
    holds true, this function should return nothing (no errors)'''
   
assert knapsack(6, [[1, 4], [5, 150], [4, 180]])==184
assert knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]])==100
assert knapsack(6, [])==0
assert knapsack(0, [[2, 100], [3, 112], [4, 125]])==0

