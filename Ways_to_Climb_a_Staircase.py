'''
Ways to Climb a Staircase from HackerRank

ou have a number of staircases in your house and you like to climb each staircase 1, 2, or 3 steps at a time. 
How many ways there are to reach the top of the staircases?
Sample Input
3
1
3
7

Sample Output
1
4
44

Compiled successfully.All available test cases passed


'''
mem=[0]*37
mem[0]=1
mem[1]=1
mem[2]=2
mem[3]=4


# Complete the stepPerms function below.
def stepPerms(n):
    
    if mem[n]!=0:
        return mem[n]
    # first 3 stairs manual.
    if n==1:
        return 1 
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        mem[n] = stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    return mem[n]
