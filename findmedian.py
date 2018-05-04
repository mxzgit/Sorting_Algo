def findMedianSortedArrays(nums1, nums2):

    A = nums1+nums2
    A.sort()
    #quicksort(A,0,len(A)-1)
    if len(A)%2 == 0:
        return (A[len(A)//2-1]+A[len(A)//2])/2
    else:
        return A[len(A)//2]



def partition(t,low,high):

    pivot = t[high]
    indice = low - 1

    for j in range(low,high):
        if t[j]<=pivot :
            indice = indice + 1
            t[indice] , t[j] = t[j] , t[indice]

    t[indice+1] , t[high] = t[high] , t[indice+1]
    return indice + 1


def quicksort(t,low,high):
    if low < high :
        pivot = partition(t,low,high) 
        quicksort(t,low,pivot-1)
        quicksort(t,pivot+1,high)

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1,nums2))