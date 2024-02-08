Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index  =  {} 
    
        for i, num in enumerate(nums):
            arg = target - num 
            if arg in num_index:
                 return [num_index[arg], i]
            num_index[num] = i
    
        return []

c=Solution()
num1=[2,7,11,15]
target1=9
print(c.twoSum(num1,target1)) 

num2=[3,2,4]
target2=6
print(c.twoSum(num2,target2)) 

num3=[3,3]
target3=6
print(c.twoSum(num3,target3))
  
