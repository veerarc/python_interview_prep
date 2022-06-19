'''
Making Anagrams from Hackerrank

Minimum number of deletions to make both string anagrams.

Input:
cde
abc
Output:
4

Compiled successfully.All available test cases passed

'''

def makeAnagram(a, b):
    match=0
    miss=0
    for i in a:
        if i in b:
            b=b.replace(i,'',1)
            match+=1
        else:
            miss+=1
    return miss+len(b)
