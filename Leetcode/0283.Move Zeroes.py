"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序.
Note that you must do this in-place without making a copy of the array.
请注意 ，必须在不复制数组的情况下原地对数组进行操作.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

#Things to remember
#Time Complexity: original: O(n^2) optimized: O(n^2)
#Space Complexity:
from typing import List

class Solution(object):
    #Idea:
    #Traverse the array from left to right.
    #Whenever we encounter a 0, we automatically remove the 0 from the current position and append it to the end of array.
    #By doing this repeatedly, all the zeros will gradually move to the end of the array while the non-zero elements stay at the front.
    #Time Complexity: O(n^2)
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            if nums[i] == 0:
                temp=nums[i]
                nums.remove(temp)
                nums.append(temp)
#           print('nums',nums) 大数组时不能加,会超过输出限制

print (Solution().moveZeroes([0, 1, 0, 3, 12]))
print (Solution().moveZeroes([0]))

#GPT Optimized Version
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                n -= 1
            else:
                i += 1

#GPT Two pointers
class GPTSolution(object):
    #Idea:
    #This solution uses the two-pointer technique.
    #The fast pointer scans the array, while the slow pointer marks the position where the next non-zero element should be placed.
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)): #faster in Python
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


#Standard Solution:Double Pointers
class StandardSolution:
    #Idea:
    #Use two pointers: right scans the array, and left marks the position for the next non-zero element.
    #使用双指针：right 负责遍历数组，left 指向下一个非零元素应该放置的位置。
    #Whenever nums[right] is non-zero, swap it with nums[left] and move left forward.
    #This keeps all non-zero elements in their original order and moves all zeros to the end in-place.
    #当 nums[right] != 0 时，交换 nums[left] 和 nums[right]，然后让 left 前进一位。
    #这样可以在不使用额外数组的情况下，把所有非零元素按原顺序移到前面，并将所有 0 移到末尾。
    def Standard_moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:#more like C++
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
