'''
Encode Secret Message from HackerRank

Given the words in the magazine and the words in the note, print Yes if you can replicate your note exactly using whole words from the magazine; otherwise, print No.
For example, the note is "Coding is fun". The magazine contains only "coding is fun". The magazine has all the right words, but there's a case mismatch. The answer is .

Input:
6 4
give me one hamburger today night
give one hamburger today

Output:
Yes

Input:
6 5
two times three is not four
two times two is four

OUtput:
No

Compiled successfully.All available test cases passed


'''
def checkMagazine(magazine, note):
    d={}
    for i in magazine:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # print(d)
    for i in note:
        if i in d and d[i]>0:
            d[i]-=1
        else:
            print("No")
            return 
    print('Yes')
    # result="Yes"
    return 
  
