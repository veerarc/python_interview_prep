'''
Input: 
8
UDDDUDUU
Output:
1

Compiled successfully.All available test cases passed
'''
def countingValleys(n, s):
    l=[]
    count=0
    last = ''
    for val in s:
        if val=='U':
            if l==[] or l[len(l)-1]=='U':
                l.append(val)
            else:
                last = l.pop()
                
        if val=='D':
            if l==[] or l[len(l)-1]=='D':
                l.append(val)
            else:
                last = l.pop()
        if l==[] and last=='D':
            count+=1
    return count
