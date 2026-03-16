"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
You must write an algorithm that runs in O(n) time.
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""

#Things to remember
#Idea:
# Traverse all numbers and only start counting when a number is the beginning of a sequence.
# 遍历所有数字，只有当某个数字是连续序列的起点时才开始统计。
# A number is the start of a sequence if its previous number does not exist.
# 如果一个数字的前一个数字不存在，那么它就是连续序列的起点。
# From the starting number, keep checking the next numbers (x+1, x+2, ...) until the sequence ends.
# 从这个起点开始，不断检查后面的数字（x+1, x+2 ...），直到连续序列结束。
# Use a set to achieve O(1) lookup time when checking if a number exists.
# 使用 set 来存储所有数字，这样查找某个数字是否存在可以满足 O(1) 的时间复杂度。
# Only expanding from sequence starts avoids repeated work.
# 只从序列起点开始扩展，可以避免重复计算。
#Time Complexity:O(n)
#Space Complexity:O(n)

#Standard Solution:
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums) #把nums转成哈希集合 change nums into the hash-set
        longest = 0 #record the maximum length of consecutive sequence found so far 记录目前找到的最长连续序列长度

        for x in num_set:#遍历哈希集合 traverse the hash set
            if x - 1 not in num_set:#如果x不是序列起点 直接跳过 if x is not the beginning of sequence
                y = x
                while y in num_set:#move forward while next num exists in the set 继续查找下一个数是否在哈希集合中
                    y += 1 #After the end of cycle, y-1 is the last num in this hash set
                longest = max(longest, y - x)
        return longest

#Wrong/Partial Right
class MySolution(object):
    #Time Complexity:O(n^2)--->Did not meet the Criteria
    #Problem:Nums was still a list,when traversing it, python has to scan the list one by one,
    #Therefore,the inner while check was also expensive,the time complexity limit easily exceeded on large inputs.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            if i-1 not in nums:
                j = i #j = 1
                      # UnboundLocalError 变量j使用之前没有被赋值 输入[0,-1]两个条件都不成立
                while j in nums:
                    j += 1
                ans = max(ans, j - i)
        return ans

print(MySolution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(MySolution().longestConsecutive([100,4,200,1,3,2]))
