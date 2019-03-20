# Maximum Subarray Problem:
# Find the contiguous subarray of numbers which has the largest sum.
# Kadane's Algorithm - Dynamic - O(n)
def Max_Sub_Arr(arr):
    print(arr)
    max_cur_sum = max_global_sum = arr[0]
    for i in range(1, len(arr)):
        max_cur_sum = max(arr[i], max_cur_sum + arr[i])
        if max_global_sum < max_cur_sum:
            max_global_sum = max_cur_sum
    return max_global_sum

arr1 = [1,2,-3,4,5,-9]
print(Max_Sub_Arr(arr1))

arr2 = [-6,-1,0,1,3]
print(Max_Sub_Arr(arr2))

arr3 = [-3,-2,-9, 9]
print(Max_Sub_Arr(arr3))
        