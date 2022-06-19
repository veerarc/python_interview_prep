'''
Character Frequencies from HackerRank

A string is considered to be valid if all characters of the string appear the same number of times. It is also valid if you can remove just 1 character anywhere in the string, and the remaining characters will occur the same number of times.

Sample Input 0
aabbcd

Sample Output 0
NO

Sample Input 1
aabbccddeefghi

Sample Output 1
NO

Compiled successfully.All available test cases passed


'''

def isValid(s):
    dict_l = {}
    for i in s:
        if i in  dict_l:
            dict_l[i]+=1
        else:
            dict_l[i]=1
    
    if len(set(dict_l.values()))==1:
        return 'YES'
    else:
        counts = list(dict_l.values())
        m_c = max(counts)
        m_i = counts.index(m_c)
        counts[m_i]-=1
        if len(set(counts))==1:
            return 'YES'
    
    counts = list(dict_l.values())
    if 1 in counts:
        counts.remove(1)
        if len(set(counts))==1:
            return 'YES'
    return 'NO'
