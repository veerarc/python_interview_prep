'''
Recursive Digit Sum by HackerRank

For example, the super digit of will be calculated as:
super_digit(9875) 9+8+7+5 = 29 
super_digit(29) 2 + 9 = 11
super_digit(11)1 + 1 = 2
super_digit(2)= 2

Compiled successfully.All available test cases passed


'''
def get_sum(s):
    # wrong approach
    # if s<10: 
    #     return s
    # # rem=0
    # # while s/10>0:
    # #     rem+=s%10
    # #     s=s//10
    # # rem+=s
    # return s%10+get_sum(s//10)
    
    if len(s)<=1:
        return s
    total=0
    for i in s:
        total+=int(i)
    return get_sum(str(total))

# Complete the superDigit function below.
def superDigit(n, k):
    # n should be a string as it can go up to infinite number
    n = get_sum(n)
    print(n)
    n = n*k
    print(n)
    return get_sum(n)
