"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack.
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
Return -1, if needle is not part of haystack.
如果 needle 不是 haystack 的一部分，则返回 -1 。

示例 1：
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。

示例 2：
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
"""

#Things to remember
#切片 slice: string[start : end]--->start:inclusive; end:exclusive 有前无后 左闭右开

#Time Complexity:O((n - m + 1) * m) ≈ O(n * m)      StandardSolution:O(n+m)
#Space Complexity:O(m)


class MySolution(object):
    #Idea:
    # Use brute force for traversing to check every possible starting position in haystack.
    # 使用暴力遍历的方法，检查 haystack 中每一个可能的起始位置。
    # For each index i, slice a substring with the same length as needle.
    # 对于每一个下标 i，切出一个与 needle 长度相同的子字符串。
    # Compare the sliced substring with needle.
    # 将切出来的子字符串和 needle 进行比较。
    # If they are equal, return the current index i.
    # 如果二者相等，就返回当前下标 i。
    # If no match is found after checking all possible positions, return -1.
    # 如果所有可能的位置都检查完了还没找到，就返回 -1。
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            # len(haystack) - len(needle) + 1
            # means the total number of valid starting indices. 表示所有合法起始下标的总数。
            if haystack[i:i+len(needle)] == needle:
                #slice a substring of the same length as needle 切出一个和needle长度相同的子字符串
                #左闭右开区间 start at index i， stop before index i + len(needle)
                return i
        return -1

print(MySolution().strStr("leetcode", "leeto"))
print(MySolution().strStr("sadbutsad", "sad"))
print(MySolution().strStr("eeehijack", "jack"))
print(MySolution().strStr("lebronjames", "bron"))
print(MySolution().strStr("leetcode", "tco"))

class StandardSolution(object):
        # Idea:
        # Use KMP (Knuth-Morris-Pratt) algorithm to avoid re-checking characters.
        # 使用 KMP（字符串匹配）算法，避免重复比较字符。
        # Build an LPS (Longest Prefix Suffix) array for the pattern (needle).
        # 为 needle 构建 LPS（最长相等前后缀）数组。

        # LPS[i] means:
        # the length of the longest proper prefix which is also a suffix
        # for the substring needle[0:i+1].
        # LPS[i] 表示：
        # 在 needle[0:i+1] 中，最长的“前缀 = 后缀”的长度。

        # Then use two pointers to scan haystack and needle:
        # 然后用两个指针同时遍历 haystack 和 needle：

        # If characters match, move both pointers forward.
        # 如果字符匹配，两个指针同时前进。

        # If mismatch happens:
        # 如果发生不匹配：
        # Do NOT move haystack pointer back.
        # 不回退 haystack 指针

        # Use LPS array to move needle pointer.
        # 使用 LPS 数组调整 needle 指针
        # This avoids redundant comparisons and achieves linear time.
        # 这样避免重复比较，实现线性时间复杂度。

        def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """

            # Edge case 边界情况：讨论字符串为空时返回值情况
            if needle == "":
                return 0

            lps = self.buildLPS(needle)

            # i -> pointer for haystack
            # j -> pointer for needle
            i = 0
            j = 0

            while i < len(haystack):
                # If characters match, move both pointers 如果字符匹配，两个指针同时前进
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1

                    # If we matched the whole needle 如果 needle 全部匹配成功
                    if j == len(needle):
                        return i - j  # start index

                else:
                    # If mismatch happens 如果发生不匹配
                    if j != 0:
                        # Use LPS to skip comparisons 利用 LPS 跳过不必要的比较
                        j = lps[j - 1]
                    else:
                        # If j == 0, just move i 如果 j 在起点，只能移动 i
                        i += 1
            return -1

        # Build LPS array 构建 LPS 数组
        def buildLPS(self, pattern):
            lps = [0] * len(pattern)
            # length of previous longest prefix suffix
            # 当前最长前后缀长度
            length = 0
            i = 1

            while i < len(pattern):

                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

print(StandardSolution().strStr("leetcode", "leet"))     # 0
print(StandardSolution().strStr("sadbutsad", "sad"))     # 0
print(StandardSolution().strStr("hijackeee", "jack"))    # 2
print(StandardSolution().strStr("lebronjames", "bron"))  # 2
print(StandardSolution().strStr("aaaaa", "bba"))         # -1
print(StandardSolution().strStr("mississippi", "issip")) # 4
