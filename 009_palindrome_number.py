class Solution(object):
    def isPalindrome(self, num):
        s = str(num)
        # return str(num) == str(num)[::-1]
        for i in range (len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True