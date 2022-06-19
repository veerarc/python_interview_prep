'''
Jumping on the clouds from Hackerrank.

Input:
7
0 0 1 0 0 1 0
Output:
  4

Input:
6
0 0 0 0 1 0
Output:
3

Compiled successfully.All available test cases passed
'''
def jumpingOnClouds(c):
    i=0
    count=0
    while i<len(c)-1:
        if i+2<len(c) and c[i+2]==0:
            i+=2
            count+=1
        elif c[i+1]==0:
            i+=1
            count+=1        
    return count
