'''
Common Child from Hacker Rank

A string A is said to be a child of another string B if they match exactly, or if any number of characters in B can be deleted to form A. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings.

Sample Input
HARRY
SALLY

Sample Output 
2

Explanation

The longest string that can be formed by deleting zero or more characters from and is AY, whose length is 2.

Compiled successfully.10/15 test cases passed

'''

def commonChild(s1, s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
