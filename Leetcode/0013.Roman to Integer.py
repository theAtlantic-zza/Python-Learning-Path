"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.给定一个罗马数字，将其转换成整数。

例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。
这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。

示例 1:
输入: s = "III"
输出: 3

示例 2:
输入: s = "IV"
输出: 4

示例 3:
输入: s = "IX"
输出: 9

示例 4:
输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""

#Things to remember
#Time Complexity:O(n)
#Space Complexity:O(1)

class MySolution(object):
    # Idea:
    # Traverse the Roman numeral string from left to right. 从左到右遍历罗马数字字符串。
    # If the current value is less than the next value, subtract it. 如果当前值小于下一个值，就减去当前值。
    # Otherwise, add it. 否则，加上当前值。
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        n = len(s)

        for i, num in enumerate(s):

            if i < n - 1 and dic[num] < dic[s[i + 1]]:
                ans -= dic[num]
            else:
                ans += dic[num]
        return ans


print(MySolution().romanToInt("III"))
print(MySolution().romanToInt("IV"))
print(MySolution().romanToInt("IX"))
print(MySolution().romanToInt("LVIII"))
print(MySolution().romanToInt("MCMXCIV"))

class StandardSolution(object):
    # Idea:
    # Traverse the string from left to right. 从左到右遍历字符串。
    # Compare the value of the current Roman numeral with the value of the next Roman numeral.
    # 比较当前罗马字符的值和下一个罗马字符的值。
    # If the current value is smaller than the next value, subtract the current value.
    # 如果当前值小于下一个值，就减去当前值。
    # Otherwise, add the current value. 否则，就加上当前值。
    # This works because in Roman numerals, a smaller numeral before a larger one means subtraction.
    # 这是因为在罗马数字中，较小的数字出现在较大的数字前面时表示减法。

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}

        total = 0

        for i in range(len(s)):
            # If the current character is not the last one,and its value is smaller than the next value, subtract the current value.
            # 如果当前字符不是最后一个，并且它的值小于下一个字符的值，就减去当前值。
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
print(StandardSolution().romanToInt("III"))
print(StandardSolution().romanToInt("IV"))
print(StandardSolution().romanToInt("IX"))
print(StandardSolution().romanToInt("LVIII"))
print(StandardSolution().romanToInt("MCMXCIV"))

