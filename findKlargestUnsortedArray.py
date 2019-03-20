# Kth largest element in unsorted arrray

# QuickSelect Algorithm : Using Quicksort and recurring only the part of array that contains the specific element
    
def find_kth(arr, k):
    _find_kth(arr, 0, len(arr)-1, k)
    
    
def _find_kth(arr, left, right, k):
    if left == right:
        return arr
    else:
        pivot = partition(arr, left, right)
        #print(arr)
        #print(pivot)
        #print(arr[pivot])
        if pivot == k:
            print(str(arr[k]) + "******************")
            return
        elif pivot < k:
            _find_kth(arr, pivot + 1, right, k)
        else:
            _find_kth(arr, left, pivot - 1, k)
        
def partition(arr, left, right):
    pivot = arr[left]
    print("pivot = " + str(pivot) + " at position left = " + str(left))
    left = left + 1
    print(arr[left])
    flag = False
    while not flag:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while right >= left and arr[right] >= pivot:
            right = right - 1
        if left > right:
            flag = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    arr[left] = arr[right]
    arr[right] = pivot
    print(arr)
    return right


arr = [5,2,4,7,3,8,9]

print(find_kth(arr, 4))
print(arr)
            
        
    