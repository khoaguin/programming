class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        n="".join(ch for ch in s if ch.isalnum()).lower()
        if len(n) == 0 or len(n) == 1:
            return True
        if len(n) == 2:
            if n[0] == n[1]:
                return True
            else:
                return False
        start = 0
        end = len(n) - 1
        while (start != end) and (start < len(n)/2):
            if n[start] == n[end]:
                start += 1
                end -= 1
            else:
                return False
        return True