##########################################
######                              ######
######    Heap_Sort/Tri par tas     ######
######                              ######
##########################################

###### Complexity 
## Best : nlogn
## Avg  : nlogn
## Worst: nlogn


def heapify(A,n,i):

    largest = i
    l = (2*i+1)%n
    r = (2*i+2)%n

    if A[l] > A[i] and l<n:
        print(i)
        largest = l
    
    if A[r] > A[largest] and r<n:
        largest = r

    if largest != i :
        A[i] , A[largest] = A[largest], A[i]

        heapify(A,n,largest)
    

def heap_Sort(A):

    n = len(A)
    for i in range(n-1,-1,-1):
        heapify(A,n,i)
    
    return(A)


A = [-1,5,0,1,45,-56,56]
print(heap_Sort(A))