"""
Write a function to find the longest common prefix string amongst an array of strings.
编写一个函数来查找字符串数组中的最长公共前缀。

If there is no common prefix, return an empty string "".
如果不存在公共前缀，返回空字符串 ""。

strs[i] consists of only lowercase English letters if it is non-empty. strs[i]如果非空则仅有小写英文字母组成

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
#Things to remember
# strs.sort()          -> sort strings in lexicographical order 按字典序对字符串排序

# strs[0]              -> first string after sorting

# strs[-1]             -> last string after sorting 排序后的最后一个字符串

# s[:i]                -> substring from index 0 to i-1 从下标 0 截取到 i-1

# while condition      -> keep looping while the condition is True 当条件为 True 时持续循环

# prefix = strs[0]         -> use the first string as the initial prefix 先把第一个字符串当作初始公共前缀

# self.lcp(str1, str2)     -> find the longest common prefix of two strings 求两个字符串的最长公共前缀

# min(len(str1), len(str2))
# the common prefix cannot be longer than the shorter string 公共前缀长度不可能超过较短字符串的长度

# str1[:index]             -> substring from 0 to index - 1 从下标 0 截取到 index - 1

# Time Complexity: O(n log n)-->O(mn) m：字符串平均长度 n：字符串个数
# Sorting takes O(n log n), and comparing two strings takes O(m).排序需要 O(n log n)，比较两个字符串需要 O(m)。

# Space Complexity: O(1) or O(log n)--->O(1)

class MySolution(object):
    # Idea:
    # First sort the list.先排序
    # Then compare only the first and last strings,然后只比较排序后的首尾字符串
    # because they are the most different after sorting.因为他们在排序前后差异最大
    # If they share the same prefix,如果他们有相同前缀
    # then all the strings in between must also share it.那中间字符串一定有此前缀
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return " "

        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0

        # Keep comparing while: 持续比较，前提是：
        # 1. i does not go out of range of first
        # 2. i does not go out of range of last
        # 3. the characters at position i are the same
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
        # first[:i] means taking the substring from the beginning up to i. 表示从开头截取到下标 i 之前。

print(MySolution().longestCommonPrefix(["flower", "flow", "flight"]))
print(MySolution().longestCommonPrefix(["dog", "racecar", "car"]))


from typing import List
class StandardSolution:
    """
    横向扫描 Horizontal Scanning
    """
    # Idea:
    # Use the first string as the initial prefix. 先把第一个字符串当作初始公共前缀。
    # Then compare it with each remaining string one by one.然后依次和后面的每个字符串比较
    # Every time, update prefix to the common prefix of the two strings.每比较一次，就把 prefix 更新为这两个字符串的公共前缀。
    # If prefix becomes empty, stop early.如果 prefix 变成空字符串，就可以提前结束。

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Return the longest common prefix among all strings.
        返回所有字符串的最长公共前缀。
        """

        # If the list is empty, return an empty string directly. 如果数组为空，直接返回空字符串。
        if not strs:
            return ""

        # Start with the first string as the initial prefix. 先用第一个字符串作为初始公共前缀。
        prefix = strs[0]

        # Compare prefix with each remaining string. 依次把 prefix 和后面的每个字符串进行比较。
        for i in range(1, len(strs)):
            prefix = self.lcp(prefix, strs[i])

            # If there is no common prefix, return early. 如果已经没有公共前缀了，就提前结束。
            if not prefix:
                break

        return prefix

    def lcp(self, str1: str, str2: str) -> str:
        """
        Return the longest common prefix of two strings.
        返回两个字符串的最长公共前缀。
        """

        # The common prefix cannot be longer than the shorter string.
        # 公共前缀长度不可能超过较短字符串的长度。
        length = min(len(str1), len(str2))

        # index is used to compare characters one by one.
        # index 用来逐个比较字符。
        index = 0

        # Keep moving forward while the characters are the same. 只要当前位置字符相同，就继续往后比较。
        while index < length and str1[index] == str2[index]:
            index += 1

        # Return the common part from the beginning to index - 1. 返回从开头到 index - 1 的公共部分。
        return str1[:index]

print(StandardSolution().longestCommonPrefix(["flower", "flow", "flight"]))
print(StandardSolution().longestCommonPrefix(["dog", "racecar", "car"]))