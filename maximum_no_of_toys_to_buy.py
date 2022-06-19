'''
Maximum Number of Toys to Buy from HackerRank

Given a list of prices and an amount to spend, what is the maximum number of toys the parent can buy?

Input:
7 50
1 12 5 111 200 1000 10

Output:
4

Compiled successfully.All available test cases passed


'''
def maximumToys(prices, k):
    prices.sort()
    count=0
    for val in prices:
        k= k-val
        if k<0:
            break
        count+=1
    return count
