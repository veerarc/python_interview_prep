'''
Count the a's in a infinitely repeating string

Input:
aba
10
Ouput:
7

Input:
a
1000000000000
Output:
1000000000000

Compiled successfully.All available test cases passed

'''

def repeatedString(s, n):
    length =len(s)
    count=s.count('a')
    total=int(n/length)*count
    substr_index = n%length
    rem = s[0:substr_index].count('a')
    return total+rem
