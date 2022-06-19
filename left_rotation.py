'''
Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Input:
5 4
1 2 3 4 5

Output:
5 1 2 3 4

Compiled successfully.All available test cases passed


'''
def rotLeft(a, d):
    return a[d:]+a[:d]
