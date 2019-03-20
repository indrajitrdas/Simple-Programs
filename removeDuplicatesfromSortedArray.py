# NOT COMPLETE
# Remove duplicates from sorted array
# Time O(n) space O(1)
# Method: use a counter for new array that will overlap the input array.
#         if the next element is not equal to the previous one, then copy value to new index 

def removeDuplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return n
    index = 0
    i = 0
    while i in range(n-1):            # increment index counter everytime values in array are not same
        if arr[i] != arr[i+1]:
            arr[index] = arr[i]
            index = index + 1
        i = i + 1
    arr[index] = arr[n-1] # last 2 elements : could be same or different: copy last element -no difference
    return index + 1

arr = [1,2,2,3,4,4,4,5,5]
result  = removeDuplicates(arr)
print(result)
print(arr[0:result])
        
        