"""
Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1, the task is to find the number of ways the floor can be tiled. A tile can either be placed horizontally i.e as a 1 x 2 tile or vertically i.e as 2 x 1 tile. Print the answer modulo 109+7.

 

Example 1:

Input:
W = 3
Output:
3
Explanation:
We need 3 tiles to tile the board
of size  2 x 3. 
We can tile in following ways:
1) Place all 3 tiles vertically. 
2) Place first tile vertically.
and remaining 2 tiles horizontally.
3) Place first 2 tiles horizontally
and remaining tiles vertically.

Link - https://practice.geeksforgeeks.org/problems/ways-to-tile-a-floor5836/1#
"""
class Solution:
    def numberOfWays(self, N):
        # code here
        if N == 0:
            return 1
        if N < 0:
            return 0
        ways = self.numberOfWays(N-1) + self.numberOfWays(N-2)
        return ways