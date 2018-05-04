##########################################
######                              ######
###### Insertion_Sort/TriInsertion  ######
######                              ######
##########################################

###### Complexity 
## Best : n
## Avg  : n**2
## Worst: n**2

def insertionSort(A):
    
    for i in range(1,len(A)):
        
        if A[i] < A[i-1]:
            j = i
            aux = A[j]
            while aux < A[j-1] and j > 0 :
                print("true2")
                A[j] = A[j-1]
                j = j-1
            A[j] = aux
    
    return A
    

A = [5,1,3,8,-5,13,4,46,-1]

print(insertionSort(A))