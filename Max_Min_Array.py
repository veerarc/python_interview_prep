'''
Max Min Array from Hacker Rank

You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of such that its unfairness is minimized. 
Call that array subarr. Unfairness of an array is calculated as
max(subarr) - min(subarr)

Sample Input 
7
3
10
100
300
200
1000
20
30

Sample Output 
20

max(10,20,30) - min(10,20,30) = 30 - 10 = 20

Compiled successfully.16/17 test cases passed

'''
def maxMin(k, arr):
    min_val=-1   
    arr.sort()
    for i in  range(0, len(arr)-k):
        if min_val==-1:
            min_val = arr[i+k-1]-arr[i]
        min_val=min(min_val, arr[i+k-1]-arr[i])
    return min_val
