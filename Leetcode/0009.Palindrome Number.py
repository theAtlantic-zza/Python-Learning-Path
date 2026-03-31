"""
Given an integer x, return true if x is a palindrome, and false otherwise.
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。         例如，121 是回文，而 123 不是。

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.
"""

#Things to remember

# s[::-1]              -> reverse a string by slicing
# s[::-1]              -> 用切片反转字符串

# ''.join(reversed(s)) -> reverse a string by reversed()
# ''.join(reversed(s)) -> 用 reversed() 反转字符串

# nums.reverse()       -> reverse a list in place
# nums.reverse()       -> 原地反转列表

#Time Complexity:O(n)--->O(log n)
#Space Complexity:O(n)--->O(1)

class MySolution(object):
    #Idea: Convert the integer to a string, reverse the string, and compare it with the original one.
    #i have neglected the requirement that x must be an integer
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) !=str(x)[::-1]:
            # In slicing, [start:end:step], step = -1 means moving backward,so [::-1] reverses the string.
            # 在切片 [start:end:step] 中，step = -1 表示倒着取，所以 [::-1] 可以反转字符串。
            return False
        return True

print(MySolution().isPalindrome(121))
print(MySolution().isPalindrome(-121))
print(MySolution().isPalindrome(0))

class Solution(object):
    # Idea:
    # We only reverse half of the number and compare it with the other half. 我们只需要反转数字的一半，再和另一半进行比较。
    # Negative numbers are not palindromes. 负数一定不是回文数。
    # If a number ends with 0, it cannot be a palindrome，unless the number itself is 0.
    # 如果一个数末尾是 0，那么它不可能是回文数，除非它本身就是 0。
    # For even-length numbers, the first half should be equal to the reversed second half.
    # 对于偶数位数字，前半部分应该等于反转后的后半部分。
    # For odd-length numbers, we can remove the middle digit by reverted // 10.
    # 对于奇数位数字，可以通过 reverted // 10 去掉中间那一位。

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False


        if x % 10 == 0 and x != 0:#直接检测x是否为10的倍数（末尾是0）
            return False ## Directly check whether x is a multiple of 10, which means it ends in 0.

        # reverted stores the reversed second half of the number.
        # reverted 用来保存反转后的后半部分数字。
        reverted = 0 #赋值，int

        # Reverse only half of the number.
        # 只反转数字的一半。
        while x > reverted:
            # Take the last digit of x and append it to reverted.
            # 取出 x 的最后一位，并把它拼接到 reverted 后面。
            reverted = reverted * 10 + x % 10 # %，求模，取余数

            # Remove the last digit from x.
            # 去掉 x 的最后一位。
            x //= 10

        # If the length is even, x should equal reverted.
        # If the length is odd, x should equal reverted // 10.
        # 如果位数是偶数，x 应该等于 reverted。
        # 如果位数是奇数，x 应该等于 reverted // 10。
        return x == reverted or x == reverted // 10
        # reverted // 10   //整除
        # For odd-length numbers, remove the middle digit from reverted by reverted // 10.
        # # 对于奇数位数字，用 reverted // 10 去掉 reverted 中的中间那一位
        # Q:为什么去不掉偶数？ A:x ==reverted 偶数已经return了

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(0))