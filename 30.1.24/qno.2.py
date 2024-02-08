                                  contain duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true



class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
          if num in seen:
              return True
          seen.add(num)
        return False

c=Solution()

nums1=[1,2,3,1]
print(c.containsDuplicate(nums1))

nums2=[1,2,3,4]
print(c.containsDuplicate(nums2))

nums3=[1,1,1,3,3,4,3,2,4,2]
print(c.containsDuplicate(nums3))
