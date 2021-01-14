"""
Top View of Binary Tree

Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Print from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3

link - https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#

"""
def topviewu(root,d,vd,lv):
    if not root:
        return
    if vd in d:
        if d[vd][0]>lv:
            d[vd]=(lv,root.data)
    else:
        d[vd]=(lv,root.data)
    topviewu(root.left,d,vd-1,lv+1)
    topviewu(root.right,d,vd+1,lv+1)
    


def topView(root):
    d=dict()
    topviewu(root,d,0,0)
    for e in sorted(d):
        print(d[e][1],end=' ')
        