# Longest Common Sub Sequence :
# sequence that appears in the same relative order,
# but not necessarily contiguous(not substring) in both the string

def lcs_recursion(str1, str2): # Recursive approach O(2^n)
    #print(str1)
    #print(str2)
    if len(str1) == 0 or len(str2) == 0:
        lcs_len = 0
    elif str1[-1] == str2[-1]:
        lcs_len = 1 + lcs_recursion(str1[:-1], str2[:-1])
    elif  str1[len(str1)-1] != str2[len(str2)-1]:
        temp1 = lcs_recursion(str1[:-1], str2)
        temp2 = lcs_recursion(str1, str2[:-1])
        lcs_len = max(temp1, temp2)
    return lcs_len


def lcs_recursion_print(str1, str2): # Recursive approach O(2^n)
    #print(str1)
    #print(str2)
    if len(str1) == 0 or len(str2) == 0:
        lcs_len = ""
    elif str1[-1] == str2[-1]:
        lcs_len = str1[-1] + lcs_recursion_print(str1[:-1], str2[:-1])
    elif  str1[len(str1)-1] != str2[len(str2)-1]:
        temp1 = lcs_recursion_print(str1[:-1], str2)
        temp2 = lcs_recursion_print(str1, str2[:-1])
        lcs_len = max(temp1, temp2)
    return lcs_len



def lcs_dynamic(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    len_Mat = [[None for x in range(l2+1)] for x in range(l1+1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0 or j==0:
                len_Mat[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                len_Mat[i][j] = 1 + len_Mat[i-1][j-1]
            else:
                len_Mat[i][j] = max(len_Mat[i-1][j],len_Mat[i][j-1])
    return len_Mat[l1][l2]
    
    

st1 = "abcde"
st2 = "afcghdk"
print(lcs_recursion(st1, st2))
print(lcs_recursion_print(st1, st2)[::-1])
print(lcs_dynamic(st1, st2))