'''
2D-array maximum hourglass from Hackerrank

There are 16 hourglasses in 6X6 arr , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.For example, given the 2D array:

Input:
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
 
Explanation:
-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18

Hourglass max == 28:
0 4 3
  1
8 6 6

Input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Output:
19

Compiled successfully.All available test cases passed


'''
def count_hr(arr):
    return arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
    
def hourglassSum(arr):
    max_count=-100
    # print(arr)
    # print(arr[0:3][0:3])
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr[0])-2):
            count = count_hr([x[j:j+3] for x in arr[i:i+3]])
            max_count = max(max_count, count)
    return max_count
