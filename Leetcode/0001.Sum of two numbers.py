"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
给定一个整数数组nums和一个整数目标值target,请在该数组中找出和为目标值的那两个整数并返回他们的数组下标
You may assume that each input would have exactly one solution, and you may not use the same element twice.
你可以假设每种输入只会对应一个答案,并且你不能使用两次相同的元素
You can return the answer in any order.

示例:
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]
"""

#Things to remember

#index():Find the index of the first occurrence of a value 查找某个值第一次出现的位置

#enumerate():Return pairs of (index, value) while iterating over an iterable.在遍历列表时,同时得到元素的下标和元素的值
#enumerate(item, start=0)<---item:list,tuple.string,set  start:Specify the number from which the index starts, the default is 0
#for index, value in enumerate(iterable):


# Time Complexity: O(n^2) The rate at which an algorithm's running time grows as the input size increases.
# 时间复杂度:O(n^2) 输入规模变大时,算法运行时间增长的速度
# The outer loop runs n times, and the "in" operation may scan up to n elements.
# 外层for循环遍历nums需n次,内层判断"res in nums[i+1]"最多需要遍历<=n次
# Therefore, the total complexity is approximately n * n.

class Solution(object):
    #Idea:
    #Traverse the list.For each number[i], compute res = target - nums[i]
    #Check whether res exists in the remaining part of the list nums[i+1:]
    #If it exists, return the indices of the two numbers.

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i, nums.index(res,i+1)]
        raise ValueError("No solution found")
        #if there are not such two correct number, the program will raise a ValueError with the message "No solution found".

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))

#Standard Solution
class StandardSolution(object):
    # Idea:
    # Use a hash map to store numbers we have already seen and their indices.
    # 使用哈希表记录“已经遍历过的数字”和它对应的下标
    # For each number, compute its complement: target - num.
    # 每遍历到一个数字 num，就计算它还差多少才能等于 target，即 target - num。
    # If the complement is already in the hash map, we have found the answer,answer these two indexes directly
    # 如果这个差值已经在哈希表中，说明之前已经出现过另一个数和当前数配对成功，直接返回这两个数的下标
    # Otherwise, store the current number and its index in the hash map.

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {} #Create an empty dict
        #the hash map means quickly recording whether the num has occurred and the index it occurred
        #哈希表作用是快速记录一个数是否出现过以及它出现的位置

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []

print(StandardSolution().twoSum([2,7,11,15], 9))
print(StandardSolution().twoSum([3,2,4], 6))
print(StandardSolution().twoSum([2,2], 4))