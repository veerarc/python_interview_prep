'''
Abbreviation from HackerRank

You can perform the following operations on the string,a :
Capitalize zero or more of a's lowercase letters.
Delete all of the remaining lowercase letters in a .

Given two strings, and , determine if it's possible to make equal to as described. If so, print YES on a new line. Otherwise, print NO.

INput:
1
daBcd
ABC

Output:
YES

Compiled successfully.All available test cases passed

'''

def abbreviation(a, b):
    m=len(a)
    n=len(b)
    dp = [[0]*(n+1) for _ in range(m+1)] 
    for i in range(m+1): # with empty b. Give lower values to 1. upper values to 0.
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1].islower():
                if a[i-1].upper()==b[j-1]: # if if same take value one step before on both strings. 
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-1]
                else:# if not equal then delete => take value from without this char in a. that is [i-1][j].
                    dp[i][j]=dp[i-1][j]    
            else:
                if a[i-1]==b[j-1]: # if same, take value one step before on both strings
                    dp[i][j]=dp[i-1][j-1]
                else: # if not equal, not satisfied
                    dp[i][j]=0
                
            # if a[i-1].islower():
            #     if a[i-1].upper()==b[j-1]:
            #         dp[i][j]=dp[i-1][j] or dp[i-1][j-1]
            #     else:
            #         dp[i][j]=dp[i-1][j]
            # else:
            #     if a[i-1]==b[j-1]:
            #         dp[i][j]=dp[i-1][j-1]
            #     else:
            #         dp[i][j]=0
    if dp[m][n]:
        return 'YES'
    else:
        return 'NO'
              
