'''
Alternating Characters from Hackerrank:

You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.Your task is to find the minimum number of required deletions.For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.

Input Format
The first line contains an integer q, the number of input strings.The next q lines each contain a string s.
Constraints
q, the number of strings, will be between 1 and 10
The length of each string s is less than 10^5
Each string s will consist only of characters A and B. 
Output Format
For each string, print the minimum number of deletions required on a new line.
Sample Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Output
3
4
0
0
4

Compiled successfully.All available test cases passed

'''
def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count
