"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

Anagrams:An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once
字母异位词:字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
"""


#Things to remember

#defaultdict:defaultdict is a dictionary that automatically creates a default value for a missing key.
#defaultdict(default_type)
#-->from collections import defaultdict
#-->table = defaultdict(list)

#Time complexity:O(n* k log k) n = num of strings;k = avr len of each string
#There are n strings, and each string needs to be sorted,sorting a string of length k takes O(k log k) time, the overall time complexity is O(n * k log k)
#一共有n个字符串,每个字符串都要排序,排序一个长度为k的字符串需要O(k log k)
#Space Complexity:O(nk)

class Solution(object):

    #Idea:
    # Sort each string and use the sorted result as the key.
    #把每个字符串排序，排序后的结果作为哈希表的key。
    # Strings that are anagrams will have the same sorted form.
    # Use a hash map to group strings with the same key.

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        for s in strs:
            key = tuple(sorted(s))#list-->tuple 不可变对象才可作为字典key
            if key not in table:
                table[key] = []
            table[key].append(s)
        return list(table.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(['a']))
print(Solution().groupAnagrams(['']))

#Standard Solution
from collections import defaultdict#要从Python标准库里的collections模块import

class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        table = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            table[key].append(s)
        return list(table.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(["a"]))

