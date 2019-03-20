# Maximum size square sub matrix

#import numpy as np
def MaxSubSquare(arr):
    r = len(arr)
    c = len(arr[0])
    print(r)
    print(c)
    #mat = np.zeros((r+1, c+1))
    mat = [[0 for i in range(c)] for j in range(r)]
    print(mat)
    for i in range(0, r):
        for j in range(0, c):
            if arr[i][j] == 0:
                mat[i][j] = 0
            else:
                mat[i][j] = min(mat[i-1][j], mat[i-1][j-1], mat[i][j-1]) + 1
    print(mat)
    


arr = [[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]]

arr2 = [[0,0,1,1,1],
        [1,0,1,1,1],
        [0,1,1,1,1],
        [1,0,1,1,1]
        ]
  
MaxSubSquare(arr2)