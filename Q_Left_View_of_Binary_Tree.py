"""
Left View of Binary Tree 

Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

link - https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1#

"""

def leftViewUtil(result, node,level):
    global max_level
    if (node == None): 
        return
        
    if (max_level < level):
        result.append(node.data)
        max_level = level
        
    leftViewUtil(result,node.left, level+1);
    leftViewUtil(result,node.right, level+1);
    
    
def LeftView(root):
    global max_level
    max_level = 0
    result = []
    leftViewUtil(result,root,1);
    return result