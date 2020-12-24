"""
Merge Sort

Merge Sort is a Divide and Conquer algorithm. It repeatedly divides the array into two halves and combines them in sorted manner. 

Given an array arr[], its starting position l and its ending position r. Merge Sort is achieved using the following algorithm. 

MergeSort(arr[], l,  r)
    If r > l
         1. Find the middle point to divide 
            the array into two halves:  
                 middle m = (l+r)/2
         2. Call mergeSort for first half:   
                 Call mergeSort(arr, l, m)
         3. Call mergeSort for second half:
                 Call mergeSort(arr, m+1, r)
         4. Merge the two halves sorted in 
            step 2 and 3:
                 Call merge(arr, l, m, r)
Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output: 1 3 4 7 9

Link - https://practice.geeksforgeeks.org/problems/merge-sort/1#

"""
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]

        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()