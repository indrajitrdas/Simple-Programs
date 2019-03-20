# Search element in sorted rotated array

def search(arr, lb , hb, key):
    if lb > hb:
        return -1
    mid = (lb + hb)//2
    if arr[mid] == key:
        return mid
    
    if arr[lb] <= arr[mid]: # Sorted between lb and mid
        if key >= arr[lb] and key <= arr[mid]:
            return search(arr, lb, mid-1, key)
        else:
            return search(arr, mid+1, hb, key)
    else:                    # Not Sorted between lb and mid
        if key >= arr[mid] and key <= arr[hb]:
            return search(arr, mid+1, hb, key)
        else:
            return search(arr, lb, mid-1, key)
        

def _search(arr, lb , hb, key):
    if lb > hb:
        return -1
    mid = (lb + hb)//2
    if arr[mid] == key:
        return mid
    
    if key >= arr[lb] and key <= arr[mid]:
        return _search(arr, lb, mid-1, key)
    else:
        return _search(arr, mid+1, hb, key)



arr = [4,5,6,7,8,9,1,2,3]
key = 7
index = _search(arr, 0, len(arr)-1, key)
if index == -1:
    print("Key doesnot exist")
else:
    print("Key found at index = "+ str(index))