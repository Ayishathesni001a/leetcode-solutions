class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        reverse_string = string[::-1]
        if string == reverse_string:
            return True
        else:
            return False    
