class Solution(object):
    def addBinary(self, a, b):
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])  # (was mistakenly a[i] in your code)
                j -= 1
            result.append(str(sum % 2))  # move out of the if
            carry = sum // 2              # move out of the if
        return ''.join(reversed(result))
