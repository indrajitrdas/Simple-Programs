# Subsequence of products less than K

def subseq_product(arr, k):
    n = len(arr)
    product = 1
    start = end = 0
    result = 0
    while(end < n):
        product = product * arr[end]
        while(start < end and product >= k):
            product = product/arr[start]
            start = start + 1
        if product < k:
            result = result + end-start +1
        end = end + 1
    return result
    

if __name__ == '__main__':
    print(subseq_product([1,2,3,4], 10))
    
    #print(subseq_product([1,9,2,8,6,4,3], 100))
            
        
    