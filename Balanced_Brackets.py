'''
Balanced Brackets from Hacker Rank


'''
def isBalanced(s):
    stack=[]
    for i in s:
        if len(stack)==0 or i in ['{','[','(']:
            stack.append(i)
        elif len(stack)==0 and i in ['}',']',')']:
            return 'NO'
        elif i==')':
            if stack[len(stack)-1]=='(':
                stack.pop()
            else:
                return 'NO'
        elif i=='}':
            if stack[len(stack)-1]=='{':
                stack.pop()
            else:
                return 'NO'
        elif i==']':
            if stack[len(stack)-1]=='[':
                stack.pop()
            else:
                return 'NO'
        else:
            return 'NO'
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'
