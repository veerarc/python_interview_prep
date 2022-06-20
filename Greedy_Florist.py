'''

Greedy Florist from HackerRank.

A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1. 
Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers.

Sample Input 
3 2
2 5 6

Sample Output 
15

Compiled successfully.All available test cases passed


'''
def getMinimumCost(k, c):
    itr=0
    total=0
    c.sort()
    while (len(c)>0):
        for i in range(k):
            if len(c)>0:
                total+=(itr+1)*c[len(c)-1]
                c.remove(c[len(c)-1])
            else:
                break
        itr+=1
    return total
