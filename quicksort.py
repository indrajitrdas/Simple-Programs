# QuickSort

def quicksort(arr):
    _quicksort(arr, 0, len(arr)-1)
    
def _quicksort(arr, start, end):
    if start >= end:
        return
    else:
        partition_index = partition(arr, start, end)
        _quicksort(arr, start, partition_index - 1) # LeftSide of partition
        _quicksort(arr, partition_index + 1, end)

def partition(arr, start, end):
    pivot_value = arr[end]
    i = j = start
    while i < end: # untill end - 1 since end is pivot
        if arr[i] <= pivot_value:
            arr[j], arr[i] = arr[i], arr[j]
            j = j + 1
        i = i + 1
    arr[j], arr[end] = arr[end], arr[j]
    return j
    


arr = [6,1,3,8,7,2,4,1,5,1,11,2,4,6,9]
quicksort(arr)
print(arr)

            
    
            
    
            
    
    
    
    
        
    