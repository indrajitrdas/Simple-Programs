# Pairs of element from two array with specified sum

def findPair(arr1, arr2, X):
    n1 = len(arr1)
    n2 = len(arr2)
    setArr1 = set(arr1)
    for i in range(n2):
        temp = X - arr2[i]
        if temp in setArr1:
            print(temp, "   ", arr2[i])
            
            
arr1 = [1, 0, -4, 7, 6, 4] 
arr2 = [0, 2, 4, -3, 2, 1]  
X = 8
findPair(arr1, arr2, X)