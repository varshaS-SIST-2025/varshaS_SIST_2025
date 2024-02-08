Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        p= [1] * n
        s= [1] * n
        t = [1] * n

        for i in range(1, n):
           p[i] = p[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
           s[i] = s[i + 1] * nums[i + 1]
        for i in range(n):
           t[i] = p[i] * s[i]

        return t

c=Solution()
n1 = [1, 2, 3, 4]
print(c.productExceptSelf(n1))  

n2 = [-1, 1, 0, -3, 3]
print(c.productExceptSelf(n2)) 
        
