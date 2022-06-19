'''
input: 
9
10 20 20 10 10 30 50 10 20
Output:
3
'''

def numberPairs(n, ar):
    hash_dict={}
    count=0
    for val in ar:
        if val in hash_dict:
            hash_dict.pop(val)
            count+=1
        else:
            hash_dict[val]=1
    return count
  
