'''
Largest Rectangle from HackerRank

A real estate company is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by h[i] where i represents the building number. If you join k adjacent buildings, they will form a solid rectangle of area k*[the minimum height of the adjacent buildings]

For example, the heights array h = [3,2,3]. A rectangle of height h = 2 and length k = 3 can be constructed within the boundaries. The area formed is h*k = 2*3 = 6.

Sample Input
5
1 2 3 4 5

Sample Output
9

Compiled successfully.All available test cases passed


'''

def largestRectangle(h):
    # i=0
    # j=len(h)-1
    # max_val = 0
    # print(h)
    # while i<j:
    #     max_val = max(max_val, min(h[i:j+1])*(j-i+1))
    #     print(i,j,min(h[i:j+1]),(j-i+1), max_val)
    #     if h[i]<=h[j]:
    #         i = i+1
    #     else:
    #         j = j-1
    # return max_val
    heights=h
    stk = [-1]
    heights.append(0)
    ans = 0
    for i in range(len(heights)):
        print('i:', i)
        while heights[i] < heights[stk[-1]]:
            print("stk: ", stk)
            print ("heights[i] and heights[stk[-1]], stk[-1]: ",heights[i], heights[stk[-1]], heights[i] < heights[stk[-1]], stk[-1])
            
            
            h = heights[stk.pop()]
            print("h = heights[stk.pop()] : ", h)
            w = i - stk[-1] - 1
            print("w = i - stk[-1]", w, i,  stk[-1])
            
            print("ans, h, w, h * w, max(ans, h * w): ", ans, h, w, h * w, max(ans, h * w))
            ans = max(ans, h * w)
        stk.append(i)
    return ans
