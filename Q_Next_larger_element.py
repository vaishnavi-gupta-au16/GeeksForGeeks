"""
"""
Next larger element
Given an array A[] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
Example 1
Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
"""

def nextLargerElement(a,n):
    n = len(a)
    stack = list()
    
    nextLargerElement = [0] * len(a)

    for idx, val in enumerate(a):
        if len(stack) == 0:
            stack.append(idx)
        else:
            cur = val
            
            while len(stack) != 0 and a[stack[-1]] < cur:
                x = stack[-1]
                stack.pop()
                nextLargerElement[x] = cur
            stack.append(idx)
    
    while len(stack) != 0:
        x = stack[-1]
        stack.pop()
        nextLargerElement[x] = -1
        
        res = nextLargerElement
    return res