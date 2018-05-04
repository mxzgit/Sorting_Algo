##########################################
######                              ######
###### Selection_Sort/TriSelection  ######
######                              ######
##########################################

###### Complexity 
## Best : n**2
## Avg  : n**2
## Worst: n**2


def selection_sort(A):

    for i in range(0,len(A)-1):
        min_i = A[i]
        min_j = i+1
        for j in range(i+1,len(A)):
            if A[j] < A[min_j]:
                min_j = j
        
        if A[i] > A[min_j]:
            A[i], A[min_j] = A[min_j], A[i]
    

    return A



A = [5,1,3,8,-5,13,4,46,-1]

print(selection_sort(A))